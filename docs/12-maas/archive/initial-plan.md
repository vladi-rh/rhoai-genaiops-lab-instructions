# Module 12: Models as a Service (MaaS) - Initial Plan

## Context & Background

### Project Overview
This plan defines Module 12 "Models as a Service" for the GenAIOps Enablement course. The module will be located in `docs/12-maas/` and follows the patterns established by existing modules (e.g., `docs/4-ready-to-scale-201/`, `docs/5-grounded-ai/`).

### Key Resources
- **LiteMaaS Repository**: https://github.com/rh-aiservices-bu/litemaas
  - React + PatternFly 6 frontend
  - Fastify + PostgreSQL backend
  - LiteLLM integration for OpenAI-compatible API proxy
  - OAuth2/JWT authentication with OpenShift integration
  - Three-tier role hierarchy: admin, adminReadonly, user

- **Presentation Reference**: "How to become the hero of your AI story" (MaaS Summit Talk)
  - Located at: `docs/12-maas/text.txt` (full transcription)
  - Speakers: Erwan Granger, Guillaume Moutier, Karl Eklund (Red Hat AI BU)

### Target Audience
- Students who have completed **Modules 1-8** (full prerequisite chain)
- Familiar with: OpenShift, GitOps, RAG, Guardrails, Observability, and Agents
- Have working Canopy application from previous modules

### Decisions Made
1. **Exercises**: Comprehensive coverage - deployment, admin tasks, AND user experience
2. **Integration**: Module will integrate with the Canopy application
3. **Deployment**: Students will deploy LiteMaaS themselves (hands-on learning)
4. **Placeholders**: Will use standard placeholders (`<USER_NAME>`, `<CLUSTER_DOMAIN>`, etc.)

---

## Why MaaS? (Presentation Insights)

### The Problem (Origin Story)
From the presentation - a real scenario at Red Hat:
- Enterprise offers OpenShift AI cluster to all 19,000 employees
- Multiple users deploy the same model independently
- Example: 7 people deployed their own Granite 3-8B instance
- Result: 7 GPUs consumed, **0% utilization** (models sitting idle)
- Users report "no GPUs available" while GPUs are wasted

### Ideas That Were Discarded
1. **Increase auto-scaling max** - Too expensive, doesn't solve the root problem
2. **Set OpenShift quotas** - Prevents overuse but not duplication
3. **Use MIG (Multi-Instance GPU) slices** - Slices too small for large models

### The MaaS Solution
The "lightbulb moment":
1. Deploy each model **once** (by expert team)
2. Put an **API gateway** in front
3. Provide **self-service access to models**, not GPUs
4. Track usage and enable chargeback

### Before vs After MaaS

| Before MaaS | After MaaS |
|-------------|------------|
| Duplication of models | Single model instances |
| Duplication of efforts | Expert team serves once |
| Lack of accountability | High traceability |
| Low GPU utilization (0%) | Increased utilization |
| Unnecessarily high costs | Lower TCO / chargeback |

### MaaS Principles
1. Become the provider of Private AI
2. Don't just "throw GPUs at the problem"
3. A team of experts serves each model only once
4. Provide self-service access to the models
5. Use an API gateway to track model consumption
6. Replicate the business structure of public AI providers (OpenAI, Gemini, etc.)
7. Note: "None of them give you access to their GPUs"

### Key Quote
> "With great GPU costs, comes great cost tracking responsibility"

---

## Module Structure

### Files to Create
```
docs/12-maas/
├── README.md                    # Module overview
├── 1-understanding-maas.md      # Why MaaS? Concepts and architecture
├── 2-deploy-litemaas.md         # Deploy LiteMaaS on OpenShift
├── 3-admin-configuration.md     # Admin: users, budgets, models
├── 4-user-experience.md         # User: API keys, model access, usage
├── 5-canopy-integration.md      # Connect Canopy to LiteMaaS
├── images/                      # Screenshots and diagrams
└── initial-plan.md              # This file (for reference)
```

### Sidebar Entry (for docs/_sidebar.md)
```markdown
* [Models as a Service](12-maas/README.md)
  * [🧠 Understanding MaaS](12-maas/1-understanding-maas.md)
  * [🚀 Deploy LiteMaaS](12-maas/2-deploy-litemaas.md)
  * [👩‍💼 Admin Configuration](12-maas/3-admin-configuration.md)
  * [👤 User Experience](12-maas/4-user-experience.md)
  * [🌳 Canopy Integration](12-maas/5-canopy-integration.md)
```

---

## Lesson Plans

### Lesson 1: Understanding MaaS (1-understanding-maas.md)

**Learning Objectives:**
- Understand what MaaS is and why organizations need it
- Learn the challenges of self-service GPU access at enterprise scale
- Recognize the inefficiencies of per-user model deployment
- Explore LiteMaaS architecture and components

**Content Outline:**

1. **The Origin Story - Self-Service GPU Problems**
   - Scenario: Enterprise offers OpenShift AI cluster to all employees
   - What happens: Multiple users deploy the same model (e.g., 7 instances of Granite)
   - Result: GPUs at 0% utilization while "no GPUs available" errors occur
   - Key insight: 19K employees × 1 GPU each = impossible to scale

2. **Ideas That Don't Work**
   - ❌ Increase auto-scaling max (too expensive)
   - ❌ Set OpenShift quotas (doesn't solve duplication)
   - ❌ Use MIG to slice GPUs (slices too small for large models)

3. **The MaaS Solution**
   - ✅ Deploy each model **once**
   - ✅ Put an API gateway in front
   - ✅ Provide self-service access to **models**, not GPUs
   - Visual: Before (7 users → 7 Granite → 7 GPUs) vs After (7 users → 1 Gateway → 1 Granite → 1 GPU)

4. **Before vs After MaaS** (comparison table)

5. **MaaS Principles** (from presentation)

6. **LiteMaaS Architecture**
   - Frontend: React + PatternFly 6
   - Backend: Fastify + PostgreSQL
   - Proxy: LiteLLM integration (OpenAI-compatible API)
   - Auth: OAuth2/JWT with OpenShift integration

**Format:** Conceptual explanation with diagrams. No hands-on exercises (theory lesson).

---

### Lesson 2: Deploy LiteMaaS (2-deploy-litemaas.md)

**Learning Objectives:**
- Deploy LiteMaaS on OpenShift using GitOps
- Configure OAuth authentication
- Connect to LiteLLM for model access

**Content Outline:**

1. **Prerequisites Check**
   - Verify OpenShift access and permissions
   - Confirm models are already deployed (from previous modules)

2. **Clone LiteMaaS Repository**
   - Git clone from https://github.com/rh-aiservices-bu/litemaas

3. **Configure Environment**
   - Database connection (PostgreSQL)
   - OAuth settings (client ID, secret)
   - JWT secret
   - LiteLLM endpoint configuration

4. **Deploy to OpenShift**
   - Apply Kubernetes manifests (`oc apply -k`)
   - Verify pods are running

5. **Access the UI**
   - Navigate to LiteMaaS dashboard
   - Initial admin login and setup

**Hands-on Exercises:**
- Deploy LiteMaaS using `oc apply -k`
- Configure OAuth with OpenShift
- Verify deployment health

---

### Lesson 3: Admin Configuration (3-admin-configuration.md)

**Learning Objectives:**
- Manage users and roles (admin/adminReadonly/user)
- Configure model availability
- Set up budgets and usage limits
- View audit logs and analytics

**Content Outline:**

1. **User Management**
   - View all users
   - Assign roles (admin, adminReadonly, user)
   - OpenShift group integration

2. **Model Management**
   - Sync models from LiteLLM
   - Enable/disable models for users
   - Model pricing configuration

3. **Budget Management**
   - Set user-level budgets
   - Team budgets
   - API key budgets

4. **Analytics Dashboard**
   - System-wide usage metrics
   - Token consumption by model/user
   - Cost tracking

5. **Audit Logs**
   - Review access and changes

**Hands-on Exercises:**
- Create a new user and assign roles
- Configure model availability
- Set budget limits
- Explore the admin analytics dashboard

---

### Lesson 4: User Experience (4-user-experience.md)

**Learning Objectives:**
- Create and manage API keys
- Access models via the API
- Track personal usage and costs
- Use the chatbot playground

**Content Outline:**

1. **Getting Your API Key**
   - Generate a new API key
   - Understand key scopes and permissions
   - Multi-model keys

2. **Using the API** (Self-Service Portal Workflow from presentation)
   - Access the API Gateway Self-Serve Portal
   - Create a new application
   - Select your model
   - Get endpoint URL and API key
   - Test with curl

3. **Chatbot Playground**
   - Test models directly in the UI
   - Compare model responses

4. **Usage Tracking**
   - View personal token consumption
   - Monitor remaining budget
   - Usage history

**Hands-on Exercises:**
- Generate an API key
- Make API calls to different models (curl examples)
- Use the chatbot playground
- Review personal usage dashboard

---

### Lesson 5: Canopy Integration (5-canopy-integration.md)

**Learning Objectives:**
- Configure Canopy to use LiteMaaS as the model backend
- Switch from direct model access to MaaS-managed access
- Verify the integration works end-to-end

**Content Outline:**

1. **Why Integrate?**
   - Centralized model management for applications
   - Usage tracking across applications
   - Consistent access control

2. **Configuration Steps**
   - Update Canopy environment variables
   - Point to LiteMaaS API endpoint
   - Configure API key

3. **Testing the Integration**
   - Use Canopy with MaaS backend
   - Verify requests appear in LiteMaaS usage logs

4. **Production Considerations**
   - API key rotation
   - Budget alerts
   - Multi-application setup

**Hands-on Exercises:**
- Update Canopy configuration
- Test Canopy with LiteMaaS backend
- Verify usage tracking in LiteMaaS dashboard

---

## Implementation Steps

1. Create `docs/12-maas/README.md` - Module overview with learning outcomes
2. Create `docs/12-maas/1-understanding-maas.md` - Theory lesson with presentation narrative
3. Create `docs/12-maas/2-deploy-litemaas.md` - Deployment exercise
4. Create `docs/12-maas/3-admin-configuration.md` - Admin tasks
5. Create `docs/12-maas/4-user-experience.md` - User perspective
6. Create `docs/12-maas/5-canopy-integration.md` - Canopy integration
7. Create `docs/12-maas/images/` directory for screenshots
8. Update `docs/_sidebar.md` to include Module 12

---

## Open Items for Refinement

1. **Screenshots**: Need to capture screenshots once LiteMaaS is deployed
2. **Exact deployment commands**: May need to adjust based on actual k8s manifests in litemaas repo
3. **Model list**: Confirm which models will be pre-deployed for students
4. **Canopy configuration**: Verify exact environment variables needed for integration
5. **GitOps approach**: Consider adding GitOps-based model serving configuration (as emphasized in presentation)

---

## Reference Links

- **LiteMaaS Repo**: https://github.com/rh-aiservices-bu/litemaas
- **MaaS Blog**: models-service-lets-use-ai-not-just-talk-about-it
- **Demo**: red.ht/parasol-ai-studio-arcade
- **Original MaaS Repo** (from presentation): github.com/rh-aiservices-bu/models-aas
- **Parasol Studio Repo**: github.com/rh-aiservices-bu/parasol-ai-studio
