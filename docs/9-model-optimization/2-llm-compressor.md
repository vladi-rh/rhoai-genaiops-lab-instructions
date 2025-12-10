# 🔧 LLM-Compressor and PTQ Methods

[llm-compressor](https://github.com/vllm-project/llm-compressor) is the production quantization toolkit from the vLLM project. It provides a unified interface for applying various Post-Training Quantization (PTQ) algorithms to large language models.

## Why LLM-Compressor?

- **Production-ready**: Built by the vLLM team for real-world deployment
- **HuggingFace integration**: Works directly with Transformers models
- **Multiple algorithms**: GPTQ, AWQ, SmoothQuant, SparseGPT in one toolkit
- **vLLM optimized**: Output models work seamlessly with vLLM serving

## Understanding PTQ

Post-Training Quantization (PTQ) converts a pre-trained model to lower precision *without retraining*. This is different from Quantization-Aware Training (QAT), which requires training with quantization in the loop.

**PTQ workflow:**
1. Load pre-trained model (FP16/FP32)
2. Run calibration data through the model
3. Compute optimal scales based on activation statistics
4. Apply quantization with error compensation
5. Save quantized model

**Why calibration matters:** The calibration dataset helps the algorithm understand the typical range of activations, so it can choose scales that minimize quantization error for real inputs.

## PTQ Algorithms

### GPTQ (GPT Quantization)

The gold standard for INT4 weight quantization.

**Analogy:** Imagine you're packing a suitcase and need to fit bulky items into smaller bags. Naive packing just squishes everything—some items get damaged. GPTQ is like a skilled packer who, after compressing one item, slightly rearranges the nearby items to compensate for the space change and keep everything balanced.

**How it works:**
- Quantizes weights one layer at a time
- Uses Hessian information to identify which weights matter most
- Compensates for quantization error by adjusting remaining weights
- Processes in blocks for efficiency

**Best for:** INT4 quantization where accuracy is critical

### AWQ (Activation-aware Weight Quantization)

Faster than GPTQ with slightly less accuracy. Won the MLSys 2024 Best Paper Award.

**Analogy:** Imagine printing a photograph of a landscape and sunset. If you use the same exposure for the whole image, you'll either blow out the sun (too bright) or lose the landscape (too dark). AWQ identifies the "bright spots"—the channels with high activations—and gives them special treatment, scaling them to preserve detail where it matters most.

**How it works:**
- Identifies "salient" weight channels based on activation magnitudes
- Protects important weights by scaling them up before quantization
- Scales activations down to compensate
- No backpropagation or reconstruction required (unlike GPTQ)

**Best for:** Fast quantization when time matters more than squeezing out the last bit of accuracy

### SmoothQuant

Enables INT8 quantization of both weights *and* activations.

**The problem:** Activations have outliers that ruin quantization. Weights are smooth and easy to quantize.

**Analogy:** Imagine two people on a seesaw—one is very heavy (hard-to-quantize activations with outliers), one is light (easy-to-quantize weights). SmoothQuant transfers some "weight" from the heavy person to the light one, balancing the seesaw so both can be handled equally.

**How it works:**
- Mathematically migrates the quantization difficulty from activations to weights
- Multiplies activations by a smoothing factor (making them easier to quantize)
- Divides weights by the same factor (they can handle it)

**Best for:** W8A8 quantization for maximum inference speedup on INT8-optimized hardware

### SparseGPT

Combines pruning with quantization for maximum compression.

**Analogy:** Like editing a novel—first you remove redundant paragraphs entirely (pruning to zero), then you compress what remains. SparseGPT identifies which "sentences" (weights) can be deleted without changing the story's meaning, then compresses the rest.

**How it works:**
- Prunes unimportant weights to zero (sparsity)
- Uses similar error compensation to GPTQ
- Can be combined with quantization: sparse + quantized

**Best for:** Extreme compression when you need both sparsity and quantization

## Which Algorithm to Choose?

| Scenario | Recommended | Why |
|----------|-------------|-----|
| Maximum accuracy | GPTQ with group_size=128 | Best error compensation |
| Fast quantization | AWQ | Simpler algorithm, good results |
| INT8 weights+activations | SmoothQuant | Only option for W8A8 |
| Maximum compression | SparseGPT + GPTQ | Sparsity + quantization |
| Production deployment | GPTQ or AWQ | Well-tested, vLLM support |

## Hands-On: Quantizing a Model with LLM-Compressor

Open notebook: `experiments/9-model-optimization/1-intro-llm-compressor.ipynb`

In this exercise, you'll use llm-compressor to quantize a small model on CPU.

Follow the instructions in the notebook to:

1. **Understand the oneshot API** - Learn llm-compressor's main interface for quantization

2. **Configure a quantization recipe** - Use `GPTQModifier` with parameters like `scheme`, `targets`, and `ignore`

3. **Run quantization** - Quantize `Qwen/Qwen2-0.5B-Instruct` with W8A8 scheme

4. **Compare file sizes** - See how much smaller the quantized model is

## 🎯 Next Steps

Continue to **[Advanced Quantization](./3-advanced-quantization.md)** to analyze different recipes and formats.
