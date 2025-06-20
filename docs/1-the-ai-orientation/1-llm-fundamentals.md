# LLM Fundamentals

## 📚 Contents
- [LLM Fundamentals](#llm-fundamentals)
  - [📚 Contents](#-contents)
  - [🔍 What is a Token?](#-what-is-a-token)
  - [🔮 Are LLMs Fixed or Do They Change?](#-are-llms-fixed-or-do-they-change)
  - [🔄 Next-Token Prediction](#-next-token-prediction)

## 🔍 What is a Token?

Tokens are the **smallest units of text** an LLM processes. A token might be a word, a piece of a word, or even punctuation.

Examples:
- `"The"` → 1 token
- `"unbelievable"` → 3 tokens (`"un"`, `"believ"`, `"able"`)

LLMs don't read full sentences—they process token sequences. The total number of tokens affects:
- Memory usage
- Inference speed
- Output length

⚠️ **Tip**: More tokens = slower, more expensive inference.

<iframe
	src="https://agents-course-the-tokenizer-playground.static.hf.space"
	frameborder="0"
	width="500"
	height="750"
	style="border: 1px solid #ccc; border-radius: 8px;"
	loading="lazy">
></iframe>

*The App is from [HuggingFace Learning Course](https://agents-course-the-tokenizer-playground.static.hf.space)*

Let's test your understanding with a quiz!

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">🔤 Quiz: How do tokens impact LLM performance?</h3>

<style>
.quiz-container-tokens { position: relative; }
.quiz-option-tokens {
  display: block;
  margin: 4px 0;
  padding: 8px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-tokens:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-tokens { display: none; }
.quiz-radio-tokens:checked + .quiz-option-tokens[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-tokens:checked + .quiz-option-tokens:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-tokens {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#tokens-correct:checked ~ .feedback-tokens[data-feedback="correct"],
#tokens-wrong1:checked ~ .feedback-tokens[data-feedback="wrong"],
#tokens-wrong2:checked ~ .feedback-tokens[data-feedback="wrong"] {
  display: block;
}
.feedback-tokens[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-tokens[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-tokens">
   <input type="radio" name="quiz-tokens" id="tokens-wrong2" class="quiz-radio-tokens">
   <label for="tokens-wrong2" class="quiz-option-tokens" data-correct="false">🔢 Token count doesn't affect processing speed</label>

   <input type="radio" name="quiz-tokens" id="tokens-wrong1" class="quiz-radio-tokens">
   <label for="tokens-wrong1" class="quiz-option-tokens" data-correct="false">🚀 More tokens always improve output quality</label>

   <input type="radio" name="quiz-tokens" id="tokens-correct" class="quiz-radio-tokens">
   <label for="tokens-correct" class="quiz-option-tokens" data-correct="true">⚡ More tokens increase memory usage and slow down inference</label>

   <div class="feedback-tokens" data-feedback="correct">✅ <strong>Perfect!</strong> You understand that tokens directly impact performance and costs.</div>
   <div class="feedback-tokens" data-feedback="wrong">❌ <strong>Not quite!</strong> Remember: more tokens = more memory + slower processing.</div>
</div>

</div>

## 🔮 Are LLMs Fixed or Do They Change?

LLMs are **frozen once trained**—they do **not learn** or update on the fly. Each time you send a prompt, they respond based on **pretrained knowledge** and context in the prompt.

However, outputs may differ due to:
- **Random sampling strategies**
- **Changes in prompts**
- **Different system instructions**

You can't "teach" an LLM new facts mid-conversation unless it's part of the prompt or a fine-tuned model.

So let's do a quiz!

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">🧠 Quiz: Do LLMs learn new information during conversations?</h3>

<style>
.quiz-container-learning { position: relative; }
.quiz-option-learning {
  display: block;
  margin: 4px 0;
  padding: 8px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-learning:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-learning { display: none; }
.quiz-radio-learning:checked + .quiz-option-learning[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-learning:checked + .quiz-option-learning:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-learning {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#learning-correct:checked ~ .feedback-learning[data-feedback="correct"],
#learning-wrong1:checked ~ .feedback-learning[data-feedback="wrong"],
#learning-wrong2:checked ~ .feedback-learning[data-feedback="wrong"] {
  display: block;
}
.feedback-learning[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-learning[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-learning">
   <input type="radio" name="quiz-learning" id="learning-wrong2" class="quiz-radio-learning">
   <label for="learning-wrong2" class="quiz-option-learning" data-correct="false">🔄 They learn gradually but only remember within the same session</label>

   <input type="radio" name="quiz-learning" id="learning-wrong1" class="quiz-radio-learning">
   <label for="learning-wrong1" class="quiz-option-learning" data-correct="false">📚 Yes, they continuously update their knowledge from each conversation</label>

   <input type="radio" name="quiz-learning" id="learning-correct" class="quiz-radio-learning">
   <label for="learning-correct" class="quiz-option-learning" data-correct="true">🔒 No, they are frozen after training and don't learn new information</label>

   <div class="feedback-learning" data-feedback="correct">✅ <strong>Exactly right!</strong> LLMs are fixed after training and only work with their pretrained knowledge plus current context.</div>
   <div class="feedback-learning" data-feedback="wrong">❌ <strong>Think again!</strong> LLMs don't update or learn - they're frozen after training.</div>
</div>

</div>

---

## 🔄 Next-Token Prediction

LLMs are **next-token machines**. At their core, they do one thing:  
👉 Predict the most likely next token based on everything they’ve seen so far.

For example:
> Input: "Photosynthesis is the process by which plants"  
> Prediction: `" convert sunlight into energy"`

This generation happens one token at a time, using **probabilities** and **context** to decide what comes next.

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">📝 Quiz: What does an LLM do during inference?</h3>

<style>
.quiz-container { position: relative; }
.quiz-option {
  display: block;
  margin: 4px 0;
  padding: 8px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio { display: none; }
.quiz-radio:checked + .quiz-option[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio:checked + .quiz-option:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#correct:checked ~ .feedback[data-feedback="correct"],
#wrong1:checked ~ .feedback[data-feedback="wrong"],
#wrong2:checked ~ .feedback[data-feedback="wrong"] {
  display: block;
}
.feedback[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container">
   <input type="radio" name="quiz" id="wrong1" class="quiz-radio">
   <label for="wrong1" class="quiz-option" data-correct="false">📊 Classify the topic of a sentence</label>

   <input type="radio" name="quiz" id="wrong2" class="quiz-radio">
   <label for="wrong2" class="quiz-option" data-correct="false">🗄️ Retrieve facts from a database</label>

   <input type="radio" name="quiz" id="correct" class="quiz-radio">
   <label for="correct" class="quiz-option" data-correct="true">🎯 Predict the most likely next token based on previous ones</label>

   <div class="feedback" data-feedback="correct">✅ <strong>Excellent!</strong> You understand how LLMs work during inference.</div>
   <div class="feedback" data-feedback="wrong">❌ <strong>Try again!</strong> Think about what LLMs fundamentally do during text generation.</div>
</div>

</div>

