# 🚀 Deploy LiteMaaS

> 🔧 **Persona Focus: The AI Engineer** — Time to put on your infrastructure hat! You're the expert who deploys models once so everyone else can benefit. Think of yourself as the person who builds the water treatment plant while everyone else just turns on their faucets.

---

## 🎯 What You'll Build

By the end of this lesson, you'll have a fully functional LiteMaaS deployment on OpenShift:

[Image: Deployment architecture diagram showing:
- OpenShift namespace "maas" containing:
  - LiteMaaS Frontend (Pod)
  - LiteMaaS Backend (Pod)
  - PostgreSQL database (Pod with PVC)
  - LiteLLM proxy (Pod)
- Connections to existing model endpoints (vLLM/KServe from previous modules)
- OpenShift Route exposing the LiteMaaS UI
- OpenShift OAuth integration for authentication]

---

## ✅ Prerequisites Check

Before we begin, let's make sure everything is in place:

### 1. OpenShift Access

Make sure you can access the cluster:

```bash
oc login https://api.<CLUSTER_DOMAIN>:6443 -u <USER_NAME> -p <PASSWORD>
```

### 2. Existing Model Endpoints

LiteMaaS is a *gateway* to models — it doesn't deploy models itself. You should have models available from previous modules:

```bash
# Check if you have model inference services running
oc get inferenceservices -n <USER_NAME>-canopy
```

You should see your Granite or other model endpoints listed.

### 3. Namespace Preparation

For this exercise, we'll deploy LiteMaaS in a dedicated namespace:

```bash
# Create the maas namespace (if it doesn't exist)
oc new-project <USER_NAME>-maas || oc project <USER_NAME>-maas
```

---

## 📦 Step 1: Clone the LiteMaaS Repository

Let's get the LiteMaaS code:

```bash
cd ~/experiments
git clone https://github.com/rh-aiservices-bu/litemaas.git
cd litemaas
```

Take a moment to explore the structure:

```
litemaas/
├── frontend/          # React + PatternFly UI
├── backend/           # Fastify API server
├── deploy/           # Kubernetes manifests
│   ├── base/         # Base resources
│   └── overlays/     # Environment-specific configs
├── docker/           # Container build files
└── docs/             # Additional documentation
```

---

## ⚙️ Step 2: Configure the Deployment

The deployment needs a few configuration values. We'll create a Kustomize overlay for our environment.

### 2.1 Create Your Overlay Directory

```bash
mkdir -p deploy/overlays/<USER_NAME>
```

### 2.2 Create the Kustomization File

Create `deploy/overlays/<USER_NAME>/kustomization.yaml`:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: <USER_NAME>-maas

resources:
  - ../../base

patches:
  - path: patches/config.yaml
```

### 2.3 Create the Configuration Patches

Create `deploy/overlays/<USER_NAME>/patches/config.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: litemaas-config
data:
  # Database configuration
  DATABASE_HOST: "postgresql"
  DATABASE_PORT: "5432"
  DATABASE_NAME: "litemaas"

  # LiteLLM endpoint (adjust based on your model deployment)
  LITELLM_ENDPOINT: "http://litellm:4000"

  # Frontend URL (will be updated after route creation)
  FRONTEND_URL: "https://litemaas-<USER_NAME>-maas.apps.<CLUSTER_DOMAIN>"

  # OAuth configuration (OpenShift)
  OAUTH_ENABLED: "true"
  OAUTH_ISSUER: "https://oauth-openshift.apps.<CLUSTER_DOMAIN>"
---
apiVersion: v1
kind: Secret
metadata:
  name: litemaas-secrets
type: Opaque
stringData:
  # Database credentials
  DATABASE_USER: "litemaas"
  DATABASE_PASSWORD: "changeme-in-production"

  # JWT secret for token signing
  JWT_SECRET: "your-super-secret-jwt-key-change-in-production"

  # OAuth client credentials (we'll get these from OpenShift)
  OAUTH_CLIENT_ID: "litemaas"
  OAUTH_CLIENT_SECRET: "to-be-configured"
```

> ⚠️ **Note:** In a real deployment, you'd use proper secrets management (e.g., External Secrets Operator, Vault). For this lab, we're keeping it simple.

---

## 🔐 Step 3: Configure OAuth with OpenShift

LiteMaaS uses OpenShift OAuth for authentication. This means users can log in with their OpenShift credentials!

### 3.1 Create an OAuth Client

```bash
oc create -f - <<EOF
apiVersion: oauth.openshift.io/v1
kind: OAuthClient
metadata:
  name: litemaas-<USER_NAME>
grantMethod: auto
redirectURIs:
  - https://litemaas-<USER_NAME>-maas.apps.<CLUSTER_DOMAIN>/api/auth/callback
secret: $(openssl rand -base64 32)
EOF
```

### 3.2 Get the OAuth Client Secret

```bash
# The secret was generated above - save it!
oc get oauthclient litemaas-<USER_NAME> -o jsonpath='{.secret}'
```

Update your `patches/config.yaml` with the actual OAuth client secret.

---

## 🚀 Step 4: Deploy to OpenShift

Now the fun part — let's deploy!

### 4.1 Apply the Kustomize Configuration

```bash
oc apply -k deploy/overlays/<USER_NAME>
```

### 4.2 Watch the Deployment

```bash
# Watch pods come up
oc get pods -n <USER_NAME>-maas -w
```

You should see:
- `postgresql-*` — Database pod
- `litemaas-backend-*` — API server
- `litemaas-frontend-*` — React UI
- `litellm-*` — OpenAI-compatible proxy

[Image: Terminal screenshot showing all pods in Running state with columns: NAME, READY, STATUS, RESTARTS, AGE]

### 4.3 Verify Services

```bash
# Check all services are running
oc get svc -n <USER_NAME>-maas
```

### 4.4 Get the Route URL

```bash
# Find your LiteMaaS URL
oc get route litemaas -n <USER_NAME>-maas -o jsonpath='{.spec.host}'
```

---

## 🔗 Step 5: Configure Model Connections

LiteMaaS uses LiteLLM as its backend proxy. We need to tell LiteLLM about our available models.

### 5.1 Get Your Model Endpoints

```bash
# Get the inference service URL from your canopy namespace
oc get inferenceservice -n <USER_NAME>-canopy -o jsonpath='{.items[0].status.url}'
```

### 5.2 Update LiteLLM Configuration

Create or update the LiteLLM config:

```bash
oc create configmap litellm-config -n <USER_NAME>-maas --from-literal=config.yaml="
model_list:
  - model_name: granite-8b
    litellm_params:
      model: openai/granite-8b
      api_base: https://your-model-endpoint.<CLUSTER_DOMAIN>/v1
      api_key: none

  - model_name: granite-3b
    litellm_params:
      model: openai/granite-3b
      api_base: https://your-other-model.<CLUSTER_DOMAIN>/v1
      api_key: none

general_settings:
  master_key: your-litellm-master-key
"
```

### 5.3 Restart LiteLLM to Pick Up Changes

```bash
oc rollout restart deployment/litellm -n <USER_NAME>-maas
```

---

## ✨ Step 6: Access the LiteMaaS UI

Open your browser and navigate to:

```
https://litemaas-<USER_NAME>-maas.apps.<CLUSTER_DOMAIN>
```

You should see the LiteMaaS login page!

[Image: LiteMaaS login page showing:
- LiteMaaS logo
- "Login with OpenShift" button
- Clean, professional PatternFly design
- Footer with version info]

### 6.1 First Login

1. Click **"Login with OpenShift"**
2. Enter your OpenShift credentials (`<USER_NAME>` / `<PASSWORD>`)
3. Authorize the LiteMaaS application
4. You're in! 🎉

### 6.2 Initial Admin Setup

The first user to log in becomes the admin by default. You should see:

[Image: LiteMaaS admin dashboard showing:
- Navigation sidebar with: Dashboard, Users, Models, API Keys, Analytics
- Main area showing welcome message and quick stats
- Cards for: Active Users, API Keys Created, Total Requests, Token Usage]

---

## 🔍 Verification Checklist

Before moving on, verify your deployment:

| Check | Command | Expected Result |
|-------|---------|-----------------|
| All pods running | `oc get pods -n <USER_NAME>-maas` | 4+ pods in Running state |
| Database accessible | Check backend logs | "Database connected" message |
| OAuth working | Try logging in | Successful redirect and login |
| LiteLLM responding | `curl http://litellm:4000/health` | 200 OK |
| Models visible | Check LiteMaaS UI | Models listed in admin panel |

---

## 🐛 Troubleshooting

### Pod not starting?

```bash
# Check pod events
oc describe pod <pod-name> -n <USER_NAME>-maas

# Check logs
oc logs <pod-name> -n <USER_NAME>-maas
```

### OAuth redirect failing?

Make sure your OAuth client redirect URI matches exactly:
```bash
oc get oauthclient litemaas-<USER_NAME> -o yaml
```

The redirect URI should be: `https://litemaas-<USER_NAME>-maas.apps.<CLUSTER_DOMAIN>/api/auth/callback`

### Can't see models?

Check the LiteLLM configuration and ensure your model endpoints are accessible:
```bash
# Test model endpoint from within the cluster
oc run curl-test --rm -it --restart=Never --image=curlimages/curl -- \
  curl -s https://your-model-endpoint/v1/models
```

---

## 🎯 What You've Accomplished

As the AI Engineer, you've just:

* ✅ Deployed a complete MaaS platform on OpenShift
* ✅ Configured OAuth for seamless authentication
* ✅ Connected existing model endpoints through LiteLLM
* ✅ Set up the foundation for centralized model access

[Image: Achievement unlocked style graphic with "🔧 AI Engineer" badge and text "Deployed LiteMaaS - Now everyone can share models instead of hoarding GPUs!"]

---

## 🎯 Next Steps

Your infrastructure is ready! Now it's time to hand off to the 👩‍💼 **Service Admin** to configure users, roles, and budgets.

**Continue to [Admin Configuration](./3-admin-configuration.md)** →
