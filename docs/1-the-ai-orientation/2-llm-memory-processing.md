# 🧠 Memory and Processing in LLMs

## 📚 Contents
- [🧠 Memory and Processing in LLMs](#-memory-and-processing-in-llms)
  - [📚 Contents](#-contents)
  - [👀 Attention Mechanism](#-attention-mechanism)
  - [🧠 Context Length and Window](#-context-length-and-window)
  - [⚡ KV Cache and Performance](#-kv-cache-and-performance)

## 👀 Attention Mechanism

**Attention** helps the model focus on the most relevant tokens in the input when generating output.

In the sentence:
> "When the student finished the exam, they felt relieved."

To predict "they", the model uses attention to relate it back to "the student".

Attention is why LLMs feel smart — it allows them to **track meaning and reference across long inputs**.

<img src="https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/AttentionSceneFinal.gif" alt="Visual Gif of Attention" width="60%">

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">👀 Quiz: What does attention help LLMs do?</h3>

<style>
.quiz-container-attention { position: relative; }
.quiz-option-attention {
  display: block;
  margin: 8px 0;
  padding: 12px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-attention:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-attention { display: none; }
.quiz-radio-attention:checked + .quiz-option-attention { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-attention[value="wrong"]:checked + .quiz-option-attention { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-attention {
  margin-top: 15px;
  padding: 12px;
  border-radius: 6px;
  opacity: 0;
  transition: opacity 0.3s ease;
}
#attention-correct:checked ~ .feedback-attention.success { opacity: 1; }
#attention-wrong1:checked ~ .feedback-attention.error, #attention-wrong2:checked ~ .feedback-attention.error { opacity: 1; }
.feedback-attention.success { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-attention.error { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-attention">
  <input type="radio" name="quiz-attention" id="attention-wrong1" class="quiz-radio-attention" value="wrong">
  <label for="attention-wrong1" class="quiz-option-attention">🎯 Focus only on the most recent tokens in the sequence</label>

  <input type="radio" name="quiz-attention" id="attention-correct" class="quiz-radio-attention" value="correct">
  <label for="attention-correct" class="quiz-option-attention" data-correct="true">🔗 Focus on relevant tokens throughout the input to understand relationships</label>
  
  <input type="radio" name="quiz-attention" id="attention-wrong2" class="quiz-radio-attention" value="wrong">
  <label for="attention-wrong2" class="quiz-option-attention">📊 Calculate mathematical operations between tokens</label>

  <div class="feedback-attention success">✅ <strong>Great job!</strong> Attention helps models understand which parts of the input are most relevant for generating each output token.</div>
  <div class="feedback-attention error">❌ <strong>Try again!</strong> Think about how attention helps models understand relationships across the entire input.</div>
</div>
</div>

---

## 🧠 Context Length and Window

The **context window** is how many tokens the model can "remember" at once.

Typical ranges:
- Small models: 2K–4K tokens
- Modern models: 8K–128K+ tokens
- Cutting-edge models: up to 1 million tokens (e.g., Qwen2.5-1M)

More context = better understanding of long documents or prior messages.
But it comes at a cost:
- Slower performance
- More VRAM usage
- Higher latency

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">🧠 Quiz: What happens with larger context windows?</h3>

<style>
.quiz-container-context { position: relative; }
.quiz-option-context {
  display: block;
  margin: 8px 0;
  padding: 12px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-context:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-context { display: none; }
.quiz-radio-context:checked + .quiz-option-context { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-context[value="wrong"]:checked + .quiz-option-context { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-context {
  margin-top: 15px;
  padding: 12px;
  border-radius: 6px;
  opacity: 0;
  transition: opacity 0.3s ease;
}
#context-correct:checked ~ .feedback-context.success { opacity: 1; }
#context-wrong1:checked ~ .feedback-context.error, #context-wrong2:checked ~ .feedback-context.error { opacity: 1; }
.feedback-context.success { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-context.error { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-context">
  <input type="radio" name="quiz-context" id="context-wrong1" class="quiz-radio-context" value="wrong">
  <label for="context-wrong1" class="quiz-option-context">🚀 Models run faster and use less memory</label>

  <input type="radio" name="quiz-context" id="context-wrong2" class="quiz-radio-context" value="wrong">
  <label for="context-wrong2" class="quiz-option-context">📈 Only output quality improves with no downsides</label>
  
  <input type="radio" name="quiz-context" id="context-correct" class="quiz-radio-context" value="correct">
  <label for="context-correct" class="quiz-option-context" data-correct="true">⚡ Better understanding but slower performance and higher VRAM usage</label>

  <div class="feedback-context success">✅ <strong>Spot on!</strong> Larger context windows provide better understanding but come with performance and resource trade-offs.</div>
  <div class="feedback-context error">❌ <strong>Not quite!</strong> Remember: larger context = better understanding but more resources needed.</div>
</div>
</div>

---

## ⚡ KV Cache and Performance

As models generate tokens, they keep track of past computations using a **KV (Key-Value) Cache**.

Instead of recomputing attention for every previous token at each step, the model stores the intermediate results (keys and values) from earlier layers and reuses them as it continues generating.

![KV Cache Autoregression Diagram](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/kv-cache/autoregression.png)

Benefits:
- Avoids repeating expensive calculations
- Greatly improves decode speed
- Reduces latency for long responses
- Enables responsive UIs like Canopy AI's streaming assistant

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">⚡ Quiz: What is the main benefit of KV Cache?</h3>

<style>
.quiz-container-kvcache { position: relative; }
.quiz-option-kvcache {
  display: block;
  margin: 8px 0;
  padding: 12px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-kvcache:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-kvcache { display: none; }
.quiz-radio-kvcache:checked + .quiz-option-kvcache { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-kvcache[value="wrong"]:checked + .quiz-option-kvcache { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-kvcache {
  margin-top: 15px;
  padding: 12px;
  border-radius: 6px;
  opacity: 0;
  transition: opacity 0.3s ease;
}
#kvcache-correct:checked ~ .feedback-kvcache.success { opacity: 1; }
#kvcache-wrong1:checked ~ .feedback-kvcache.error, #kvcache-wrong2:checked ~ .feedback-kvcache.error { opacity: 1; }
.feedback-kvcache.success { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-kvcache.error { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-kvcache">
  <input type="radio" name="quiz-kvcache" id="kvcache-wrong1" class="quiz-radio-kvcache" value="wrong">
  <label for="kvcache-wrong1" class="quiz-option-kvcache">📊 It improves the quality of generated text</label>

  <input type="radio" name="quiz-kvcache" id="kvcache-wrong2" class="quiz-radio-kvcache" value="wrong">
  <label for="kvcache-wrong2" class="quiz-option-kvcache">🧠 It increases the model's context window capacity</label>
  
  <input type="radio" name="quiz-kvcache" id="kvcache-correct" class="quiz-radio-kvcache" value="correct">
  <label for="kvcache-correct" class="quiz-option-kvcache" data-correct="true">🚀 It avoids recomputing attention for previous tokens, speeding up generation</label>

  <div class="feedback-kvcache success">✅ <strong>Perfect!</strong> KV Cache stores previous computations to avoid redundant calculations during token generation.</div>
  <div class="feedback-kvcache error">❌ <strong>Think again!</strong> KV Cache is about performance optimization, not content quality or capacity.</div>
</div>
</div>

[🔝 Back to Contents](#contents)