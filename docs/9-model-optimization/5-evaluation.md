# 📊 Evaluation: Prove It Works

You've compressed your model. Your tests pass. Your gut says it's fine.

But "gut feeling" doesn't fly in production. You need numbers. You need benchmarks. You need *evidence*.

Enter [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)—the same tool that powers HuggingFace's Open LLM Leaderboard. If it's good enough for NVIDIA and Cohere, it's good enough for us.

## Why Bother With Formal Benchmarks?

Because "it seems to work" isn't a deployment strategy.

| The Question | What Benchmarks Tell You |
|--------------|--------------------------|
| Did we break it? | Scores vs baseline—the receipts |
| Where did it hurt? | Per-task breakdown shows weak spots |
| Can we ship it? | Compare against your thresholds |

## The Benchmark Menu

These are the tests that matter—the same ones used on the Open LLM Leaderboard:

| Benchmark | What It Tests | Why It Matters for Quantization |
|-----------|---------------|--------------------------------|
| **MMLU** | 57 academic subjects | Did the model forget what it learned? |
| **HellaSwag** | Commonsense inference | Humans ace this (~95%), models struggle |
| **ARC-Challenge** | Grade-school science | Can it still reason under compression? |
| **Winogrande** | Pronoun resolution | Basic language understanding intact? |
| **GSM8K** | Math word problems | ⚠️ **Most sensitive to quantization** |
| **TruthfulQA** | Factual accuracy | Still avoiding hallucinations? |

### Which Tasks Feel the Pain?

Not all benchmarks are created equal when it comes to quantization sensitivity:

| Sensitivity | Benchmarks | Why |
|-------------|------------|-----|
| 🔴 **High** | GSM8K, math tasks | Numeric precision matters—compression hurts |
| 🟡 **Medium** | MMLU, ARC | Knowledge retrieval—some degradation |
| 🟢 **Low** | HellaSwag, Winogrande | Pattern matching—pretty robust |

**The warning:** If you're doing math tutoring with Canopy, watch GSM8K like a hawk. It's usually the first to show cracks.

## What the Research Actually Says

Here's the good news: large-scale studies show quantization works better than you'd fear.

### The Headlines

All quantization schemes recover **over 99%** of baseline accuracy on OpenLLM Leaderboard benchmarks. Here's the breakdown:

| Precision | What to Expect |
|-----------|----------------|
| **INT8** | Nearly lossless—less than 0.5% drop |
| **INT4** | 1-3% degradation is typical |
| **70B+ models** | More resilient (bigger = better cushion) |
| **8B models** | More variability, but still usable |

### The Plot Twist: Answer Flipping

Here's something that'll keep you up at night. Even when aggregate accuracy stays within 1% of baseline:

- Some correct answers become *incorrect*
- Some incorrect answers become *correct*
- On math tasks, 12-30% of answers "flip"

**What this means:** The average looks fine, but individual questions behave differently. Don't just check the summary score—test your actual use cases.

### Which Algorithm Wins?

| Algorithm | Accuracy Retention | The Verdict |
|-----------|-------------------|-------------|
| AWQ | Higher | More stable across tasks |
| GPTQ | Slightly lower | More variability on GSM8K, ARC |
| Q5_K_M (GGUF) | Sweet spot | Best trade-off for most use cases |
| Q3_K_M (GGUF) | Risky | Significant degradation—use carefully |

## Running Your Own Evaluations

### Testing a Deployed Model

lm-evaluation-harness can hit your model's API endpoint directly:

```bash
lm_eval --model local-completions \
        --model_args base_url=<your-endpoint> \
        --tasks hellaswag,winogrande,arc_easy \
        --limit 100
```

### Don't Have All Day? Use tinyBenchmarks

Full benchmarks have tens of thousands of questions. tinyBenchmarks cherry-picks the most informative ones:

| Benchmark | Full Size | tinyBenchmarks |
|-----------|-----------|----------------|
| MMLU | 14,000+ questions | ~100 questions |
| All 6 benchmarks | 50,000+ questions | <3% of the total |

Same accuracy estimates, fraction of the time. Perfect for quick validation during development.

## The Decision Framework

### General Thresholds

When should you ship? Here's the rule of thumb:

| Accuracy Drop | Verdict | What to Do |
|---------------|---------|------------|
| <1% | ✅ **Ship it** | Deploy with confidence |
| 1-3% | ⚠️ **Acceptable** | Deploy, but monitor closely |
| 3-5% | 🔍 **Marginal** | A/B test with real users |
| >5% | ❌ **Too much** | Try INT8 or smaller group size |

### Task-Specific Thresholds

If Canopy is helping with specific tasks, apply stricter standards:

| What Canopy Does | Max Acceptable Drop |
|------------------|---------------------|
| Math tutoring | <2% on GSM8K |
| Code help | <2% on HumanEval |
| General chat | <5% average |
| Summarization | <3% on MMLU |

<!-- 📊 Quiz: Ship or Not? -->
<div style="background:linear-gradient(135deg,#e8f2ff 0%,#f5e6ff 100%);padding:20px;border-radius:10px;margin:20px 0;border:1px solid #d1e7dd;">
<h3 style="margin:0 0 8px;color:#5a5a5a;">📝 Quick Check: Ship or Not?</h3>
<p style="margin:0 0 12px;color:#666;">Your team quantized a model to INT4. Benchmark results show: 4% drop on GSM8K, 1% drop on MMLU, 1% drop on HellaSwag. Canopy is being used as a math tutoring assistant. Should you ship this model?</p>
<style>
.quiz-container-ship{position:relative}
.quiz-option-ship{display:block;margin:4px 0;padding:8px 16px;background:#f8f9fa;border-radius:6px;cursor:pointer;transition:.2s;border:2px solid #e9ecef;color:#495057}
.quiz-option-ship:hover{background:#e9ecef}
.quiz-radio-ship{display:none}
.quiz-radio-ship:checked+.quiz-option-ship[data-correct="true"]{background:#d4edda;color:#155724;border-color:#c3e6cb}
.quiz-radio-ship:checked+.quiz-option-ship:not([data-correct="true"]){background:#f8d7da;color:#721c24;border-color:#f5b7b1}
.feedback-ship{display:none;margin:4px 0;padding:8px 16px;border-radius:6px}
#ship-correct:checked~.feedback-ship[data-feedback="correct"]{display:block;background:#d4edda;color:#155724}
#ship-wrong1:checked~.feedback-ship[data-feedback="wrong1"],#ship-wrong2:checked~.feedback-ship[data-feedback="wrong2"],#ship-wrong3:checked~.feedback-ship[data-feedback="wrong3"]{display:block;background:#f8d7da;color:#721c24}
</style>
<div class="quiz-container-ship">
<input type="radio" name="quiz-ship" id="ship-wrong1" class="quiz-radio-ship">
<label for="ship-wrong1" class="quiz-option-ship" data-correct="false">✅ Ship it—the average drop is only ~2%, which is acceptable</label>
<input type="radio" name="quiz-ship" id="ship-wrong2" class="quiz-radio-ship">
<label for="ship-wrong2" class="quiz-option-ship" data-correct="false">⚠️ Ship and monitor—1-3% overall is within acceptable range</label>
<input type="radio" name="quiz-ship" id="ship-correct" class="quiz-radio-ship">
<label for="ship-correct" class="quiz-option-ship" data-correct="true">❌ Don't ship—4% GSM8K drop exceeds the 2% threshold for math tutoring</label>
<input type="radio" name="quiz-ship" id="ship-wrong3" class="quiz-radio-ship">
<label for="ship-wrong3" class="quiz-option-ship" data-correct="false">🔍 Run more benchmarks before deciding</label>
<div class="feedback-ship" data-feedback="correct">✅ <strong>Correct!</strong> Task-specific thresholds matter more than averages. For math tutoring, GSM8K is the critical benchmark—and 4% exceeds your 2% threshold. Try INT8 or a smaller group size (g64) to recover accuracy on math tasks.</div>
<div class="feedback-ship" data-feedback="wrong1">❌ Averaging hides the problem! For math tutoring, GSM8K is the benchmark that matters—and 4% is double your acceptable threshold.</div>
<div class="feedback-ship" data-feedback="wrong2">❌ The general thresholds don't apply here. Since Canopy is specifically for math tutoring, GSM8K's 4% drop exceeds the task-specific 2% limit.</div>
<div class="feedback-ship" data-feedback="wrong3">❌ You already have the data you need. GSM8K is the right benchmark for math tutoring—and it's clearly above threshold. More benchmarks won't change the decision.</div>
</div>
</div>

## The Decision Matrix

Put it all together in a comparison table:

| Model Variant | Size | GSM8K | MMLU | HellaSwag | Avg Drop | Ship It? |
|---------------|------|-------|------|-----------|----------|----------|
| FP16 (baseline) | 6.4 GB | 0.412 | 0.654 | 0.762 | — | Reference |
| INT8 | 3.2 GB | 0.405 | 0.651 | 0.759 | -0.8% | ✅ Yes |
| INT4 g128 | 1.8 GB | 0.389 | 0.640 | 0.751 | -2.5% | ⚠️ Monitor |
| INT4 g64 | 2.0 GB | 0.398 | 0.647 | 0.755 | -1.5% | ✅ Yes |

---

## 🎉 Module Complete!

You made it. Here's what you now know:

- ✅ **Quantization fundamentals** — What it is, why it works, what can go wrong
- ✅ **The algorithms** — GPTQ, AWQ, SmoothQuant, and when to use each
- ✅ **Deployment choices** — Schemes, group sizes, output formats
- ✅ **The pipeline** — Testing, model cards, GitOps deployment
- ✅ **Evaluation** — Benchmarks, thresholds, and making the call

**The bottom line:** You can cut your model's memory by 4x and still ship something students won't complain about. Now go make finance happy.

Continue to **[On-Prem Practicum](../10-on-prem-practicum/README.md)** to deploy your optimized models!
