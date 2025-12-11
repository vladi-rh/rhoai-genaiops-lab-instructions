# 🧪 Testing and Deployment Pipeline

You've compressed the model. It's smaller, it loads faster, and you're feeling pretty good about yourself.

But does it still *work*?

This section is about making sure your compressed model doesn't embarrass you in production. Spoiler: benchmarks aren't enough.

## The Two-Stage Testing Philosophy

Here's the thing about quantized models: they can pass standardized tests with flying colors and still break your application in weird ways. So we test twice.

### Stage 1: Does the Model Still Know Things? 📚

First, verify the model didn't lose its mind during compression.

| What to Test | Why It Matters | How to Test |
|--------------|----------------|-------------|
| Perplexity | Basic language competence | lm-evaluation-harness |
| Task benchmarks | Knowledge retention | MMLU, HellaSwag, GSM8K |
| Your domain | Performance on *your* data | Custom eval sets |

#### Perplexity: The Sanity Check

Perplexity measures how "surprised" a model is by text. Given a sequence of words, how well does it predict what comes next?

- **Lower perplexity = better model** (less surprised by real text)
- **How it works:** The model sees text and predicts each word. If it assigns high probability to the correct word, perplexity goes down.
- **What it catches:** Severe compression damage. If perplexity spikes after quantization, something fundamental broke.

Think of it like a reading comprehension baseline—if the model can't predict common word sequences, it's probably not going to answer questions well either.

#### Task Benchmarks: Testing Actual Knowledge

These are multiple-choice or short-answer tests that probe specific capabilities:

| Benchmark | What It Tests | Format |
|-----------|---------------|--------|
| **MMLU** | 57 academic subjects (history, math, law, medicine...) | Multiple choice |
| **HellaSwag** | Commonsense reasoning ("What happens next?") | Multiple choice |
| **GSM8K** | Grade-school math word problems | Generate the answer |
| **ARC** | Science questions at grade-school level | Multiple choice |
| **TruthfulQA** | Resistance to common misconceptions | Multiple choice |
| **HumanEval** | Python coding problems | Generate code |
| **MBPP** | Basic Python programming tasks | Generate code |

**How they actually work:**

For **multiple-choice** benchmarks, the model doesn't "pick A, B, C, or D." Instead, you feed each possible completion to the model and measure which one has the lowest perplexity. The model essentially rates how natural each answer sounds given the question.

For **generative** benchmarks (like GSM8K), the model produces an answer, and you check if it matches the correct solution—usually with some parsing to extract the final number.

For **coding** benchmarks (like HumanEval), the model generates a function body, and the test harness runs it against test cases. If the code executes correctly and produces the right output, it passes.

#### Why Benchmark Selection Matters

Different benchmarks stress different capabilities:

| Capability | Most Sensitive Benchmark |
|------------|-------------------------|
| Math/numeric precision | GSM8K (often first to degrade) |
| World knowledge | MMLU |
| Reasoning chains | ARC-Challenge |
| Common sense | HellaSwag, Winogrande |
| Code generation | HumanEval, MBPP |

If Canopy does math tutoring, GSM8K matters most. If it helps with coding, HumanEval is critical. For a general assistant, balance across all of them.

**The good news:** Studies consistently show that both 8-bit and 4-bit quantized models retain accuracy very close to their FP16 baselines. Large models (70B+) exhibit almost no degradation, while smaller ones (around 8B) show slightly more variation but still perform reliably.

### Stage 2: Does Canopy Still Work? 🌳

Here's where most people get burned. A model can ace benchmarks and still break your app.

| What to Test | What Can Go Wrong |
|--------------|-------------------|
| System prompts | Model ignores instructions it used to follow |
| Agent workflows | Tool calling breaks, reasoning chains derail |
| Edge cases | Those weird inputs that "used to work" don't |
| Output formats | JSON becomes malformed, markdown gets weird |

> ⚠️ **The trap:** Quantization affects instruction-following and chain-of-thought reasoning *differently* than raw accuracy. Your benchmarks might say "all clear" while Canopy is hallucinating in production.

**Always test your actual application flows.**

<!-- 🧪 Quiz: The Testing Trap -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">
<h3 style="margin:0 0 8px;color:#5a5a5a;">📝 Quick Check: The Testing Trap</h3>
<p style="margin:0 0 12px;color:#666;">Your quantized model scores 98% on MMLU and passes all standard benchmarks. You deploy it to production. A week later, students complain that Canopy is ignoring their system prompts and returning malformed JSON. What went wrong?</p>
<style>
.quiz-container-testing{position:relative}
.quiz-option-testing{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;cursor:pointer;transition:.2s;border:2px solid #e9ecef;color:#495057}
.quiz-option-testing:hover{background:#e9ecef}
.quiz-radio-testing{display:none}
.quiz-radio-testing:checked+.quiz-option-testing[data-correct="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.quiz-radio-testing:checked+.quiz-option-testing:not([data-correct="true"]){background:#f8d7da;color:#721c24;border-color:#f5b7b1}
.feedback-testing{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#testing-correct:checked~.feedback-testing[data-feedback="correct"]{display:block;background:#d4edda;color:#155724}
#testing-wrong1:checked~.feedback-testing[data-feedback="wrong1"],#testing-wrong2:checked~.feedback-testing[data-feedback="wrong2"],#testing-wrong3:checked~.feedback-testing[data-feedback="wrong3"]{display:block;background:#f8d7da;color:#721c24}
</style>
<div class="quiz-container-testing">
<input type="radio" name="quiz-testing" id="testing-wrong1" class="quiz-radio-testing">
<label for="testing-wrong1" class="quiz-option-testing" data-correct="false">📊 The benchmarks were too easy—you should have used harder tests</label>
<input type="radio" name="quiz-testing" id="testing-correct" class="quiz-radio-testing">
<label for="testing-correct" class="quiz-option-testing" data-correct="true">🧪 You only tested Stage 1 (knowledge) but skipped Stage 2 (application flows)</label>
<input type="radio" name="quiz-testing" id="testing-wrong2" class="quiz-radio-testing">
<label for="testing-wrong2" class="quiz-option-testing" data-correct="false">🔢 The model needed a smaller group size</label>
<input type="radio" name="quiz-testing" id="testing-wrong3" class="quiz-radio-testing">
<label for="testing-wrong3" class="quiz-option-testing" data-correct="false">⏱️ You deployed too quickly—should have waited longer</label>
<div class="feedback-testing" data-feedback="correct">✅ <strong>Exactly!</strong> Benchmark scores test knowledge retention, but quantization can break instruction-following and output formatting in ways benchmarks don't catch. Always test your actual application flows—system prompts, tool calling, JSON output—before deploying.</div>
<div class="feedback-testing" data-feedback="wrong1">❌ MMLU is already challenging. The problem isn't test difficulty—it's that benchmarks measure different things than application behavior.</div>
<div class="feedback-testing" data-feedback="wrong2">❌ Group size affects accuracy, but the issue here is <em>what</em> you tested, not <em>how</em> you quantized.</div>
<div class="feedback-testing" data-feedback="wrong3">❌ Timing isn't the issue. You could wait a year and still hit this problem if you only run benchmark tests.</div>
</div>
</div>

### About Those "Emergent Abilities"

The upside: Studies show that key capabilities—such as in-context learning, chain-of-thought reasoning, and instruction following—remain intact under INT4 quantization.
The downside: At 2 bits, these abilities degrade severely. Anything below 4-bit isn’t viable for meaningful workloads.

## Model Cards: Because Future You Will Forget

Six months from now, someone (probably you) will ask: "What algorithm did we use on this model? What calibration data? Why did we choose g64?"

Model cards are your insurance policy against amnesia.

### What to Document

| Section | What to Include |
|---------|-----------------|
| **Base model** | Link to the original (so you can trace lineage) |
| **Quantization config** | Algorithm, scheme, group size—the recipe |
| **Accuracy metrics** | How much did we lose? Perplexity delta, benchmark scores |
| **Performance wins** | Memory reduction, speedup—the payoff |
| **Calibration data** | What dataset did we use? This matters for reproducibility |
| **Known issues** | Where does it struggle? Save your teammates the debugging |

### HuggingFace Metadata

If you're uploading to HuggingFace Hub, tag it properly:

```yaml
base_model: meta-llama/Llama-3.2-3B-Instruct
base_model_relation: quantized
tags:
  - quantized
  - gptq
  - int4
```

This helps others (and future you) find related models.

## Organizing Your Model variants

You're going to end up with multiple variants. Stay organized or drown.

```
models/
├── llama-3.2-3b/
│   ├── v1.0-fp16/           # Baseline (your reference point)
│   ├── v1.1-int8/           # Conservative compression
│   ├── v1.2-int4-g128/      # Aggressive, default group size
│   └── v1.3-int4-g64/       # Aggressive, better accuracy
```

**The naming scheme:** `{model}-{version}-{precision}-{config}`

For each variant, track:
- The recipe used (so you can reproduce it)
- Calibration dataset (same reason)
- Benchmark results (so you can compare)
- Where it's deployed (test? staging? prod?)

## GitOps: Ship Models Like Software

You've been using Argo CD to deploy Canopy. Good news: compressed models work the same way.

### Why This Works

| GitOps Benefit | What It Means for Models |
|----------------|--------------------------|
| **Git is truth** | The repo says what's deployed. Period. |
| **Audit trail** | "Who deployed this?" → Check the commit log |
| **Easy rollback** | Model breaking prod? Revert the commit. Done. |
| **Multi-environment** | Same workflow: test → staging → prod |

### ModelCars: Models as Container Images

Here's the trick that makes GitOps really sing for ML: [ModelCars](https://developers.redhat.com/articles/2025/01/30/build-and-deploy-modelcar-container-openshift-ai).

Instead of pulling models from S3 or HuggingFace at runtime, you package the model *into* a container image. The model files live in a `/models` directory inside the container—no external storage needed.

**Why this matters:**

| Traditional Approach | ModelCar Approach |
|---------------------|-------------------|
| Model in S3, reference in config | Model *is* the container |
| Runtime download delays | Cached on node after first pull |
| Separate versioning systems | Same tags as your app images |
| Different promotion workflows | Use your existing CI/CD |
| Mutable storage (files can change) | **Immutable**—what you tag is what you get |

**The immutability guarantee:** Once you push `llama-3.2-3b:v1.2-int4-g64`, that tag always refers to *exactly* that model. No one can quietly swap the weights. No "it worked yesterday" mysteries. The SHA256 digest proves it's the same artifact you tested.

**The workflow:**

1. Compress your model (you just learned how)
2. Build a container with the model in `/models`
3. Push to your OCI registry (Quay, Harbor, etc.)
4. Tag it with a meaningful version (`v1.2-int4-g64`)
5. Reference the image tag in your deployment config
6. Argo CD picks it up—done

```dockerfile
# Simple ModelCar Dockerfile
FROM scratch
COPY ./compressed-model /models/
```

**The catch:** This works best for smaller, compressed models. A 900GB model makes for a painful container pull. But that INT4 model you just compressed? Perfect fit.

**The payoff:** Once the image is cached on a node, vLLM startup is *fast*. No waiting for S3 downloads. Your model versions are just container tags living right next to your app images in the registry. And because they're immutable, you can deploy with confidence—what passed your tests is *exactly* what runs in production.

### The Promotion Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Experiment │ ──► │    Test     │ ──► │    Prod     │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
   Compress &          Run the            Deploy &
   quick eval        full suite           monitor
```

**The gates:**
1. **Experiment → Test:** Perplexity within 3% of baseline
2. **Test → Prod:** All system tests pass, Canopy works correctly
3. **Prod:** Canary rollout, watch the metrics

### When Things Go Wrong (Rollback)

The beautiful thing about GitOps: rollback is just `git revert`.

**Red flags that mean "rollback now":**
- Accuracy drops in production monitoring
- Students complaining about weird responses
- System prompts being ignored

**Time to recover:** Minutes, not hours. That's why we do this.

## Keep Watching After Launch

Deployment isn't the finish line. Monitor these:

| Metric | What You're Looking For |
|--------|-------------------------|
| Response latency | Should improve (that's why we compressed!) |
| Error rates | New failure modes = something's wrong |
| User feedback | Students notice quality drops before benchmarks do |
| Token throughput | Verify you got the speedup you expected |

**Pro tip:** GuideLLM can simulate realistic traffic and measure throughput, latency, and time-to-first-token. Run it before *and* after to prove the win.

## 🎯 Next Steps

Time to get rigorous. Continue to **[Evaluation](./5-evaluation.md)** for systematic benchmarking with lm-evaluation-harness.
