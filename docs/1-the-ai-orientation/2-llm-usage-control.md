# 💭 Using and Controlling LLMs

## 📚 Contents
- [💭 Using and Controlling LLMs](#-using-and-controlling-llms)
  - [📚 Contents](#-contents)
  - [💭 Prompting Techniques](#-prompting-techniques)
  - [🚨 Understanding Hallucinations](#-understanding-hallucinations)
    - [How can we reduce hallucinations?](#how-can-we-reduce-hallucinations)
  - [🛡️ Implementing Guardrails](#️-implementing-guardrails)
    - [🔍 Hands-on Exercises - Do LLMs have built in Memory?](#-hands-on-exercises---do-llms-have-built-in-memory)
    - [🔍 Hands-on Exercises - Are LLMs deterministic?](#-hands-on-exercises---are-llms-deterministic)

## 💭 Prompting Techniques

The way you *ask* a model something has a big impact on how it answers. This is called **prompting** — and it’s how we guide the model’s behavior.

There are two key parts to a prompt:
- **System Prompt**: Sets the tone or role for the assistant. Example: `You are a strict grader.`
- **User Prompt**: The actual question or message from the person using the model.

Even small changes in your wording can lead to very different responses.

Prompting well is essential — it helps you get clearer, more helpful, and more accurate answers from the model.

📚 We’ll explore more advanced prompt strategies later. For now, let’s try a fun quiz to see how prompting works in practice:

<!-- 💭 Prompting – what will happen? -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);
            padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">

<h3 style="margin:0 0 8px;color:#5a5a5a;">📝 Quiz</h3>

<p style="color:#495057;font-weight:500;">
<strong>Prompt sent to the model:</strong></p>

<pre style="background:#f8f9fa;border:1px solid #ccc;border-radius:6px;padding:10px;font-size:.9em;color:#495057;font-weight:500;">
{"role":"system",
 "content":"You are a strict grader. Respond with only the single word PASS or FAIL."}

{"role":"user",
 "content":"Explain IN DETAIL how you would grade this homework."}
</pre>

<p style="color:#495057;font-weight:500;">
The model has no temperature tricks and uses default sampling.<br>
<strong>What output is the model most likely to produce?</strong></p>

<style>
.quiz-container-prompt-out{position:relative}
.quiz-option-prompt-out{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;
  cursor:pointer;transition:.2s;border:2px solid #e9ecef;color:#495057}
.quiz-option-prompt-out:hover{background:#fff;transform:translateY(-1px);border-color:#dee2e6}
.quiz-radio-prompt-out{display:none}
.quiz-radio-prompt-out:checked+.quiz-option-prompt-out[data-correct="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.quiz-radio-prompt-out:checked+.quiz-option-prompt-out:not([data-correct="true"]){background:#f8d7da;color:#721c24;border-color:#f5b7b1}
.feedback-prompt-out{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#prompt-out-correct:checked~.feedback-prompt-out[data-feedback="correct"],
#prompt-out-wrong1:checked~.feedback-prompt-out[data-feedback="wrong"],
#prompt-out-wrong2:checked~.feedback-prompt-out[data-feedback="wrong"]{display:block}
.feedback-prompt-out[data-feedback="correct"]{background:#d1f2eb;color:#0c5d56;border:1px solid #a3d9cc}
.feedback-prompt-out[data-feedback="wrong"]{background:#fce8e6;color:#58151c;border:1px solid #f5b7b1}
</style>

<div class="quiz-container-prompt-out">
  <input type="radio" name="quiz-prompt-out" id="prompt-out-wrong1" class="quiz-radio-prompt-out">
  <label for="prompt-out-wrong1" class="quiz-option-prompt-out" data-correct="false">
    📝 A multi-paragraph explanation
  </label>

  <input type="radio" name="quiz-prompt-out" id="prompt-out-correct" class="quiz-radio-prompt-out">
  <label for="prompt-out-correct" class="quiz-option-prompt-out" data-correct="true">
    ✔️ Just one word: <code>PASS</code> <em>or</em> <code>FAIL</code>
  </label>

  <input type="radio" name="quiz-prompt-out" id="prompt-out-wrong2" class="quiz-radio-prompt-out">
  <label for="prompt-out-wrong2" class="quiz-option-prompt-out" data-correct="false">
    🚫 A refusal message
  </label>

  <div class="feedback-prompt-out" data-feedback="correct">
    ✅ <strong>Exactly.</strong> The system instruction outranks the user request, so the model sticks to the one-word format.
  </div>
  <div class="feedback-prompt-out" data-feedback="wrong">
    ❌ Remember: system-role text sets the policy the model follows.
  </div>
</div>
</div>



---

## 🚨 Understanding Hallucinations

Sometimes, language models **make things up** — they sound confident but give you answers that are false or even fictional. This is called a **hallucination**.

Why does it happen?
- The model isn’t checking facts — it’s just guessing the next most likely token.
- It doesn’t know what’s real. It only knows what *sounded* common in its training data.

👻 You might ask for a real citation, and it could invent a document that looks good but doesn’t exist.

### How can we reduce hallucinations?
- Give the model real, accurate facts inside the prompt.
- Add guardrails to catch false claims before they reach users. (see below)
- Use tools that add “retrieval” — like pulling info from a trusted database or website.

Let’s explore this with a quick quiz:

<!-- 🚨 Hallucination – realistic prevention options -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">
  <h3 style="margin:0 0 8px;color:#5a5a5a;">🚨 Quiz</h3>
  <p style="color:#495057;font-weight:500;">
    <strong>Scenario:</strong> A teacher asks, “Give me a NASA citation for the tallest mountain on Mars.”<br>
    The model replies with a non-existent 2023 NASA white paper.
  </p>

  <p style="color:#495057;font-weight:500;">
    You're an engineer who needs to prevent this kind of hallucination. Which solution below would be most effective?
  </p>

  <style>
  .hall-fix-row{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;
                border:2px solid #e9ecef;color:#495057;cursor:pointer;transition:.2s}
  .hall-fix-row:hover{background:#fff;transform:translateY(-1px);border-color:#dee2e6}
  .hall-fix-radio{display:none}
  .hall-fix-radio:checked + .hall-fix-row[data-good="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
  .hall-fix-radio:checked + .hall-fix-row[data-good="false"]{background:#f8d7da;color:#721c24;border-color:#f5b7b1}
  .hall-fix-feedback{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
  #hall-fix-correct:checked ~ .hall-fix-feedback[data-type="good"],
  #hall-fix-w1:checked     ~ .hall-fix-feedback[data-type="bad"],
  #hall-fix-w2:checked     ~ .hall-fix-feedback[data-type="bad"]{display:block}
  .hall-fix-feedback[data-type="good"]{background:#d1f2eb;color:#0c5d56;border:1px solid #a3d9cc}
  .hall-fix-feedback[data-type="bad"]{background:#fce8e6;color:#58151c;border:1px solid #f5b7b1}
  </style>

  <div class="quiz-container-prompt-out">
  <input type="radio" id="hall-fix-w1" name="hall-fix" class="hall-fix-radio">
  <label for="hall-fix-w1" class="hall-fix-row" data-good="false">
    🚧 Fine-tune the model overnight.
  </label>

  <input type="radio" id="hall-fix-correct" name="hall-fix" class="hall-fix-radio">
  <label for="hall-fix-correct" class="hall-fix-row" data-good="true">
    📝 Rewrite the prompt to include <b>correct info + real URL</b><br>
    e.g. “According to NASA, <em>Olympus Mons</em> is tallest. Cite that source.”
  </label>

  <input type="radio" id="hall-fix-w2" name="hall-fix" class="hall-fix-radio">
  <label for="hall-fix-w2" class="hall-fix-row" data-good="false">
    📢 Add “Don’t hallucinate!” as the first sentence of the prompt.
  </label>

  <div class="hall-fix-feedback" data-type="good">
    ✅ Correct – giving the model the <em>true fact and real link</em> steers its next-token guesses toward reality. This is called "grounding" the model.
  </div>
  <div class="hall-fix-feedback" data-type="bad">
    ❌ Not ideal. Consider a solution that explicitly provides verified facts directly into the prompt to eliminate fabrications. Warnings alone won’t supply missing facts.
  </div>
</div>
</div>

---

## 🛡️ Implementing Guardrails

What if you need to make sure the model:
- Doesn’t say harmful things?
- Stays focused on its task?
- Never shares private or medical advice?

That’s where **guardrails** come in.

Guardrails are extra rules or checks we put around the model’s behavior, such as:
- Templates that tell it exactly how to answer
- Filters that block unsafe content
- External systems that fact-check what the model says

They’re important in real-world systems like Canopy — especially in schools, healthcare, and public-facing apps.

Here’s a quiz that explores when to use guardrails and when to be more flexible:


<!-- 🛡️ Guardrails – architectural quiz -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);
            padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">

  <h3 style="margin:0 0 10px;color:#5a5a5a;">🛡️ Quiz</h3>

  <p style="color:#495057;font-weight:500;">
    <strong>When do guardrails pay off?</strong><br>
    For each scenario, choose whether adding standard safety guardrails is the better architectural choice.
    Consider abuse-risk, latency budget, and false-positive cost.
  </p>

  <style>
    .gtbl{border-collapse:collapse;width:100%;font-size:.94em;color:#495057}
    .gtbl th,.gtbl td{border:1px solid #d1e7dd;padding:10px}
    .gtbl th{background:#eef5ff;text-align:center}
    .grad{display:none}

    /* initial neutral cell */
    .gopt{display:block;height:32px;line-height:30px;border-radius:6px;
          background:#f8f9fa;border:2px solid #e9ecef;cursor:pointer}

    .gopt:hover{background:#fff;border-color:#dee2e6}

    /* right pick */
    .grad:checked + .gopt[data-good="yes"]{
      background:#d4edda;border-color:#c3e6cb;color:#155724}
    .grad:checked + .gopt[data-good="yes"]::after{content:"✓";font-weight:600}

    /* wrong pick + explanation */
    .grad:checked + .gopt[data-good="no"]{
      background:#f8d7da;border-color:#f5b7b1;color:#721c24}
    .grad:checked + .gopt[data-good="no"]::after{
      content:"✗  → " attr(data-msg);
      font-weight:600;
      margin-left:6px}
  </style>

  <table class="gtbl">
    <tr>
      <th style="width:45%">Scenario</th>
      <th>Guardrails<br><small>(YES)</small></th>
      <th>Guardrails<br><small>(NO)</small></th>
    </tr>

  <!-- 1 Public bot -->
  <tr>
    <td>🌐 <b>Public Q&amp;A Bot</b></td>

  <td align="center">
    <input type="radio" id="r1y" name="r1" class="grad">
    <label for="r1y" class="gopt" data-good="yes"></label>
  </td>

  <td align="center">
    <input type="radio" id="r1n" name="r1" class="grad">
    <label for="r1n" class="gopt" data-good="no"
            data-msg="Unsafe without filters"></label>
  </td>
  </tr>

  <!-- 2 Latency-critical internal -->
  <tr>
    <td>⚡ <b>Internal Alert Router</b></td>

  <td align="center">
    <input type="radio" id="r2y" name="r2" class="grad">
    <label for="r2y" class="gopt" data-good="no"
            data-msg="Adds avoidable delay"></label>
  </td>

  <td align="center">
    <input type="radio" id="r2n" name="r2" class="grad">
    <label for="r2n" class="gopt" data-good="yes"></label>
  </td>
  </tr>

  <!-- 3 Medical assistant -->
  <tr>
    <td>🏥 <b>Health-Advice Assistant</b></td>

  <td align="center">
    <input type="radio" id="r3y" name="r3" class="grad">
    <label for="r3y" class="gopt" data-good="yes"></label>
  </td>

  <td align="center">
    <input type="radio" id="r3n" name="r3" class="grad">
    <label for="r3n" class="gopt" data-good="no"
            data-msg="Risk of harmful advice"></label>
  </td>
  </tr>

  <!-- 4 Dev code helper -->
  <tr>
    <td>💻 <b>Dev-only Code Helper</b></td>

  <td align="center">
    <input type="radio" id="r4y" name="r4" class="grad">
    <label for="r4y" class="gopt" data-good="no"
            data-msg="Blocks harmless snippets"></label>
  </td>

  <td align="center">
    <input type="radio" id="r4n" name="r4" class="grad">
    <label for="r4n" class="gopt" data-good="yes"></label>
  </td>
  </tr>
  </table>

  <p style="margin-top:8px;font-size:.9em;color:#495057;">
    Green ✓ marks the architecturally sound choice; red ✗ explains why the alternative is sub-optimal.
  </p>
</div>



### 🔍 Hands-on Exercises - Do LLMs have built in Memory?

Try sending this question to the model:  

```bash
What did you learn today?
```

Then follow up with:  

```bash
What did I say in the last message?
```

What did the model respond with?


<div class="iframe-scroll-container">
  <iframe 
    src="https://gradio-app-ai501.<CLUSTER_DOMAIN>/chat-interface"  
    width="600px" 
    height="800px" 
    frameborder="0"
    style="border: 1px solid transparent; border-radius: 1px;">
  </iframe>
</div>

Now try the same thing in **Canopy** and compare. Does it remember what you said? What makes it different?


### 🔍 Hands-on Exercises - Are LLMs deterministic?

Now ask the model something simple like:  

```bash
How can I brew Turkish tea? ☕️🫖
```

Take note of the response. Then ask the **exact same question again**.

Did you get the same answer, or something different?

<div class="iframe-scroll-container">
  <iframe 
    src="https://gradio-app-ai501.<CLUSTER_DOMAIN>/chat-interface"  
    width="600px" 
    height="800px" 
    frameborder="0"
    style="border: 1px solid transparent; border-radius: 1px;">
  </iframe>
</div>

LLMs often use a bit of randomness when generating answers. This randomness is controlled by something called **temperature**:
- **Low temperature (e.g., 0.1)** → more predictable, repeatable responses
- **High temperature (e.g., 0.9)** → more variety and creativity

Try adjusting the temperature and see how it changes the behavior.


[🔝 Back to Contents](#contents)
