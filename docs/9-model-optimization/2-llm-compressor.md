# 🔧 LLM-Compressor: Your Model's Personal Trainer

So you understand what quantization is—now let's actually do it.

[llm-compressor](https://github.com/vllm-project/llm-compressor) is the tool the vLLM team built to compress models for production. Think of it as a Swiss Army knife for quantization: one tool, multiple algorithms, works with HuggingFace, outputs models ready for vLLM serving.

## Why This Tool?

| Feature | Why You Care |
|---------|--------------|
| **Production-tested** | Built by the vLLM team—they use it themselves |
| **HuggingFace native** | Load any Transformers model, compress, save |
| **All the algorithms** | GPTQ, AWQ, SmoothQuant, SparseGPT in one place |
| **vLLM ready** | Output models just work with your serving stack |

## The PTQ Workflow

Post-Training Quantization (PTQ) compresses a model *after* it's been trained—no expensive retraining required. It's like tailoring a suit: the fabric (knowledge) is already there, you're just making it fit better.

Here's what happens under the hood:

1. **Load the model** — Start with your FP16/FP32 model
2. **Feed it calibration data** — Show the model representative inputs
3. **Learn the ranges** — Algorithm figures out typical activation values
4. **Compress with compensation** — Quantize weights while minimizing error
5. **Save the result** — Export your shiny compressed model

**Why calibration matters:** Imagine compressing a photo without knowing what's in it—you might crush the important details. Calibration data teaches the algorithm what "normal" looks like, so it knows what to preserve.

## Pick Your Algorithm

Not all compression algorithms are created equal. Here are the main contenders—each with its own personality.

### GPTQ: The Perfectionist 🎯

The gold standard for INT4 weight quantization. If accuracy is your top priority, start here.

**The suitcase analogy:** Imagine packing a suitcase where everything needs to fit perfectly. Naive packing just squishes everything—some items get damaged. GPTQ is like a master packer who, after compressing one item, carefully rearranges nearby items to compensate. The result? Everything fits, nothing's crushed.

**Under the hood:**
- Processes weights layer by layer
- Uses math (Hessian matrices) to figure out which weights matter most
- After quantizing each weight, tweaks the remaining weights to compensate
- Slower, but worth it for quality

**Use it when:** Accuracy is non-negotiable

### AWQ: The Speed Demon 🏎️

Faster than GPTQ, nearly as accurate. Won the MLSys 2024 Best Paper Award—so it's not just fast, it's clever.

**The photography analogy:** Imagine editing a sunset photo. If you apply the same settings everywhere, you'll either blow out the sun or lose the landscape. AWQ identifies the "highlight" channels—the weights that matter most based on activation patterns—and protects them during compression.

**Under the hood:**
- Finds "salient" channels by looking at activation magnitudes
- Scales important weights up before quantization (protects them)
- Scales activations down to balance things out
- No expensive backpropagation needed

**Use it when:** You need results today, not tomorrow

### SmoothQuant: The Equalizer ⚖️

The only way to quantize *both* weights AND activations to INT8. This is how you get true W8A8.

**The problem:** Weights are well-behaved and easy to compress. Activations are wild—they have outliers that ruin everything.

**The seesaw analogy:** Picture two people on a seesaw—one heavyweight (difficult activations with outliers), one lightweight (easy weights). SmoothQuant transfers some weight from the heavy side to the light side, balancing the seesaw so both can be handled equally.

**Under the hood:**
- Mathematically shifts the quantization difficulty from activations to weights
- Multiplies activations by a smoothing factor (tames the outliers)
- Divides weights by the same factor (they can absorb it)

**Use it when:** You need W8A8 for maximum throughput on INT8 hardware

### SparseGPT: The Marie Kondo 🗑️

Why just compress when you can delete? SparseGPT removes entire weights that don't "spark joy" (contribute to accuracy), then compresses what's left.

**The editing analogy:** Like editing a novel—first cut the filler paragraphs entirely (pruning), then tighten the prose (quantization). You end up with something that's both shorter AND better.

**Under the hood:**
- Identifies weights that can be zeroed without hurting accuracy
- Uses GPTQ-style compensation to maintain quality
- Can combine sparsity + quantization for extreme compression

**Use it when:** You're going for maximum compression and have the patience to tune it

## The Cheat Sheet

Still not sure? Here's the quick decision guide:

| Your Situation | Algorithm | Why |
|----------------|-----------|-----|
| "I need the best accuracy possible" | GPTQ (g128) | Gold standard error compensation |
| "I needed this done yesterday" | AWQ | Fast and good enough |
| "I want W8A8 for max throughput" | SmoothQuant | Only game in town for activation quantization |
| "Squeeze it as much as possible" | SparseGPT + GPTQ | Pruning + quantization combo |
| "Just tell me what to use" | GPTQ or AWQ | Battle-tested, vLLM loves them |

## 🧪 Time to Get Your Hands Dirty

Enough reading—let's compress a model!

Open the notebook: **`experiments/9-model-optimization/1-intro-llm-compressor.ipynb`**

In this exercise, you'll take a small model and compress it on CPU (yes, CPU—no fancy hardware needed to learn).

**What you'll do:**

1. **Meet the oneshot API** — llm-compressor's main interface. One function call, compressed model.

2. **Write a recipe** — Configure `GPTQModifier` with parameters like `scheme`, `targets`, and `ignore`

3. **Compress a model** — We'll use `Qwen/Qwen2-0.5B-Instruct` as our guinea pig

4. **See the difference** — Compare file sizes before and after (prepare to be impressed)

When you're done, come back and we'll dive into the advanced stuff.

## 🎯 Next Steps

Continue to **[Advanced Quantization](./3-advanced-quantization.md)** to learn about schemes, group sizes, and output formats.
