Intro to backend as well?

# 🗂️ Prompt Templates

> *Organizing ideas into repeatable, structured formats.*

<div class="terminal-curl"></div>

Now that you’ve explored how prompt design can dramatically shape model behavior, it’s time to **bring order to your creativity**.

In this module, you’ll learn how to move from one-off prompt experiments to **versioned, auditable, reusable prompt templates**—just like managing code in a Git repository.

### 🎯 Why Prompt Templates Matter

Think of a good prompt like a well-written function or component. Once you get it right, you want to **reuse it** across different apps and users.

But in GenAI workflows, we face a big challenge: Prompt experiments are often **invisible**, **untracked**, and **not reusable**.

This makes collaboration hard and reproducibility nearly impossible—especially at scale.

That’s where **prompt templates** and a **prompt registry** concept come in. And we know that Git provides traceability, visibility, auditability so why not using Git as the prompt registry.

By storing prompts in Git, we enable:

* ✅ Version control
* ✅ Collaboration
* ✅ Rollback and traceability

---

## 🧱 Structure of a Prompt Template

You’ll standardize your prompts using a simple template format that captures:

```yaml
name: canopy-ai
use_case: summarization
model: openai/gpt-4
system_prompt: |
  You are a patient and clear tutor helping students to summarize topics.
example_user_prompt: |
  Explain the difference between supervised and unsupervised learning.
tags: [education, ai-assistant, beginner-friendly]
created_by: <USER_NAME>
```

Each template lives in its own file and folder in the prompt registry, stored in Git.

---

Maybe we ask them to iterate here? like figure out what kind of tags, key / values etc needs to here? and our pipeline can only relky on `name` and `system_prompt` keys? 
and next chapter we do the hands on?

---

## 🧪 Hands-On: Your Prompt Registry

1. **Clone the Prompt Registry Repo**

```bash
git clone https://github.com/rhoai-genaiops/canopy-prompts
cd canopy-prompts/templates
```

2. **Create a New Prompt Template**

You’ll base it on the system prompt that performed best in your last experiment. Create a new file like:

```bash
tutoring-assistant-v1.yaml
```

Fill in the YAML structure above.

3. **Commit & Push**

```bash
git checkout -b add-tutoring-prompt
git add templates/tutoring-assistant-v1.yaml
git commit -m "Add prompt for tutoring assistant"
git push origin add-tutoring-prompt
```

Open a Pull Request and document why you picked this template. This adds **narrative and visibility** to prompt decisions.

---

## 🌿 Deploying with a Prompt Template

Now, update your Canopy AI frontend to **reference this prompt** by name instead of pasting a hardcoded string.

You’ll modify your deployment environment to point to:

```env
SYSTEM_PROMPT_SOURCE=https://raw.githubusercontent.com/rhoai-genaiops/prompt-registry/main/templates/tutoring-assistant-v1.yaml
```

This makes your frontend **dynamic and auditable**—any changes to prompts go through Git, not a hidden textarea.

