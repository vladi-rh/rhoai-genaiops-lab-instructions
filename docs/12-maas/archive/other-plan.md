Based on the provided presentation and the structure of the existing modules you shared, here is a comprehensive curriculum plan for your **"Models as a Service" (MaaS)** module.

This plan adopts the structure of the example labs (Introduction -> Architecture -> Hands-on -> Conclusion) and utilizes the narrative arc from your source material to explain the "Why" before moving to the "How" with `litemaas`.

---

# Module: Implementing Models-as-a-Service (MaaS)

## 1. Module Overview & Learning Objectives
**Goal:** Transform the student from a user of raw GPU infrastructure into a provider of "Private AI" services.

**Objectives:**
* [cite_start]Understand the resource and cost inefficiencies of the "One GPU per Developer" model[cite: 51, 88].
* [cite_start]Learn the architectural principles of MaaS: Centralized serving, API Gateways, and GitOps [cite: 106-110].
* **Lab:** Deploy the `litemaas` stack on OpenShift AI.
* [cite_start]**Lab:** Act as a "Consumer" to generate API keys and consume models via code[cite: 123].
* [cite_start]**Lab:** Act as an "Admin" to view usage metrics and quotas[cite: 165].

---

## 2. The Problem: The "Hardware Hoarding" Anti-Pattern
*Concept: Setting the stage using the "Origin Story" from the presentation.*

* **The Scenario:** You have a cluster with GPUs. You give developers direct access to deploy their own models.
* [cite_start]**The Bottleneck:** Even with 19,000 employees, you cannot afford 1 GPU per person[cite: 50, 51].
* **The Inefficiency:**
    * [cite_start]**Duplication:** 7 people deploy the same "Granite" model, consuming 7 GPUs[cite: 44].
    * [cite_start]**Idleness:** Those models sit idle when the developers aren't actively querying them[cite: 44].
    * [cite_start]**No Governance:** You lose track of who is using what resource[cite: 91].


---

## 3. The Solution: The MaaS Architecture
*Concept: Moving from "Infrastructure Provider" to "Service Provider."*

* [cite_start]**The Philosophy:** Replicate the business structure of public AI providers (like OpenAI or Anthropic) internally[cite: 113]. [cite_start]Users don't get GPUs; they get API endpoints[cite: 114].
* **Core Components:**
    1.  [cite_start]**Model Serving:** A team of experts deploys the model *once* (e.g., vLLM serving Granite)[cite: 68, 108].
    2.  [cite_start]**API Gateway:** Sits in front of the models to handle authentication and traffic[cite: 69, 110].
    3.  [cite_start]**Self-Service Portal:** Allows users to generate their own access tokens[cite: 98, 124].


* **Benefits:**
    * [cite_start]**High Traceability:** You know exactly who is using the model[cite: 100].
    * [cite_start]**Increased Utilization:** One GPU serves multiple users via the API[cite: 103].
    * [cite_start]**Cost Control:** Reduce TCO by eliminating idle personal deployments[cite: 102].

---

## 4. Lab Instructions

### Phase 1: The Provider Persona (Deploying MaaS)
*In this section, the student sets up the `litemaas` project.*

1.  **Prerequisites:** Access to an OpenShift cluster with OpenShift AI installed and at least 1 GPU node available.
2.  **GitOps Setup:**
    * Clone the `litemaas` repository.
    * Explain the folder structure: separating the *infrastructure* (Gateway) from the *models* (InferenceServices).
    * [cite_start]*Teaching Point:* We manage models via GitOps to ensure centralized and reliable configuration[cite: 164, 167].
3.  **Deploy the Stack:**
    * Run the installation script/OC commands to deploy the API Gateway and the Model Serving runtime.
    * Verify the pods are running in the `maas-system` namespace.

### Phase 2: The Consumer Persona (Consuming AI)
*In this section, the student acts as a developer needing AI for an app.*

1.  **Access the Portal:**
    * [cite_start]Navigate to the deployed MaaS dashboard URL[cite: 124].
    * 2.  **Create Credentials:**
    * [cite_start]Create a new Application (e.g., "My GenAI App")[cite: 126].
    * [cite_start]Select the desired model (e.g., Granite-3.1-8b-Instruct)[cite: 128].
    * [cite_start]Generate an API Key[cite: 130].
3.  **Integration (The "Hello World" of AI):**
    * [cite_start]Copy the `curl` command provided by the portal[cite: 135].
    * Execute the command in the terminal to receive an inference response.
    * *Observation:* Note how the interaction mimics using a public SaaS API, hiding the infrastructure complexity.

### Phase 3: The Accountant Persona (Observability)
*In this section, the student acts as the platform owner tracking usage.*

1.  **Traffic Analysis:**
    * Return to the MaaS admin view.
    * [cite_start]Navigate to the **Statistics/Graphs** section[cite: 138].
2.  **Analyze Metrics:**
    * [cite_start]Identify the "Hits over last 24H" and "Total Tokens" consumed by the application created in Phase 2[cite: 182, 184].
    * 3.  **Governance discussion:**
    * [cite_start]Discuss how this data facilitates chargeback models[cite: 166].
    * [cite_start]Demonstrate (optional) how to set a "Cap" or quota on usage to prevent cost overruns[cite: 193].

---

## 5. Summary & Next Steps

* **Recap:** We moved from a chaotic "free-for-all" where everyone hoarded GPUs to a streamlined service where models are shared resources.
* **Key Takeaway:** "Don't just throw GPUs at the problem." [cite_start]Be the provider of Private AI[cite: 106, 107].
* [cite_start]**Extension:** In a production scenario, you would use this architecture to deploy quantized models to further reduce memory footprint and costs[cite: 163].

---

### Suggested Visual Aids for the Course Material:
Based on your deck, I recommend extracting these specific slides to use as static diagrams within the lab instructions:
1.  **The "Before" Architecture:** Slide 37/44 (The messy GPU allocation).
2.  **The "After" Architecture:** Slide 81 or 170 (The API Gateway + Model flow).
3.  **The Workflow:** Slide 127 (The "Select Service" UI) and Slide 139 (The Usage Graph).