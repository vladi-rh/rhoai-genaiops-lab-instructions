# 🧪 Testing and Deployment Pipeline

Quantizing a model is only half the job. This section covers how to validate quantized models and deploy them through your GenAIOps pipeline.

## Two-Stage Testing

When you quantize a model, test **two things**:

### Stage 1: Test the Model Itself

Validate that the quantized model maintains acceptable accuracy:

| Test Type | What It Measures | Tools |
|-----------|------------------|-------|
| Perplexity | Language modeling quality | lm-evaluation-harness |
| Task benchmarks | Accuracy on specific tasks | MMLU, HellaSwag, GSM8K |
| Domain-specific | Performance on your use case | Custom eval sets |

Research shows 8-bit and 4-bit quantized LLMs maintain competitive accuracy—larger models (70B+) show negligible degradation, while smaller models (8B) may have slight variability but preserve semantic meaning.

### Stage 2: Test the AI System

A model can pass benchmarks but break your application. Test the complete system:

| Test Type | What to Verify |
|-----------|----------------|
| System prompts | Still produce expected behavior |
| Agent workflows | Tool calling, reasoning chains work |
| Edge cases | Inputs that previously worked still work |
| Response format | JSON, markdown, structured outputs intact |

> ⚠️ **Critical insight:** Quantization can affect instruction-following and chain-of-thought reasoning differently than raw accuracy. Always test your specific application flows.

### Emergent Abilities

Research confirms that emergent abilities (in-context learning, chain-of-thought reasoning, instruction-following) still exist in 4-bit quantization. However, 2-bit models encounter severe performance degradation—avoid going below 4-bit for production.

## Model Cards for Quantized Models

Document every quantized model with a model card. This is essential for reproducibility, discoverability, and team communication.

### What to Include

| Section | Content |
|---------|---------|
| **Base model** | Link to original model |
| **Quantization config** | Algorithm, scheme, group size |
| **Accuracy metrics** | Perplexity delta, benchmark scores |
| **Performance metrics** | Memory reduction, speedup |
| **Recommendations** | Good use cases, known limitations |
| **Calibration data** | What dataset was used |

### Hugging Face Metadata

When uploading to Hugging Face Hub, set the relationship explicitly:

```yaml
base_model: meta-llama/Llama-3.2-3B-Instruct
base_model_relation: quantized
tags:
  - quantized
  - gptq
  - int4
```

This helps users discover your model and understand its relationship to the base model.

## Version Control Strategy

Organize quantized model variants systematically:

```
models/
├── llama-3.2-3b/
│   ├── v1.0-fp16/           # Baseline (reference)
│   ├── v1.1-int8/           # INT8 quantized
│   ├── v1.2-int4-g128/      # INT4, group size 128
│   └── v1.3-int4-g64/       # INT4, group size 64
```

**Naming convention:** `{model}-{version}-{precision}-{config}`

Track each variant with:
- Quantization recipe used
- Calibration dataset
- Benchmark results
- Deployment history

## GitOps Deployment with Argo CD

Argo CD provides declarative, GitOps continuous delivery for Kubernetes. It continuously monitors your Git repository and automatically syncs the cluster state to match.

### Why GitOps for Model Deployment?

| Benefit | Description |
|---------|-------------|
| **Single source of truth** | Git repo defines what's deployed |
| **Audit trail** | Every change tracked in git history |
| **Easy rollback** | Revert commit = revert deployment |
| **Multi-environment** | Same process for test → staging → prod |

### Promotion Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Experiment │ ──► │    Test     │ ──► │    Prod     │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
   Quantize &          Full test           Deploy &
   quick eval          suite               monitor
```

**Stage gates:**
1. **Experiment → Test:** Perplexity within 3% of baseline
2. **Test → Prod:** All system tests pass, no regressions
3. **Prod:** Canary deployment, monitor for issues

### Rollback Strategy

GitOps makes rollback trivial—revert the commit and Argo CD syncs automatically.

**When to rollback:**
- Accuracy drops detected in production monitoring
- User complaints about response quality
- System prompt behavior changes unexpectedly

**Rollback time:** Minutes, not hours. This is the power of GitOps.

## Production Monitoring

After deployment, continuously monitor:

| Metric | Why It Matters |
|--------|----------------|
| Response latency | Quantization should improve this |
| Error rates | Watch for new failure modes |
| User feedback | Quality issues users notice |
| Token throughput | Verify expected speedup |

Tools like GuideLLM can simulate real-world traffic and measure throughput, latency, and time-to-first-token against your deployed models.

## 🎯 Next Steps

Continue to **[Evaluation](./5-evaluation.md)** for systematic benchmarking with lm-evaluation-harness.
