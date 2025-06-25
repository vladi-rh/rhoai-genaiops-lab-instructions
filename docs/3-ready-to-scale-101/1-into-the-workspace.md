---
intro to OpenShift AI and Workbench concept

"this is where we are going to do develop the continuous model evaluation stuff"

intro to GitOps a bit?

intro to repos we have


## 📘 Introduction to Red Hat OpenShift AI

Welcome to the foundation of our adaptive learning platform, Canopy AI! To build smart, scalable AI solutions for students and educators, we use **Red Hat OpenShift AI**—a powerful, enterprise-grade platform for developing, deploying, and managing AI and machine learning workloads on Kubernetes.

### 🧩 What is Red Hat OpenShift AI?

OpenShift AI is Red Hat’s integrated AI/ML platform built on top of **OpenShift Container Platform**. It provides tools and infrastructure to:

* **Build** AI models quickly with preconfigured environments
* **Deploy** models as scalable, secure APIs using Kubernetes-native runtimes
* **Manage** AI workloads with built-in monitoring, autoscaling, and GPU scheduling
* **Collaborate** across teams with shared projects and IDEs

OpenShift AI abstracts away much of the complexity behind running AI workloads at scale so that data scientists, ML engineers, and developers can focus on what matters—building and improving intelligent applications.

### 🔍 What’s Inside Our OpenShift AI Environment?

For this enablement, you will work within a tailored OpenShift AI environment designed for experimentation and learning.

Here’s what you have _for now_:

#### 1️⃣ Data Science Project: `<USER_NAME>-canopy`

* A dedicated **Data Science project (namespace)** scoped just for you
* Acts as your playground to deploy, experiment, and test models for Canopy AI
* Isolated environment to avoid conflicts and enable focused work

#### 2️⃣ Connection for Model Container Images in Quay

* A configured **image pull secret** connecting your project to Red Hat’s Quay registry
* Enables your environment to pull container images that package AI models (like LLMs)
* Ensures seamless model deployment from trusted container sources

#### 3️⃣ Workbench: Your Cloud IDE

* An integrated **web-based development environment** hosted inside OpenShift AI
* Provides tools like terminals, code editors, and notebooks for building and testing AI workflows
* Allows you to write scripts, develop prompt playgrounds, and interact with deployed models without leaving the platform

➡️ **Up Next:**
Now that you’re familiar with OpenShift AI and your environment, let’s dive into **LLM 101**—understanding the models we will use and how to deploy them.
