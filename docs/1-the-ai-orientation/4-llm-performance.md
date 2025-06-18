# 📊 LLM Performance and Hardware

## 📚 Contents
- [📊 LLM Performance and Hardware](#-llm-performance-and-hardware)
  - [📚 Contents](#-contents)
  - [📊 Key Performance Metrics](#-key-performance-metrics)
  - [📦 Model Sizes and Requirements](#-model-sizes-and-requirements)
  - [✅ Summary](#-summary)

## 📊 Key Performance Metrics

Understanding how your model performs helps you scale and troubleshoot.

| Metric                  | Meaning                                                      |
|-------------------------|--------------------------------------------------------------|
| **TTFT**                | Time to First Token – how fast the model starts responding   |
| **TPOT**                | Time Per Output Token – how fast each new token is generated |
| **Throughput**          | Number of parallel requests handled                          |
| **VRAM Usage**          | GPU memory required (↑ model size or context = ↑ memory)     |

These metrics help you balance latency vs. cost in OpenShift AI deployments.

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">📏 Quiz: What does TTFT measure in LLM inference?</h3>

<style>
.quiz-container-metrics { position: relative; }
.quiz-option-metrics {
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
.quiz-option-metrics:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-metrics { display: none; }
.quiz-radio-metrics:checked + .quiz-option-metrics[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-metrics:checked + .quiz-option-metrics:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-metrics {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#metrics-correct:checked ~ .feedback-metrics[data-feedback="correct"],
#metrics-wrong1:checked ~ .feedback-metrics[data-feedback="wrong"],
#metrics-wrong2:checked ~ .feedback-metrics[data-feedback="wrong"] {
  display: block;
}
.feedback-metrics[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-metrics[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-metrics">
   <input type="radio" name="quiz-metrics" id="metrics-wrong2" class="quiz-radio-metrics">
   <label for="metrics-wrong2" class="quiz-option-metrics" data-correct="false">📊 The number of tokens processed per second during generation</label>

   <input type="radio" name="quiz-metrics" id="metrics-correct" class="quiz-radio-metrics">
   <label for="metrics-correct" class="quiz-option-metrics" data-correct="true">⚡ How long it takes for the model to generate its first response token</label>

   <input type="radio" name="quiz-metrics" id="metrics-wrong1" class="quiz-radio-metrics">
   <label for="metrics-wrong1" class="quiz-option-metrics" data-correct="false">💾 The total amount of VRAM memory consumed during inference</label>

   <div class="feedback-metrics" data-feedback="correct">✅ <strong>Perfect!</strong> TTFT (Time to First Token) measures the initial latency before the model starts responding, which is crucial for user experience.</div>
   <div class="feedback-metrics" data-feedback="wrong">❌ <strong>Not quite!</strong> TTFT specifically measures the time delay before the model produces its first output token.</div>
</div>
</div>

---

## 📦 Model Sizes and Requirements

Model size matters—for performance *and* capability.

| Model Size     | Parameters | GPU Requirement            | Notes                            |
|----------------|------------|-----------------------------|----------------------------------|
| **<3B**         | Small      | 8–12GB VRAM (1 GPU)         | Lightweight and fast             |
| **7B–13B**      | Medium     | ≥24GB VRAM or quantization  | Balanced power vs. cost          |
| **>30B**        | Large      | Multi-GPU or high-end cards | Slower, but more context-aware   |

🧠 Larger models may be smarter, but smaller ones are often faster and easier to deploy.

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">📦 Quiz: What's the trade-off with model sizes?</h3>

<style>
.quiz-container-models { position: relative; }
.quiz-option-models {
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
.quiz-option-models:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-models { display: none; }
.quiz-radio-models:checked + .quiz-option-models[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-models:checked + .quiz-option-models:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-models {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#models-correct:checked ~ .feedback-models[data-feedback="correct"],
#models-wrong1:checked ~ .feedback-models[data-feedback="wrong"],
#models-wrong2:checked ~ .feedback-models[data-feedback="wrong"] {
  display: block;
}
.feedback-models[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-models[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-models">
   <input type="radio" name="quiz-models" id="models-wrong2" class="quiz-radio-models">
   <label for="models-wrong2" class="quiz-option-models" data-correct="false">⚡ Model size doesn't affect hardware requirements</label>

   <input type="radio" name="quiz-models" id="models-correct" class="quiz-radio-models">
   <label for="models-correct" class="quiz-option-models" data-correct="true">⚖️ Larger models may be more capable but require more GPU resources and are slower</label>

   <input type="radio" name="quiz-models" id="models-wrong1" class="quiz-radio-models">
   <label for="models-wrong1" class="quiz-option-models" data-correct="false">📈 Larger models are always better and should be chosen when possible</label>

   <div class="feedback-models" data-feedback="correct">✅ <strong>Great understanding!</strong> Model selection involves balancing capability with resource constraints and performance needs.</div>
   <div class="feedback-models" data-feedback="wrong">❌ <strong>Not quite!</strong> Consider the trade-offs between model capability and deployment requirements.</div>
</div>
</div>

---

## ✅ Summary

| Concept                | Key Idea                                                            |
|------------------------|---------------------------------------------------------------------|
| **Token**              | The basic unit of LLM input/output                                  |
| **Next-token machine** | LLMs predict one token at a time                                    |
| **Attention**          | Helps models focus on relevant words                                |
| **Context length**     | How much the model can "remember"                                   |
| **KV Cache**           | Speeds up generation by caching internal state                      |
| **Prompting**          | Guides model behavior through smart input design                    |
| **Hallucination**      | LLMs can generate plausible but wrong info                          |
| **Guardrails**         | Techniques to constrain model behavior and output                   |
| **TTFT & TPOT**        | Speed metrics for user experience                                   |
| **VRAM & Throughput**  | Resource and scalability metrics                                    |
| **Model size & GPU**   | Match model size to hardware capability and use case                |

[🔝 Back to Contents](#contents)