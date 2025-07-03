# 📘 Interacting with Llama Stack via Workbench

Now that we’ve deployed the Llama Stack and verified it’s up and running, it’s time to get hands-on.

In this section, we’ll launch a Workbench on Red Hat OpenShift AI to spin up a Code Server environment. This gives us a powerful, browser-based IDE where we can run Python notebooks and start interacting with the Llama Stack programmatically.

You’ll use this environment to:

- Explore Llama Stack’s API
- Send test prompts directly from a notebook
- Understand how the backend handles requests from your frontend

By the end of this section, you'll have a better grasp of how to integrate Llama Stack into your own workflows and applications — and set the stage for more advanced use cases.

1. Login to OpenShift AI. The link and the credentials will be provided by your instructor. You’ll see `<USER_NAME>-canopy` project there. 

2. Let's create a workbench! A workbench is your integrated web-based development environment hosted inside OpenShift AI. Click on the `<USER_NAME>-canopy` project, then click `Create a Workbench`. OpenShift AI Dashboard is pretty intuitive, isn't it? :)

   Select a name you want, could be something like `<USER_NAME>-canopy` 🌳

    **Notebook Image:** 

    - Image selection: `code-server`
    - Version selection: `2025.1`
  
    **Deployment size**
    - Container size: `Small`

    **Environment variables**
    - No need to add one at the moment.

    **Cluster storage**
    - Leave it as max 20 GiB.

    **Connections**
    - Leave it as it is. We don't need any connection definition at the moment.

    And finally, hit `Create workbench`.

When it is in running state, Open it and use your credentials to access it.

  If you're prompted to confirm whether you trust the authors, go ahead and select 'Yes' :) After all, we know you trust us… right? 💚

4. Open a new terminal by hitting the hamburger menu on top left then select `Terminal` > `New Terminal` from the menu.

5. Let's clone our Canopy repository that has some Notebooks in it and learn more about Llama Stack!
<!-- 

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

 -->
