# 📊 LLM Performance and Hardware

## 📚 Contents
- [📊 LLM Performance and Hardware](#-llm-performance-and-hardware)
  - [📚 Contents](#-contents)
  - [📊 Key Performance Metrics](#-key-performance-metrics)
  - [📦 Model Sizes and Requirements](#-model-sizes-and-requirements)
  - [✅ Summary](#-summary)

## 📊 Key Performance Metrics

Before we jump into hardware and sizes, it's helpful to understand how we measure a model's responsiveness and efficiency. These key metrics help us see how fast a model can start talking, how quickly it produces each word, and how much resource it uses.

| Metric                  | Meaning                                                      |
|-------------------------|--------------------------------------------------------------|
| **TTFT**                | Time to First Token – how quickly the model starts giving its first token after you ask something. |
| **TPOT**                | Time Per Output Token – the speed at which each next token is generated once the response has started. |
| **Throughput**          | How many requests the system can handle at the same time without slowing down. |
| **VRAM Usage**          | The amount of GPU memory the model needs (bigger models or longer conversations need more memory). |

These metrics help you balance latency vs. cost in OpenShift AI deployments.

<!-- 📏 Latency root-cause quiz -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);
            padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">

<h3 style="margin:0 0 8px;color:#5a5a5a;">📏 Quiz</h3>

<p style="color:#495057;font-weight:500;">
Your demo streams an LLM answer and then appends a <b>~900 KB</b> PNG chart
at the very end.<br>
Telemetry shows:
</p>

<ul style="margin-left:1.2em;color:#5a5a5a;">
  <li>~4 s TTFT</li>
  <li>~30 ms TPOT</li>
  <li>PNG transfer time is ~3 s</li>
</ul>

<p style="color:#495057;font-weight:500;">
Which single change will <b>most directly</b> improve what users feel?
</p>

<style>
.latOpt{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;cursor:pointer;
       border:2px solid #e9ecef;color:#495057;transition:.2s}
.latOpt:hover{background:#fff;transform:translateY(-1px);border-color:#dee2e6}
.latRad{display:none}
.latRad:checked + .latOpt[data-good="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.latRad:checked + .latOpt[data-good="false"]{background:#f8d7da;color:#721c24;border-color:#f5b7b1}
.latFeed{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#lat-good:checked ~ .latFeed[data-type="good"],
#lat-w1:checked  ~ .latFeed[data-type="bad"],
#lat-w2:checked  ~ .latFeed[data-type="bad"]{display:block}
.latFeed[data-type="good"]{background:#d1f2eb;color:#0c5d56;border:1px solid #a3d9cc}
.latFeed[data-type="bad"]{background:#fce8e6;color:#58151c;border:1px solid #f5b7b1}
</style>

<div>
  <input type="radio" id="lat-w1" name="lat" class="latRad">
  <label for="lat-w1" class="latOpt" data-good="false">
    🖼️ Compress the PNG from 900 KB → 150 KB.
  </label>

  <input type="radio" id="lat-good" name="lat" class="latRad">
  <label for="lat-good" class="latOpt" data-good="true">
    ⚡ Move the model to a faster, always-warm GPU (weights & cache pre-loaded).
  </label>

  <input type="radio" id="lat-w2" name="lat" class="latRad">
  <label for="lat-w2" class="latOpt" data-good="false">
    ✏️ Reduce response length by 20 %.
  </label>

  <div class="latFeed" data-type="good">
    ✅ The biggest pain is the 4 s silence <em>before</em> any text streams.
    Shortening model start-up on a warm GPU tackles that gap directly.
  </div>
  <div class="latFeed" data-type="bad">
    ❌ Image size or per-token speed tweaks won’t fix the long initial pause.
  </div>
</div>
</div>

---

## 📦 Model Sizes and Requirements

Models come in different sizes. The bigger the model (measured in billions of parameters), the smarter and more detailed its responses can be. But bigger models need more powerful GPUs and more memory, which can make them slower or more expensive to run.

The biggest bottleneck for being able to load and run a model is going to be GPU memory.  
An easy way to think of it is: Number of parameters x 4 = GPU memory needed.  
For example, a 3B parameter model requires ~12GB of GPU memory to load and run.  

| Model Size     | Parameters | GPU Requirement            | Notes                            |
|----------------|------------|-----------------------------|----------------------------------|
| **<3B**         | Small      | 8–12GB VRAM                | Lightweight, fast, and easy to deploy             |
| **7B–13B**      | Medium     | ≥24GB VRAM or quantized*     | Balanced power and cost          |
| **>30B**        | Large      | Multi-GPU or high-end cards | Better at understanding context but slower and costly |

🧠 Larger models may be smarter, but smaller ones are often faster and easier to deploy.

_* Quantization makes models take up less space, so they can run faster and fit on smaller GPUs. It slightly reduces quality but often works well enough._

<!-- 📦 model size / GPU trade-off -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);
            padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">

<h3 style="margin:0 0 8px;color:#5a5a5a;">📦 Quiz</h3>

<p style="color:#495057;font-weight:500;">
You need an assistant to <b>auto-tag support tickets</b> with one of 50 categories.<br>
Traffic target: ~20 requests / sec.<br>
GPU budget: single A10 24 GB.
</p>

<p style="color:#495057;font-weight:500;">Which model choice fits best?</p>

<style>
.szOpt{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;cursor:pointer;
       border:2px solid #e9ecef;color:#495057;transition:.2s}
.szOpt:hover{background:#fff;transform:translateY(-1px);border-color:#dee2e6}
.szRad{display:none}
.szRad:checked + .szOpt[data-good="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.szRad:checked + .szOpt[data-good="false"]{background:#f8d7da;color:#721c24;border-color:#f5b7b1}
.szFeed{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#sz-good:checked ~ .szFeed[data-type="good"],
#sz-w1:checked  ~ .szFeed[data-type="bad"],
#sz-w2:checked  ~ .szFeed[data-type="bad"]{display:block}
.szFeed[data-type="good"]{background:#d1f2eb;color:#0c5d56;border:1px solid #a3d9cc}
.szFeed[data-type="bad"]{background:#fce8e6;color:#58151c;border:1px solid #f5b7b1}
</style>

<div>
  <input type="radio" id="sz-w1" name="sz" class="szRad">
  <label for="sz-w1" class="szOpt" data-good="false">
    70 B quantized to 4-bit
  </label>

  <input type="radio" id="sz-good" name="sz" class="szRad">
  <label for="sz-good" class="szOpt" data-good="true">
    7 B quantized to 16-bit
  </label>

  <input type="radio" id="sz-w2" name="sz" class="szRad">
  <label for="sz-w2" class="szOpt" data-good="false">
    3 B unquantized (FP32) running on CPU
  </label>

  <div class="szFeed" data-type="good">
    ✅ 7 B @ 16-bit ≈ 7 B × 2 byte ≈ 14 GB → easily fits 24 GB with some space for the KV-cache (context window) and meets 20 req/s.
  </div>
  <div class="szFeed" data-type="bad">
    ❌ Reminder: rough memory rule — parameters ×4 bytes (FP32) or ×2 bytes (FP16).  <br>
    Even at 0.5 B/param (4-bit), 70 B ≈ 35 GB → too big for 24 GB. <br>
    For the small 3B model, accuracy/QPS drops too much.
  </div>
</div>
</div>

---

## ✅ Summary

Let's wrap up with a quick review of important concepts that you have seen through this chapter. These terms will help you understand how LLMs work under the hood and how to think about their performance and deployment.

| Concept                | Key Idea                                                            |
|------------------------|---------------------------------------------------------------------|
| **Token**              | The smallest piece of text an LLM processes at a time—like a word or part of a word. Think of tokens as the building blocks of language for the model. |
| **Next-token machine** | LLMs work by predicting one token at a time, based on what came before. They generate responses step-by-step. |
| **Attention**          | A method that lets the model focus on the important parts of the input when deciding what token to generate next. |
| **Context length**     | How much recent conversation or text the model can "remember" at once, usually measured in tokens. |
| **KV Cache**           | A memory shortcut that helps speed up generating tokens by remembering parts of previous calculations. |
| **Prompting**          | How we guide the model’s behavior by carefully designing the input text we give it. |
| **Hallucination**      | When the model makes up facts or details that sound real but are incorrect. |
| **Guardrails**         | Techniques and controls to keep the model’s output safe, accurate, and on-topic. |
| **TTFT & TPOT**        | Metrics showing how quickly the model starts responding and how fast it produces each next word. |
| **VRAM & Throughput**  | How much GPU memory is needed and how many users can be served simultaneously. |
| **Model size & GPU**   | Picking the right model size based on your hardware and needs ensures the best balance of performance and cost. |



[🔝 Back to Contents](#contents)