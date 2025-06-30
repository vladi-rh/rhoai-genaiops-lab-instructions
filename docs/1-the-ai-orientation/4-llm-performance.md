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

Model size matters—for performance *and* capability.

| Model Size     | Parameters | GPU Requirement            | Notes                            |
|----------------|------------|-----------------------------|----------------------------------|
| **<3B**         | Small      | 8–12GB VRAM (1 GPU)         | Lightweight and fast             |
| **7B–13B**      | Medium     | ≥24GB VRAM or quantization  | Balanced power vs. cost          |
| **>30B**        | Large      | Multi-GPU or high-end cards | Slower, but more context-aware   |

🧠 Larger models may be smarter, but smaller ones are often faster and easier to deploy.

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