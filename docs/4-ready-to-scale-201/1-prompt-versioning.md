# 🗂️ Prompt Versioning

> *Organizing ideas into repeatable, structured formats.*

You’ve explored how prompt design can dramatically shape model behavior, it’s time to **bring order to your creativity**.

In this module, you’ll learn how to move from one-off prompt experiments to **versioned, auditable, reusable prompt templates**—just like managing code in a Git repository.


### 🎯 Why Prompt Versioning Matter

Think of a good prompt like a well-written function or component. Once you get it right, you want to **reuse it** across different apps and users.

But in GenAI workflows, we face a big challenge: Prompt experiments are often **invisible**, **untracked**, and **not reusable**.

This makes collaboration hard and reproducibility nearly impossible—especially at scale.

That’s where **prompt versioning** and a **prompt registry** concept come in. And we know that Git provides traceability, visibility, auditability so why not using Git as the prompt registry.

By storing prompts in Git, we enable:

* ✅ Version control
* ✅ Collaboration
* ✅ Rollback and traceability

---

## 🧱 Storing a Promt

You’ll standardize your prompts using a simple format that captures:

```yaml
LLAMA_STACK_URL: "http://llama-stack-service:8321"
summarize:
  enabled: true
  model: llama32
  prompt: |
    Give me a good summary of the following text.
```

There are a variety of different strategies here on where to store your prompts and how to load them into the backend.  
In our case, we will store this inside the canopy backend repo as the one who develop the backend likely is the same persona to iterate on the prompts.  
More specifically, we will store them inside our values.yaml file and then load them into a configmap which then gets mounted to our backend pod. This way, we can make sure that when the values.yaml file changes, GitOps will update, and the pod will automatically restart with the latest prompt.

Let's go through what we added to our prompt file:

- **LLAMA_STACK_URL** - This is simply the llamastack we are using for the backend. We wanted it here so we can flexibly change it (test vs prod for example) and so that we can keep track of what was used at any given time.
- **summarize** - This is the name of the feature, we will use this name to know which prompt we should use where in the backend. Anything under this feature can be flexibly customized and read in the backend.
- **enabled** - This simply says if the feature is enabled or disabled. We are grouping prompts under their relevant features here which may not always be what you want to do, but it works well in this scenario.
- **model** - The model name as listed in Llamastack, this is to keep track of what model(s) we use for our prompts as the result may differ drastically from model to model.
- **prompt** - The prompt(s) we are using for our feature. If more are needed we can simply add more (prompt1, prompt2, etc for example, although you probably want to use better names 😄)

---

## 🧪 Hands-On: Version Your Prompts

1. Go to your canopy-be folder in your workbench and update the `values-test.yaml` file to have a new prompt.

2. **Commit & Push**

```bash
cd /opt/app-root/src/canopy-be
git checkout -b add-summarization-prompt
git add canopy-be/chart/templates/values-test.yaml
git commit -m "Add prompt for summarization"
git push origin add-summarization-prompt
```

3. Open a Pull Request and document why you picked this template. This adds **narrative and visibility** to prompt decisions.

TODO: Instructions and image for how to open a PR in gitea.

## Prompt Tracker

We use Git to track our changes and able to tell which prompts and settings are at the moment effective in Canopy, or _were_ at a given time. But going through a Git commit history and figure out such answer can be tedious. For that reason we built and deploy a tracker for you to visualize your changes. 

You can find the link in the Quick Link drop down or simply clicking [here](https://prompt-tracker-ai501.<CLUSTER_DOMAIN>/?git_repo_url=https://gitea-gitea.<CLUSTER_DOMAIN>/<USER_NAME>/<CLUSTER_DOMAIN>). 

TODO: Screenshot


### Testing the Prompt Tracker

To test the prompt tracker, try making a change to your model configuration:

1. Edit your prompt in the `chart/values-test.yaml` file in the `canopy-be` repository. 

2. Let's commit and push the changes:

    ```bash
    cd /opt/app-root/src/canopy-be
    git add .
    git commit -m  "🦊 Test the Prompt Tracker dashboard 🦊"
    git push 
    ```

3. Watch the dashboard update with your new changes or hit `Refresh` if you don't want to wait.

    TODO: add screenshots

The dashboard will automatically detect this change and display it in a new card with the changes, the commit information and author details. 


---

## 🌿 Using the New Prompt

Since we already set up the backend before, every change you make to your prompts will now automatically be used in the backend.

This makes your prompts **dynamic and auditable**, any changes to prompts go through Git.

Go to your Canopy UI and try out your new prompt!