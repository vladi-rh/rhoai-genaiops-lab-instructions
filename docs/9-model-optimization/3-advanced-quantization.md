# ⚡ Advanced Quantization: The Deployment Playbook

You've compressed a model. Now comes the real question: *which* compression for *your* situation?

This is where quantization gets strategic. The right choice depends on your hardware, your traffic patterns, and how much accuracy you're willing to trade.

## Decoding the Notation

You'll see notation like "W4A16" everywhere. Here's the decoder ring:

**WxAy** = x-bit **W**eights, y-bit **A**ctivations

| Scheme | Translation | Size Reduction | Sweet Spot |
|--------|-------------|----------------|------------|
| W8A16 | 8-bit weights, 16-bit activations | ~2x smaller | Safe choice, balanced |
| W4A16 | 4-bit weights, 16-bit activations | ~3.5x smaller | Edge devices, latency-critical |
| W8A8 | 8-bit everything | ~2x smaller | High-throughput servers |

## Weight-Only vs. Full Quantization

Here's where it gets interesting. There are two philosophies:

### The "Just Compress the Weights" Approach (W4A16 / W8A16)

Store weights as INT4/INT8, but run math in FP16. It's like storing your photos as compressed JPEGs but editing them in RAW.

**Why it works:**
- Weights are static—compress once, benefit forever
- Activations stay precise—no accuracy hit from math errors
- Memory savings unlock bigger KV caches = more parallel requests

**The numbers:** ~2.4x speedup for single requests. Perfect for "one student at a time" scenarios.

### The "Compress Everything" Approach (W8A8)

Both weights AND activations in INT8. This is the throughput play.

**Why it works:**
- INT8 math is *fast* on modern hardware
- More students per GPU at peak hours
- A 70B model on 2 GPUs can match FP16 on 4 GPUs

**The catch:** You need SmoothQuant to tame those activation outliers.

### When to Use Which?

Here's the decision framework:

| Traffic Pattern | Best Choice | Why |
|-----------------|-------------|-----|
| Single student, fast response needed | W4A16 | Memory-bound, latency wins |
| Lots of students, peak hours | W8A8 | Compute-bound, throughput wins |
| "I don't know yet" | W8A16 | Safe default, good balance |

**The crossover point:** At low batch sizes, weight-only wins. At high batch sizes, W8A8 wins. Your mileage varies by hardware.

## Group Size: The Precision Dial

Remember how we mentioned scales—those little numbers that help reconstruct the original values? Group size determines how many weights share a single scale.

**Smaller group = more scales = better accuracy = bigger file**

Think of it like resolution in an image:

| Group Size | Quality | Overhead | When to Use |
|------------|---------|----------|-------------|
| 32 | 🏆 Best | Highest | Rarely worth it |
| 64 | ⭐ Better | Higher | Math-heavy tasks, code generation |
| **128** | ✅ Good | Balanced | **Start here (the default)** |
| 1024 | 🔽 Lower | Minimal | When speed trumps everything |

**From the research:** Going from per-channel to g1024 improves perplexity by ~0.2 points. Dropping to g128 adds another ~0.1 improvement. After that, diminishing returns.

**The rule:** Start with g128. Only go to g64 if your benchmarks scream for mercy on math or code tasks.

## Output Formats: Where Will This Model Live?

You've compressed the model. Now: what file format?

This isn't just about file extensions—it's about *where* and *how* you'll serve the model.

### SafeTensors: The GPU Standard 🖥️

Created by HuggingFace for production GPU serving. This is what vLLM expects.

| Why It's Good | The Details |
|---------------|-------------|
| **Secure** | No vulnerabilities (your security team will thank you) |
| **Fast loading** | Lazy-loading and memory mapping |
| **Ecosystem** | HuggingFace, vLLM, TensorRT-LLM all speak it |

**Use it for:** Anything running on GPUs in your cluster.

### GGUF: The Edge Format 📱

Created by Georgi Gerganov for llama.cpp. This is how you run models on laptops, phones, and that Raspberry Pi in the corner.

| Why It's Good | The Details |
|---------------|-------------|
| **CPU-optimized** | Built for inference without GPUs |
| **Flexible quantization** | Q4_K_M, Q5_K_M, Q8_0—lots of options |
| **Single file** | One file = easy to distribute |

**Use it for:** Ollama, llama.cpp, edge devices, offline deployments.

### The Quick Reference

| Where's the Model Going? | Format |
|--------------------------|--------|
| vLLM on Kubernetes | SafeTensors |
| TensorRT-LLM | SafeTensors |
| Ollama / llama.cpp | GGUF |
| Edge device (CPU) | GGUF |
| Future fine-tuning | SafeTensors |

**The workflow:** Compress with llm-compressor → SafeTensors for GPU. Only convert to GGUF if you're deploying to CPU/edge.

## 🎯 Next Steps

You know what to compress and how. Now let's make sure it actually works.

Continue to **[Testing Pipeline](./4-testing-pipeline.md)** to learn how to validate quantized models before they hit production.
