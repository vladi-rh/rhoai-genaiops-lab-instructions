# Trusty AI Guardrails Orchestrator

Trusty AI FMS Guardrails Orchestrator gives you an external policy layer that sits around your models. It coordinates different type of detectors before anything reaches the LLM or response reaches to the user. 

We first need to install Guardrails Orchestator, integrate it with Llama Stack as the safety guardrails layer to route the prompts and responses through detectors.

### Deploy Guardrails Orchestrator

1. Again, let's start deploying it to experiment environment. Go to OpenShift Console > Helm > Releases > Create Helm Release and select `GenAIOps Helm Charts` and find `Guardrails Orchestrator` helm chart.

  ![guardrails-orchestrator-helm.png](guardrails-orchestrator-helm.png)

  You don't have to make any changes, just hit Create!

2. Now, let's integrate it with Llama Stack. For it, you need 