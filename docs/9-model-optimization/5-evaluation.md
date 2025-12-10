# 📊 Evaluation with lm-evaluation-harness

[lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) is the gold standard for LLM benchmarking. It powers Hugging Face's Open LLM Leaderboard and is used by NVIDIA, Cohere, and dozens of other organizations.

## Why Standardized Evaluation?

Quantized models need rigorous comparison against baselines:

| Question | What Evaluation Answers |
|----------|------------------------|
| Did accuracy drop? | Benchmark scores vs baseline |
| Which tasks suffered? | Per-task breakdown |
| Is it production-ready? | Comparison to thresholds |

## Common Benchmarks

The Open LLM Leaderboard uses these benchmarks to evaluate models:

| Benchmark | What It Tests | Shot Count | Why It Matters for Quantization |
|-----------|---------------|------------|--------------------------------|
| **MMLU** | 57 academic subjects | 5-shot | General knowledge retention |
| **HellaSwag** | Commonsense inference | 10-shot | Easy for humans (~95%), hard for models |
| **ARC-Challenge** | Grade-school science | 25-shot | Reasoning under compression |
| **Winogrande** | Coreference resolution | 5-shot | Language understanding |
| **GSM8K** | Math word problems | 5-shot | Most sensitive to quantization |
| **TruthfulQA** | Factual accuracy | 0-shot | Avoiding hallucinations |

### Task Sensitivity to Quantization

Not all benchmarks respond equally to quantization:

| Sensitivity | Benchmarks | Notes |
|-------------|------------|-------|
| **High** | GSM8K, math tasks | Numeric precision matters |
| **Medium** | MMLU, ARC | Knowledge retrieval |
| **Low** | HellaSwag, Winogrande | Pattern matching robust |

Research shows formats with aggressive compression (INT4, Q3) degrade GSM8K performance earlier than other tasks.

## What Research Shows

Large-scale studies on quantized LLMs reveal:

### Accuracy Recovery

All quantization schemes recover **over 99%** of baseline accuracy on OpenLLM Leaderboard benchmarks—regardless of model size. The key findings:

- **8-bit (INT8):** Nearly lossless (<0.5% drop)
- **4-bit (INT4):** 1-3% degradation typical
- **Larger models (70B+):** More resilient to quantization
- **Smaller models (8B):** More variability, still usable

### The "Flip" Phenomenon

Accuracy alone can be misleading. Research found that even when overall accuracy stays within 1% of baseline:

- Some correct answers become incorrect after quantization
- Some incorrect answers become correct
- Math tasks show 12-30% "flip rates"

**Implication:** Don't just check aggregate scores—test your specific use cases.

### Algorithm Comparison

| Algorithm | Accuracy Retention | Notes |
|-----------|-------------------|-------|
| AWQ | Higher | More stable across tasks |
| GPTQ | Slightly lower | More noticeable on GSM8K, ARC |
| Q5_K_M (GGUF) | Optimal | Best trade-off for most domains |
| Q3_K_M (GGUF) | Use cautiously | Significant degradation risk |

## Running Evaluations

### Against Pre-deployed Models

lm-evaluation-harness can evaluate models via API endpoints:

```
lm_eval --model local-completions \
        --model_args base_url=<endpoint> \
        --tasks hellaswag,winogrande,arc_easy \
        --limit 100
```

### Efficient Evaluation with tinyBenchmarks

Full benchmarks have tens of thousands of examples. tinyBenchmarks identifies the most informative items:

| Original Benchmark | Full Size | tinyBenchmarks Size |
|-------------------|-----------|---------------------|
| MMLU | 14,000+ | ~100 examples |
| Combined (6 benchmarks) | 50,000+ | <3% of original |

This enables quick validation during development while preserving accuracy estimates.

## Acceptable Accuracy Thresholds

Use these guidelines for production decisions:

| Accuracy Drop | Recommendation | Action |
|---------------|----------------|--------|
| <1% | ✅ Ship it | Deploy with confidence |
| 1-3% | ⚠️ Acceptable | Monitor in production |
| 3-5% | 🔍 Marginal | A/B test with users |
| >5% | ❌ Too high | Try different config (g64, INT8) |

### Task-Specific Thresholds

For mission-critical tasks, apply stricter thresholds:

| Use Case | Max Acceptable Drop |
|----------|---------------------|
| Math tutoring | <2% on GSM8K |
| Code generation | <2% on HumanEval |
| General chat | <5% average |
| Summarization | <3% on MMLU |

## Making the Decision

Build a decision matrix for your quantized models:

| Model | Size | GSM8K | MMLU | HellaSwag | Avg Drop | Decision |
|-------|------|-------|------|-----------|----------|----------|
| FP16 (baseline) | 6.4 GB | 0.412 | 0.654 | 0.762 | - | Reference |
| INT8 | 3.2 GB | 0.405 | 0.651 | 0.759 | -0.8% | ✅ Ship |
| INT4 g128 | 1.8 GB | 0.389 | 0.640 | 0.751 | -2.5% | ⚠️ Monitor |
| INT4 g64 | 2.0 GB | 0.398 | 0.647 | 0.755 | -1.5% | ✅ Ship |

---

## Module Complete! 🎉

You've learned:
- ✅ Quantization fundamentals and precision formats
- ✅ PTQ algorithms with llm-compressor
- ✅ Deployment decisions: schemes, group sizes, formats
- ✅ GenAIOps pipeline for quantized models
- ✅ Evaluation with lm-evaluation-harness

Continue to **[On-Prem Practicum](../10-on-prem-practicum/README.md)** to deploy optimized models!
