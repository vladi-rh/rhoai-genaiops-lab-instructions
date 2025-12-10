# ⚡ Advanced Quantization Techniques

This section covers the deployment decisions: which precision scheme to use, how group size affects accuracy, and which output format fits your infrastructure.

## Quantization Schemes

The notation **WxAy** means x-bit weights and y-bit activations.

| Scheme | Meaning | Compression | Best For |
|--------|---------|-------------|----------|
| W8A16 | 8-bit weights, 16-bit activations | ~2x | Balanced accuracy/performance |
| W4A16 | 4-bit weights, 16-bit activations | ~3.5x | Latency-critical, edge devices |
| W8A8 | 8-bit weights and activations | ~2x | High-throughput server scenarios |

### Weight-Only vs Weight+Activation Quantization

**W4A16 / W8A16 (Weight-only)**
- Weights stored in INT4/INT8, dequantized to FP16 at inference
- Best at small batch sizes (memory-bound workloads)
- Provides ~2.4x speedup for single-stream scenarios
- Freed memory allows larger KV cache = more parallel requests

**W8A8 (Weight + Activation)**
- Both weights and activations in INT8
- Requires SmoothQuant to handle activation outliers
- Best at large batch sizes (compute-bound workloads)
- A 70B model with W8A8 on 2 GPUs matches FP16 on 4 GPUs

**The crossover:** At low batch sizes, W4A16 wins. At high batch sizes, W8A8 wins. The exact crossover depends on model size and hardware.

## Group Size

Group size controls how many weights share a single scale factor.

| Group Size | Accuracy | Overhead | Use Case |
|------------|----------|----------|----------|
| 32 | Best | Highest | Rarely needed |
| 64 | Better | Higher | Accuracy-critical (math, code) |
| **128** | Good | Balanced | **Default for most use cases** |
| 1024 | Lower | Minimal | Maximum speed |

From the GPTQ paper: moving from per-channel to g1024 improves perplexity by ~0.2, and g128 adds another ~0.1 improvement.

**Rule of thumb:** Start with g128. Only drop to g64 if benchmarks show unacceptable accuracy loss on your specific tasks.

## Output Formats

After quantization, choose a format based on your deployment target.

### SafeTensors

Developed by Hugging Face for secure, efficient tensor storage.

| Aspect | Details |
|--------|---------|
| **Security** | No code execution vulnerabilities (unlike pickle) |
| **Loading** | Lazy-loading and mmap support for speed |
| **Ecosystem** | HuggingFace, vLLM, TensorRT-LLM |
| **Best for** | GPU inference in production |

### GGUF

Designed by Georgi Gerganov for llama.cpp and consumer hardware.

| Aspect | Details |
|--------|---------|
| **Optimization** | Built for CPU inference on consumer hardware |
| **Quantization** | Flexible built-in schemes (Q4_K_M, Q5_K_M, Q8_0) |
| **Distribution** | Single-file format, easy to share |
| **Best for** | CPU inference, edge devices, Ollama |

### Choosing a Format

| Deployment Target | Recommended Format |
|-------------------|-------------------|
| vLLM on GPU | SafeTensors |
| TensorRT-LLM | SafeTensors |
| llama.cpp / Ollama | GGUF |
| Edge devices (CPU) | GGUF |
| Fine-tuning after quantization | SafeTensors |

**Workflow:** Quantize with llm-compressor to SafeTensors for GPU serving. Convert to GGUF only if deploying to CPU/edge.

## 🎯 Next Steps

Continue to **[Testing Pipeline](./4-testing-pipeline.md)** to learn how to validate and deploy quantized models.
