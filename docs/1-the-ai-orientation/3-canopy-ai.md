# 🌿 What is Canopy AI?

**Canopy AI** is an intelligent, leafy little assistant designed to support teaching and learning at **Redwood Digital University**. From summarizing texts to generating quizzes and scoring assignments — it’s your educational AI lab in action.

This frontend gives you a clean, playful UI built in Streamlit, powered by your choice of LLMs. Whether hosted in OpenShift or running locally, it’s built for experimentation and enablement.

## 🎯 Why This Frontend Matters for Prompt Engineering

Just like a good prompt shapes a great model response, a good UI shapes great exploration.

This Canopy AI interface gives you a starting point to test how prompting changes behavior — and how LLMs can support real educational tasks. It supports:

    System prompts 🧠 to define model behavior.

    User prompts 💬 to define what you ask.

    Live streaming output 🌱 so you see each token bloom.

In future modules, this same interface will evolve to handle content creation, grading, and personalized feedback.

## 🚀 Getting Started with Canopy AI on OpenShift

Follow these instructions to get your own instance of Canopy AI up and running in just a few minutes.

### 📦 1. Deploy the Frontend to OpenShift

Apply the deployment, service, and route with a single command:

```bash
oc apply -k https://github.com/rhoai-genaiops/canopy-ai/tree/main/deployment
```

✅ This will create:

- A UBI9-based Streamlit app
- A service exposing port 8501
- A secure OpenShift route (TLS termination: edge)

Run this to see that the frontend has been deployed:
```bash
oc get po -l app.kubernetes.io/name=canopy-ai -n <USER_NAME>-canopy
```

### ⚙️ 2. Configure Your Environment Variables

Once deployed, go to:
- OpenShift Console
- Workloads -> Deployment -> canopy-ai
- Environment tab

In here you need to modify the `LLM_ENDPOINT` and `SYSTEM_PROMPT` to reflect yours:

![change-env-vars](./images/change-env-vars.png)

### 🧪 3. Try the Summarization UI

Open the route created by OpenShift, e.g.:

https://canopy-ai-<your-project>.<cluster-domain>

Inside the app, you can:

    Paste in any block of text 📄

    Watch the model generate a summary in real-time ✨

    See how different prompts affect the output

📸 Insert screenshot of the running UI with input & output


✅ Your Goal

By the end of this module, you should:

Deploy the Canopy AI frontend on OpenShift

Connect it to your own LLM endpoint

Use the system prompt to shape the assistant's behavior

Understand the relationship between prompting and summarization style