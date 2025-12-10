# Module 12: Models as a Service (MaaS) - Implementation Plan

> This plan merges the original `initial-plan.md` with valuable elements from `other-plan.md` to create a comprehensive, persona-driven module.

## Context & Background

### What is this module?
Module 12 teaches students how to implement Models as a Service (MaaS) - a pattern that transforms GPU/model access from chaotic self-service to a managed, efficient service. Students will deploy and use **LiteMaaS** (https://github.com/rh-aiservices-bu/litemaas).

### Prerequisites
- Students have completed Modules 1-8
- Familiar with: OpenShift, GitOps, RAG, Guardrails, Observability, Agents
- Have working Canopy application from previous modules

---

## Connection to Course Narrative

### The RDU Story Arc
The course is set at **Redwood Digital University (RDU)**, where students build **Canopy** - an educational AI assistant. Throughout the modules, Canopy evolves:

| Module | Canopy Evolution |
|--------|------------------|
| Module 2 | Introduced as a simple Streamlit UI for prompt engineering |
| Module 3 | Deployed via GitOps to dev/test/prod environments |
| Module 5 | Enhanced with RAG for document intelligence |
| Module 6 | Protected with guardrails for academic integrity |
| Module 8 | Extended with agentic capabilities |
| **Module 12** | **Connects to centralized MaaS for efficient model access** |

### Current Technical Pattern (What Students Know)
By Module 8, students deploy models directly:
- **KServe/vLLM** inference services on OpenShift AI
- Direct endpoints like `https://canopy-llm-modelmesh-serving.apps.<CLUSTER_DOMAIN>/...`
- Each team/user can deploy their own model instance
- Uses **Llama Stack** framework for model interactions

### The Natural Evolution (Module 12's Story)
**The narrative hook for Module 12:**
> "Canopy has been a success at RDU! But now the Computer Science department, the Business School, AND the Library all want their own Canopy instances. Each team is deploying Granite models... and the GPUs are running out. Sound familiar?"

This connects to the MaaS origin story - the problem students will solve is exactly what happened at RDU (and at real enterprises like Red Hat).

### How Module 12 Fits
- **Before MaaS**: Each Canopy instance has its own model endpoint (direct deployment)
- **After MaaS**: All Canopy instances share models via LiteMaaS API gateway
- **Student Journey**: From "I deploy my own model" → "I consume models as a service"

This mirrors the real-world transition organizations make as they scale AI adoption.

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

---

## Key Enrichments (from other-plan.md)

| Element | How to Integrate |
|---------|------------------|
| **Persona-based framing** | Add clear role markers throughout lessons |
| **"Hardware Hoarding" label** | Use as a friendly, memorable term in Lesson 1 |
| **Narrative arc** | Strengthen the "problem → solution" story with friendly tone |
| **Separate Observability lesson** | New Lesson 5 for usage tracking and chargeback |
| **"Hello World of AI"** | Use as framing for first API call in User Experience |

---

## Personas

The module introduces 4 personas to help students understand different perspectives:

| Persona | Concerned With | Primary Lessons |
|---------|----------------|-----------------|
| **Owner** | Cost, efficiency, ROI, strategy | 1, 5 |
| **AI Engineer / Infrastructure Admin** | Model deployment, infrastructure | 2 |
| **MaaS Service Admin** | Configuration, user support, monitoring | 3, 5 |
| **User / Consumer** | API access, building applications | 4, 6 |

---

## Module Structure (6 Lessons)

```
docs/12-maas/
├── README.md                    # Module overview with personas intro
├── 1-understanding-maas.md      # Why MaaS? The friendly origin story
├── 2-deploy-litemaas.md         # [AI Engineer] Deploy LiteMaaS
├── 3-admin-configuration.md     # [Service Admin] Configuration
├── 4-user-experience.md         # [Consumer] API keys, usage
├── 5-usage-observability.md     # [Owner/Accountant] Metrics, chargeback (NEW)
├── 6-canopy-integration.md      # Connect Canopy to LiteMaaS
├── images/                      # Screenshots and diagrams
├── plan.md                      # This file
└── archive/
    ├── initial-plan.md          # Original plan (preserved)
    └── other-plan.md            # Alternative plan (preserved)
```

### Sidebar Entry (for docs/_sidebar.md)
```markdown
* [Models as a Service](12-maas/README.md)
  * [🧠 Understanding MaaS](12-maas/1-understanding-maas.md)
  * [🚀 Deploy LiteMaaS](12-maas/2-deploy-litemaas.md)
  * [👩‍💼 Admin Configuration](12-maas/3-admin-configuration.md)
  * [👤 User Experience](12-maas/4-user-experience.md)
  * [📊 Usage & Observability](12-maas/5-usage-observability.md)
  * [🌳 Canopy Integration](12-maas/6-canopy-integration.md)
```

---

## Lesson Details

### README.md - Module Overview

**Content:**
- Opening quote (friendly tone, matching other modules like Grounded AI)
- 🧑‍🍳 Module Intro section explaining the MaaS concept
  - Reference the RDU journey: "Canopy has grown from a simple chatbot to a full-featured AI assistant..."
  - Introduce the scaling challenge: "But what happens when everyone at RDU wants their own Canopy?"
- 🖼️ Big Picture image placeholder
- 🔮 Learning Outcomes
- 👥 **Personas Overview** - Introduce the 4 roles with their concerns
- 🔨 Tools used (LiteMaaS, LiteLLM, PostgreSQL, OAuth)

**Example opening quote style:**
> "Giving everyone a GPU is like giving everyone their own power plant. What if we just... shared the electricity instead?"

**RDU Connection:**
> "At RDU, Canopy started as one team's experiment. Now the whole university wants AI. Time to think like a service provider, not just a developer."

---

### 1-understanding-maas.md - Why MaaS?

**Persona focus:** Owner (understanding the problem)

**Learning Objectives:**
- Understand what MaaS is and why organizations need it
- Learn the challenges of self-service GPU access at enterprise scale
- Recognize the inefficiencies of per-user model deployment
- Explore LiteMaaS architecture and components

**Content Outline:**

1. **The Origin Story - The "Hardware Hoarding" Anti-Pattern** (friendly framing)
   - **Start with RDU scenario** (relatable to students):
     - "Canopy was such a hit that the CS department, Business School, and Library all want their own instances"
     - Each department deploys their own Granite model
     - Result: 3 identical models, 3 GPUs, sitting idle most of the time
   - **Scale to enterprise** (the Red Hat story):
     - Scenario: Enterprise offers OpenShift AI cluster to all 19,000 employees
     - What happens: 7 people deploy their own Granite 3-8B instance
     - Result: 7 GPUs at 0% utilization, "no GPUs available" errors
     - Key insight: 19K employees × 1 GPU each = impossible to scale
   - Persona moment: "This is where the **Owner** says 'wait, what?!'"

2. **Ideas That Don't Work** (with friendly tone)
   - ❌ Increase auto-scaling max (too expensive)
   - ❌ Set OpenShift quotas (doesn't solve duplication)
   - ❌ Use MIG to slice GPUs (slices too small for large models)

3. **The MaaS Solution - The Lightbulb Moment**
   - ✅ Deploy each model **once** (by expert team)
   - ✅ Put an API gateway in front
   - ✅ Provide self-service access to **models**, not GPUs
   - Visual: Before (7 users → 7 Granite → 7 GPUs) vs After (7 users → 1 Gateway → 1 Granite → 1 GPU)

4. **Before vs After MaaS** (comparison table from initial-plan)

5. **MaaS Principles**
   - Become the provider of Private AI
   - "Don't just throw GPUs at the problem"
   - A team of experts serves each model only once
   - Replicate the business structure of public AI providers
   - Key quote: "With great GPU costs comes great cost tracking responsibility"

6. **LiteMaaS Architecture**
   - Frontend: React + PatternFly 6
   - Backend: Fastify + PostgreSQL
   - Proxy: LiteLLM integration (OpenAI-compatible API)
   - Auth: OAuth2/JWT with OpenShift integration

**Format:** Conceptual explanation with diagrams. No hands-on exercises (theory lesson).

---

### 2-deploy-litemaas.md - Deploy LiteMaaS

**Persona focus:** AI Engineer / Infrastructure Admin
- Opening: "In this lesson, you wear the AI Engineer hat"
- Context: You're the expert who deploys models once so everyone benefits

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

### 3-admin-configuration.md - Admin Configuration

**Persona focus:** MaaS Service Admin
- Opening: "Now you're the Service Admin - the friendly face of the MaaS platform"

**Learning Objectives:**
- Manage users and roles (admin/adminReadonly/user)
- Configure model availability
- Set up budgets and usage limits

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

**Hands-on Exercises:**
- Create a new user and assign roles
- Configure model availability
- Set budget limits

**Note:** Analytics/observability content moved to Lesson 5

---

### 4-user-experience.md - User Experience

**Persona focus:** User / Consumer
- Opening: "Time to switch perspectives - you're now a developer who needs AI for your app"

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

2. **The "Hello World" of AI** (framing from other-plan)
   - Access the Self-Service Portal
   - Create a new application
   - Select your model
   - Get endpoint URL and API key
   - Test with curl - your first API call!

3. **Chatbot Playground**
   - Test models directly in the UI
   - Compare model responses

4. **Personal Usage Tracking**
   - View your token consumption
   - Monitor remaining budget
   - Usage history

**Hands-on Exercises:**
- Generate an API key
- Make API calls to different models (curl examples)
- Use the chatbot playground
- Review personal usage dashboard

---

### 5-usage-observability.md - Usage & Observability (NEW)

**Persona focus:** Owner / Accountant
- Opening: "With great GPU costs comes great cost tracking responsibility"
- This is where the business case is validated

**Learning Objectives:**
- View system-wide usage metrics
- Understand token consumption patterns
- Set up cost tracking and chargeback models
- Configure quotas and caps

**Content Outline:**

1. **The Accountant's View**
   - Why observability matters for MaaS
   - Cost visibility enables accountability

2. **System-Wide Metrics**
   - Total requests and tokens
   - Usage by model
   - Usage by user/team
   - Time-series analytics

3. **Cost Tracking & Chargeback**
   - Token pricing models
   - Department/team allocation
   - Generating usage reports
   - Chargeback implementation strategies

4. **Quotas and Caps**
   - Setting usage limits
   - Alert thresholds
   - Preventing cost overruns

5. **Audit Logs**
   - Review access and changes
   - Security and compliance

**Hands-on Exercises:**
- Explore the admin analytics dashboard
- Generate a usage report
- Set up a quota with alert threshold
- Review audit logs

---

### 6-canopy-integration.md - Canopy Integration

**Persona focus:** All personas benefit
- Opening: "Remember your Canopy from Module 3? It's been pointing directly at your model endpoint. Time to upgrade it to use MaaS!"

**Learning Objectives:**
- Configure Canopy to use LiteMaaS as the model backend
- Switch from direct model access to MaaS-managed access
- Verify the integration works end-to-end

**Content Outline:**

1. **The Before/After**
   - **Before (Module 3-8)**: Canopy → Direct vLLM/KServe endpoint
   - **After (Module 12)**: Canopy → LiteMaaS API Gateway → Shared models
   - Diagram showing the transition

2. **Why Integrate?**
   - Centralized model management for applications
   - Usage tracking across applications
   - Consistent access control
   - RDU can now track all Canopy usage across departments!

3. **Configuration Steps**
   - Update Canopy environment variables
   - Change from direct endpoint to LiteMaaS API endpoint
   - Configure API key (generated in Lesson 4)
   - The endpoint format changes from `https://canopy-llm-...` to `https://litemaas.../v1/...`

4. **Testing the Integration**
   - Use Canopy with MaaS backend
   - Verify requests appear in LiteMaaS usage logs
   - "Your Canopy queries now show up in the admin dashboard!"

5. **Production Considerations**
   - API key rotation
   - Budget alerts for applications
   - Multi-application setup (multiple Canopy instances sharing MaaS)

**Hands-on Exercises:**
- Update Canopy configuration to use LiteMaaS
- Test Canopy with MaaS backend
- Verify usage tracking in LiteMaaS dashboard
- Compare the experience: same Canopy, different backend!

---

## Tone Guidelines

Match existing modules (see `docs/5-grounded-ai/README.md` for reference):
- Friendly, conversational
- Use analogies and storytelling
- Light humor where appropriate
- Emojis for section headers (🧑‍🍳, 🔮, 🖼️, 🔨)
- Not alarming - "We're here to learn and have fun!"
- Clear progression from concept to hands-on

---

## Implementation Steps

1. Create `docs/12-maas/archive/` directory -> already done
2. Move `initial-plan.md` and `other-plan.md` to `archive/` -> already done
3. Create `docs/12-maas/README.md` with personas overview
4. Create `docs/12-maas/1-understanding-maas.md` with narrative elements
5. Create `docs/12-maas/2-deploy-litemaas.md` with persona markers
6. Create `docs/12-maas/3-admin-configuration.md` with persona markers
7. Create `docs/12-maas/4-user-experience.md` with "Hello World" framing
8. Create `docs/12-maas/5-usage-observability.md` (NEW - Accountant/Owner focus)
9. Create `docs/12-maas/6-canopy-integration.md`
10. Create `docs/12-maas/images/` directory
11. Update `docs/_sidebar.md` with new structure

---

## Open Items for Later

1. **Screenshots**: Capture screenshots once LiteMaaS is deployed
2. **Exact deployment commands**: Adjust based on actual k8s manifests in litemaas repo
3. **Model list**: Confirm which models will be pre-deployed for students
4. **Canopy configuration**: Verify exact environment variables needed
5. **GitOps approach**: Consider adding GitOps-based model serving configuration

---

## Reference Links

- **LiteMaaS Repo**: https://github.com/rh-aiservices-bu/litemaas
- **MaaS Blog**: models-service-lets-use-ai-not-just-talk-about-it
- **Demo**: red.ht/parasol-ai-studio-arcade
- **Original MaaS Repo** (from presentation): github.com/rh-aiservices-bu/models-aas
- **Parasol Studio Repo**: github.com/rh-aiservices-bu/parasol-ai-studio
