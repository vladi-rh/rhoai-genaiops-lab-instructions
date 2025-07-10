# LLM Fundamentals

## 📚 Contents
- [LLM Fundamentals](#llm-fundamentals)
  - [📚 Contents](#-contents)
  - [🔍 What is a Token?](#-what-is-a-token)
  - [🔮 Are LLMs Fixed or Do They Change?](#-are-llms-fixed-or-do-they-change)
  - [🔄 Next-Token Prediction](#-next-token-prediction)

## 🔍 What is a Token?

Before an AI model can understand or generate text, it breaks everything down into tiny pieces called **tokens**.

A token is not quite a word — it could be:
- A whole short word: `"The"` → 1 token
- Parts of a longer word: `"unbelievable"` → 3 tokens (`"un"`, `"believ"`, `"able"`)
- Punctuation: `","` or `"."` might each be 1 token

These are the basic building blocks the model sees. It doesn’t understand text the way humans do — it just sees a stream of tokens and learns patterns in how they appear.

You may ask "why not just feed it words or letters?"  
There are two main reasons to use tokens:
- Regardless of what we use, we need to convert it into numbers because ultimately the computer only understands numbers 🔢 Aaand, there are too many words to give them all a number each.
- They are designed to be as large but also as reusable as possible, so that the **number** of inputs we send to the LLM is as few as possible. For example, if I send the word `unbelievable` it would be 12 inputs if I sent each letter, but only 3 tokens. The number of inputs are important which we explain... now 👇

When you start working with LLMs you will often see people counting tokens. We don't just do this for fun, it's because the number of tokens is now how large our input into the LLM is.  
An LLM can only input and output a certain number of tokens in the same request/inference (think of it as how much context/information it can see at once).  
Besides that, the more we input the more memory it needs to use (GPU memory specifically) to keep track of all the inputs and outputs (remember that the output turns into input in the next step). 

![input-output.png](images/input-output.png)

Here you can try your hands on how sentences get converted into tokens:
<iframe
	src="https://agents-course-the-tokenizer-playground.static.hf.space"
	frameborder="0"
	width="500"
	height="750"
	style="border: 1px solid #ccc; border-radius: 8px;"
	loading="lazy">
></iframe>

*The App is from [HuggingFace Learning Course](https://agents-course-the-tokenizer-playground.static.hf.space)*

Let’s test your understanding with a quick quiz!

<!-- 🔍 Token‐capacity calculation (typed answer) -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">
  <h3 style="margin:0 0 8px;color:#5a5a5a;">🔤 Quiz</h3>
  <p style="color:#495057; font-weight:500;">
    You’re working on a big codebase (thousands of lines long) and you don't feel like reading through it line-by-line. <br>
    So instead, you decide to get help from your favorite LLM 🤖<br>
    You start off by writing some instructions:

    “Explain what this code does, step by step, in simple terms...”
  <p style="color:#495057; font-weight:500;">
    Which takes 96 tokens in total.<br>
    Then you start feeding it the code, line by line, where each line takes about 12 tokens per line.<br>
    Now, you also happen know that the model only can handle 4096 tokens at the same time.<br>
  </p>
  <p style="color:#495057; font-weight:500;">
    👉 <strong>How many <em>full</em> lines of code can you send the LLM at a time?</strong>
  </p>

  <style>
    /* hide the native number-input arrows */
    #cap-input::-webkit-inner-spin-button,
    #cap-input::-webkit-outer-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }
    #cap-input {
      -moz-appearance: textfield;
    }
    /* your existing valid/invalid styling… */
    #cap-input { margin:6px 0 4px; padding:6px 10px; border:2px solid #e9ecef; border-radius:6px; width:120px; font-size:1em; }
    #cap-input:focus { outline:none; border-color:#6ea8fe; }
    #cap-input:valid { background:#d4edda; border-color:#28a745; color:#155724; }
    #cap-input:invalid:not(:placeholder-shown) { background:#f8d7da; border-color:#dc3545; color:#721c24; }
    .feedback-cap { display:none; margin:4px 0; padding:8px 16px; border-radius:6px; }
    #cap-input:valid + .feedback-cap[data-feedback="correct"],
    #cap-input:invalid:not(:placeholder-shown) + .feedback-cap[data-feedback="wrong"] {
      display:block;
    }
    .feedback-cap[data-feedback="correct"] { background:#d1f2eb; color:#0c5d56; border:1px solid #a3d9cc; }
    .feedback-cap[data-feedback="wrong"]   { background:#fce8e6; color:#58151c; border:1px solid #f5b7b1; }
  </style>

  <input
    id="cap-input"
    type="number"
    placeholder="---"
    min="333"
    max="333"
    step="1"
    required>

  <div class="feedback-cap" data-feedback="correct">✅ Right! 333 lines.</div>
  <div class="feedback-cap" data-feedback="wrong">❌ Nope, that’s not it.</div>
</div>

<script>
  // prevent Up/Down arrows from jumping to 333 when empty
  document.getElementById('cap-input')
    .addEventListener('keydown', function(e) {
      if ((e.key === 'ArrowUp' || e.key === 'ArrowDown') && this.value === '') {
        e.preventDefault();
      }
    });
</script>



## 🔮 Are LLMs Fixed or Do They Change?

Once a large language model is trained, it becomes **frozen** — it doesn’t learn new things by talking to you. Every time you send a message (called a **prompt**), the model uses what it already knows and responds based only on:
- Its original training data
- The content of your current prompt
- Randomness in the generation process

Even if you tell the model something new today, it won’t “remember” it tomorrow unless you remind it again.

So how do systems “remember” facts between conversations?
They use tricks like saving information in a database and re-feeding it into the prompt — not because the model learned it, but because someone re-taught it.

Let’s explore this idea with a quiz!

<!-- 🔮 Frozen-model memory dilemma (harder) -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">

<h3 style="margin:0 0 8px;color:#5a5a5a;">🧠 Quiz</h3>
<p style="color:#495057; font-weight:500;"><strong>Scenario:</strong> Warehouse staff type new SKUs during today’s chat.  
Tomorrow, in a brand-new session, the assistant must recall them instantly.</p>
<p style="color:#495057; font-weight:500;">Pick the <em>most practical</em> way to achieve that.</p>

<style>
.quiz-container-sku{position:relative}
.quiz-option-sku{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;cursor:pointer;transition:.2s;border:2px solid #e9ecef;color:#495057}
.quiz-option-sku:hover{background:#fff;transform:translateY(-1px);border-color:#dee2e6}
.quiz-radio-sku{display:none}
.quiz-radio-sku:checked+.quiz-option-sku[data-correct="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.quiz-radio-sku:checked+.quiz-option-sku:not([data-correct="true"]){background:#f8d7da;color:#721c24;border-color:#f5b7b1}
.feedback-sku{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#sku-correct:checked~.feedback-sku[data-feedback="correct"],
#sku-wrong1:checked~.feedback-sku[data-feedback="wrong"],
#sku-wrong2:checked~.feedback-sku[data-feedback="wrong"],
#sku-wrong3:checked~.feedback-sku[data-feedback="wrong"]{display:block}
.feedback-sku[data-feedback="correct"]{background:#d1f2eb;color:#0c5d56;border:1px solid #a3d9cc}
.feedback-sku[data-feedback="wrong"]{background:#fce8e6;color:#58151c;border:1px solid #f5b7b1}
</style>

<div class="quiz-container-sku">
  <input type="radio" name="quiz-sku" id="sku-wrong1" class="quiz-radio-sku">
  <label for="sku-wrong1" class="quiz-option-sku" data-correct="false">🔖 Append “Remember these forever” to the end of today’s prompt</label>

  <input type="radio" name="quiz-sku" id="sku-wrong2" class="quiz-radio-sku">
  <label for="sku-wrong2" class="quiz-option-sku" data-correct="false">🧹 Increase the context window so <em>today’s</em> chat fits in tomorrow’s prompt untouched</label>

  <input type="radio" name="quiz-sku" id="sku-wrong3" class="quiz-radio-sku">
  <label for="sku-wrong3" class="quiz-option-sku" data-correct="false">🔧 Retrain the model overnight on the new SKUs</label>

  <input type="radio" name="quiz-sku" id="sku-correct" class="quiz-radio-sku">
  <label for="sku-correct" class="quiz-option-sku" data-correct="true">📦 Store the SKUs in a database or and auto-inject them into tomorrow’s prompt (retrieval)</label>

  <div class="feedback-sku" data-feedback="correct">✅ Correct! Frozen weights can’t learn overnight—you must feed yesterday’s SKUs back in (retrieval is fastest and cheapest).</div>
  <div class="feedback-sku" data-feedback="wrong">❌ Prompts alone can’t alter weights, massive context gets expensive, and retraining the model is often overkill (especially if it's needed frequently).</div>
</div>
</div>


---

## 🔄 Next-Token Prediction

At their core, large language models do something surprisingly simple:  
They guess the **next token**.

You give them a string of text, and the model continues it by predicting the most likely next piece. Then it does it again. And again. And again.

It’s like a very fast autocomplete — but one that’s been trained on a massive collection of text from books, websites, conversations, and more.

For example:
> Input: “Photosynthesis is the process by which plants”  
> Model prediction: `“ convert sunlight into energy”`

This step-by-step guessing game is called **inference**.

Because the model is trying to predict what *usually* comes next, it’s sensitive to clues and patterns in your prompt — and sometimes a small change can lead to a very different outcome.

Let’s see how well it guesses in a specific context:

<!-- 🔄 Next token – tricky semantic cue -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">

<h3 style="margin:0 0 8px;color:#5a5a5a;">📝 Quiz</h3>
<p style="color:#495057; font-weight:500;">
<strong>Scenario:</strong> The prompt sent to the model reads exactly like this:
</p>

<p style="color:#495057; font-weight:500;">
"John carefully packed his bag with essentials for the desert hike: water, sunscreen, and a wide-brimmed hat. He double-checked everything twice. When he arrived, the blazing sun made him immediately grateful he'd remembered his..."
</p>

<p style="color:#495057; font-weight:500;">Which <em>single token</em> is the model most likely to produce next?</p>

<style>
.quiz-container-next-tricky{position:relative}
.quiz-option-next-tricky{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;cursor:pointer;transition:.2s;border:2px solid #e9ecef;color:#495057}
.quiz-option-next-tricky:hover{background:#fff;transform:translateY(-1px);border-color:#dee2e6}
.quiz-radio-next-tricky{display:none}
.quiz-radio-next-tricky:checked+.quiz-option-next-tricky[data-correct="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.quiz-radio-next-tricky:checked+.quiz-option-next-tricky:not([data-correct="true"]){background:#f8d7da;color:#721c24;border-color:#f5c6cb}
.feedback-next-tricky{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#next-tricky-correct:checked~.feedback-next-tricky[data-feedback="correct"],
#next-tricky-wrong1:checked~.feedback-next-tricky[data-feedback="wrong"],
#next-tricky-wrong2:checked~.feedback-next-tricky[data-feedback="wrong"],
#next-tricky-wrong3:checked~.feedback-next-tricky[data-feedback="wrong"]{display:block}
.feedback-next-tricky[data-feedback="correct"]{background:#d1f2eb;color:#0c5d56;border:1px solid #a3d9cc}
.feedback-next-tricky[data-feedback="wrong"]{background:#fce8e6;color:#58151c;border:1px solid #f5b7b1}
</style>

<div class="quiz-container-next-tricky">
  <input type="radio" name="quiz-next-tricky" id="next-tricky-wrong1" class="quiz-radio-next-tricky">
  <label for="next-tricky-wrong1" class="quiz-option-next-tricky" data-correct="false">🥤 water</label>

  <input type="radio" name="quiz-next-tricky" id="next-tricky-correct" class="quiz-radio-next-tricky">
  <label for="next-tricky-correct" class="quiz-option-next-tricky" data-correct="true">🎩 hat</label>

  <input type="radio" name="quiz-next-tricky" id="next-tricky-wrong2" class="quiz-radio-next-tricky">
  <label for="next-tricky-wrong2" class="quiz-option-next-tricky" data-correct="false">🧴 sunscreen</label>

  <input type="radio" name="quiz-next-tricky" id="next-tricky-wrong3" class="quiz-radio-next-tricky">
  <label for="next-tricky-wrong3" class="quiz-option-next-tricky" data-correct="false">🕶️ sunglasses</label>

  <div class="feedback-next-tricky" data-feedback="correct">✅ Exactly! Context indicates intense sun ("blazing sun"), making "hat" the strongest logical continuation.</div>
  <div class="feedback-next-tricky" data-feedback="wrong">❌ Read again carefully. What specific clue ("blazing sun") makes a particular item most relevant?<br>If you think your answer is better, that's cause it might be, but the LLM only guesses based on this limited context.</div>
</div>
</div>


