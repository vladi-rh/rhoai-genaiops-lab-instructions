# 🐙 Argo CD - GitOps Controller 

GitOps is important because it provides a consistent, automated way to manage machine learning workflows and model & app deployments, ensuring that everything is versioned, traceable, and reproducible. By using Git as the single source of truth, teams can easily track changes, manage configurations, and ensure that models and applications are always deployed in the correct state.

To put GitOps into action, we’ll use Argo CD as our GitOps engine.

## Argo CD Applications
Argo CD is one of the most popular GitOps tools. It keeps the state of our OpenShift applications synchronized with our git repos. It is a controller that reconciles what is stored in our git repo (desired state) against what is live in our cluster (actual state). 

In the context of MLOps, we’ll leverage Argo CD to deploy our tools and models in a repeatable and reproducible manner. By storing configuration definitions in Git, Argo CD will automatically apply those definitions, making the deployment process more efficient and consistent. This means we’ll be working with YAML files :)

Let's setup the foundation of our GitOps system and deploy Canopy frontend via Argo CD.
