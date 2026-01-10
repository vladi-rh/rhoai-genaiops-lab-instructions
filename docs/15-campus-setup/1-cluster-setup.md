## AI501 Cluster Setup

<p class="warn">
    ⛷️ <b>NOTE</b> ⛷️ - You need an OpenShift 4.14+ cluster with cluster-admin privilege.
</p>

Just like we practice throughout the course, we keep the cluster configuration as code in a GitHub repository: https://github.com/rhoai-genaiops/deploy-lab

This repository has three main parts:
- **Operators**: A Helm chart to deploy operators including OpenShift AI, GitOps, Pipelines, and GPU support.
- **Toolings**: A Helm chart to configure shared infrastructure like MinIO, observability stack, and workbench templates.
- **Student Content**: A Helm chart for per-student environments including ArgoCD instances and Data Science projects.

## Prerequisites

Before you begin, ensure you have:

- OpenShift 4.14+ cluster with cluster-admin access
- Helm 3.x installed
- `oc` CLI configured and authenticated
- (Optional) AWS credentials for GPU machine provisioning

### GPU Requirements

This lab requires **3 GPU nodes** with specific taints:

| Component | GPU Count | Instance Type | Taint |
|-----------|-----------|---------------|-------|
| Docling Serve | 1 | g4dn (T4) | `nvidia.com/gpu.instance-type=g4dn` |
| Llama 3.2 (cloud-model) | 1 | g5 (A10G) | `nvidia.com/gpu.instance-type=g5` |
| Llama 3.2 FP8 (quantized-model) | 1 | g5 (A10G) | `nvidia.com/gpu.instance-type=g5` |

<p class="tip">
    💡 <b>TIP</b> 💡 - If you have different taints on your GPU nodes, update the deployment tolerations in the <code>student-content/templates/</code> directory.
</p>

## Quick Installation

The fastest way to get started is using the automated installation script.

1. **Clone the repository**

    ```bash
    git clone https://github.com/rhoai-genaiops/deploy-lab.git
    cd deploy-lab
    ```

2. **Configure your deployment**

    Edit `student-content/values.yaml` before running the installation:

    ```yaml
    cluster_domain: apps.your-cluster.example.com  # Your OpenShift apps domain
    attendees: 20                                   # Number of students to create
    ```

    To find your cluster domain:
    ```bash
    oc get ingresses.config.openshift.io cluster -o jsonpath='{.spec.domain}'
    ```

3. **Run the installation**

    ```bash
    ./install.sh
    ```

    This script will:
    - Install required operators (RHOAI, Pipelines, GitOps, GPU Operator)
    - Deploy shared tooling infrastructure
    - Create student environments
    - Configure OAuth authentication with HTPasswd
    - Set up ArgoCD for multi-tenancy
    - Configure Tekton and user workload monitoring

## Step-by-Step Installation

If you prefer more control over the installation process, you can run each step manually.

### Step 1: Install Operators

First, install the base operators that provide the platform capabilities:

```bash
cd deploy-lab
helm upgrade --install ai501-base operators \
    --namespace ai501 \
    --create-namespace
```

Wait for the GitOps operator to be ready:

```bash
oc wait --for=jsonpath='{.status.availableReplicas}'=1 \
    -n openshift-gitops deployment/cluster
```

<p class="warn">
    ⏳ <b>NOTE</b> ⏳ - This step might take up to 15 minutes as operators are installed and reconciled.
</p>

### Step 2: Install Shared Toolings

Deploy the shared infrastructure components:

```bash
helm upgrade --install ai501-toolings toolings \
    --namespace ai501 \
    --create-namespace
```

This installs:
- MinIO (S3-compatible storage)
- Observability stack (Prometheus, Grafana, Tempo)
- Custom workbench templates

### Step 3: Install Student Content

Deploy the per-student resources:

```bash
helm upgrade --install ai501-student-content student-content \
    --namespace ai501 \
    --create-namespace
```

<p class="tip">
    💡 <b>TIP</b> 💡 - Make sure you've configured <code>values.yaml</code> with your cluster domain and desired number of attendees before running this step.
</p>

### Step 4: Configure Authentication

Set up HTPasswd authentication for students:

```bash
oc patch --type=merge OAuth/cluster -p '{
    "spec": {
        "identityProviders": [{
            "name": "Students",
            "type": "HTPasswd",
            "mappingMethod": "claim",
            "htpasswd": {
                "fileData": {
                    "name": "htpasswd-ai501"
                }
            }
        }]
    }
}'
```

### Step 5: Configure ArgoCD for Multi-Tenancy

Enable ArgoCD for student namespaces. The install script automatically calculates the namespace list based on your attendee count:

```bash
# Example for 5 attendees
oc -n openshift-gitops-operator patch subscriptions.operators.coreos.com/openshift-gitops-operator \
    --type=json \
    -p '[
        {
            "op": "add",
            "path": "/spec/config/env",
            "value": [{"name": "DISABLE_DEFAULT_ARGOCD_INSTANCE", "value": "true"}]
        },
        {
            "op": "add",
            "path": "/spec/config/env/1",
            "value": {"name": "ARGOCD_CLUSTER_CONFIG_NAMESPACES", "value": "user1-toolings,user2-toolings,user3-toolings,user4-toolings,user5-toolings"}
        }
    ]'
```

### Step 6: Configure Tekton and Monitoring

Optimize Tekton for cost and configure user workload monitoring:

```bash
# Disable affinity assistant for cost optimization
oc patch tektonconfig config --type merge -p '{"spec":{"pipeline":{"disable-affinity-assistant":true}}}'

# Configure user workload monitoring
oc -n openshift-user-workload-monitoring patch configmap user-workload-monitoring-config \
    --type=merge \
    -p '{"data": {"config.yaml": "prometheus:\n  logLevel: debug\n  retention: 15d\nalertmanager:\n  enabled: true\n  enableAlertmanagerConfig: true\n"}}'
```

## GPU Provisioning (AWS)

If you're running on AWS and need to provision GPU nodes, you can use the machine provisioning script:

```bash
./machineset.sh
```

This script supports provisioning various GPU instance types:
- T4 (g4dn instances)
- A10G (g5 instances)
- A100 (p4d instances)
- H100 (p5 instances)
- L40 instances

## Verify The Installation

After installation completes, verify everything is working:

1. **Check operators are ready**:
    ```bash
    oc get csv -n openshift-operators
    ```

2. **Check student namespaces**:
    ```bash
    oc get namespaces | grep user
    ```

3. **Check pods in the main namespace**:
    ```bash
    oc get pods -n ai501
    ```

4. **Check Helm releases**:
    ```bash
    helm list -n ai501
    ```

5. **Monitor ArgoCD sync status**:
    ```bash
    oc get applications -A
    ```

Log in to the cluster via UI and use `htpasswd` login with your student username and password. You should only see `<USER_NAME>` and `<USER_NAME>-toolings` namespaces.

## Getting the Necessary Links

The necessary links such as OpenShift console, OpenShift AI Dashboard, and other tools are embedded in the top right of this page under `Quick Links`.

## Troubleshooting

### Helm Release Issues

If a Helm release fails, check the release status:

```bash
helm list -n ai501
helm status <release-name> -n ai501
```

### ConfigMap Already Exists

If you encounter errors about ConfigMaps already existing (not owned by Helm), you may need to delete them first:

```bash
oc delete configmap <configmap-name> -n <namespace>
```

Then re-run the Helm installation.

### GPU Pods Not Scheduling

If GPU workloads aren't scheduling, verify:

1. GPU nodes are available:
    ```bash
    oc get nodes -l nvidia.com/gpu.present=true
    ```

2. Check node taints match deployment tolerations:
    ```bash
    oc describe node <gpu-node-name> | grep Taints
    ```

3. Verify the NVIDIA GPU operator is running:
    ```bash
    oc get pods -n nvidia-gpu-operator
    ```
