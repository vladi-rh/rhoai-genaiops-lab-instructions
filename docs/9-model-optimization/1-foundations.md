# 🧮 Understanding Quantization

Quantization reduces model size by using fewer bits to represent weights and activations. A 7B parameter model in FP16 needs ~14GB of memory. With INT4 quantization, it needs only ~3.5GB.

## Why Quantization Matters

| Benefit | Impact |
|---------|--------|
| **Memory** | 2-4x reduction in GPU memory |
| **Speed** | Faster inference on compatible hardware |
| **Cost** | Smaller models = cheaper deployment |
| **Accuracy** | Trade-off: potential for quality loss |

The key question isn't *whether* to quantize—it's *which method* to choose for your use case.

## Precision Formats

| Format | Bits | Memory vs FP32 | Use Case |
|--------|------|----------------|----------|
| FP32 | 32 | 100% | Training |
| FP16/BF16 | 16 | 50% | Standard inference |
| FP8 | 8 | 25% | Modern GPU inference (H100, MI300) |
| INT8 | 8 | 25% | Quantized inference |
| INT4 | 4 | 12.5% | Aggressive quantization |

## What Can Be Quantized?

Three components of an LLM can be quantized, each with different trade-offs:

### 1. Weight Quantization
- Model parameters stored in lower precision
- **Most common and safest** approach
- Applied once at quantization time
- Examples: W8A16 (8-bit weights, 16-bit activations)

### 2. Activation Quantization
- Intermediate values during inference
- **More challenging** - activations have outliers
- Requires calibration data
- Examples: W8A8 (both weights and activations quantized)

### 3. KV Cache Quantization
- Attention cache for long-context inference
- Reduces memory for long sequences
- Particularly useful for high-throughput serving

## Quantization Techniques

### Symmetric vs. Asymmetric

Think of it like a thermometer:

- **Symmetric** is like a thermometer centered at 0°C—it measures equally in both directions (-50° to +50°). Great when your data is balanced around zero, like model weights typically are.

- **Asymmetric** is like a thermometer for body temperature (35°C to 42°C)—it has an offset (zero-point) to focus precision where the data actually lives. Better for activations that might all be positive or skewed to one side.

| Approach | Method | Formula | Best For |
|----------|--------|---------|----------|
| **Symmetric** | Scale only | `q = round(x / scale)` | Weights (centered around 0) |
| **Asymmetric** | Scale + zero-point | `q = round(x / scale) + zero_point` | Activations (non-centered) |

**When to use each:**
- Symmetric is simpler and faster
- Asymmetric handles non-zero-centered distributions better
- Most weight quantization uses symmetric
- Activation quantization often needs asymmetric

### Granularity

The granularity determines how many values share a single scale factor:

| Level | Description | Trade-off |
|-------|-------------|-----------|
| **Per-tensor** | One scale for entire tensor | Fastest, least accurate |
| **Per-channel** | One scale per output channel | Good balance |
| **Group (g128, g64)** | One scale per N weights | Most accurate, more overhead |

**Group quantization** (e.g., group_size=128) is the sweet spot for INT4:
- `g128`: Good compression, acceptable accuracy
- `g64`: Better accuracy, slightly larger size
- `g32`: Best accuracy, most overhead

### How Quantization Data is Stored

A quantized model doesn't just store the low-precision weights—it also stores the metadata needed to reconstruct the original values during inference.

**What gets saved:**
- **Quantized weights**: The actual INT4/INT8 values
- **Scales**: One per tensor, channel, or group (depending on granularity)
- **Zero-points**: For asymmetric quantization only
- **Quantization config**: Algorithm used, group size, which layers were quantized

**Example structure** (simplified):
```
model.safetensors
├── model.layers.0.self_attn.q_proj.weight      # INT4 packed weights
├── model.layers.0.self_attn.q_proj.weight_scale # FP16 scales (one per group)
├── model.layers.0.self_attn.q_proj.weight_zp   # Zero-points (if asymmetric)
└── ...
```

**The overhead trade-off:**
- Finer granularity (smaller groups) = more scales to store = larger file
- INT4 with g128 on a 7B model: ~3.5GB weights + ~50MB scales
- INT4 with g64: slightly larger due to 2x more scale values

This is why group size affects both accuracy *and* final model size.

## Common Challenges

### Outlier Activations

A few extremely large activation values force a wide quantization range, wasting precision for normal values.

```
Normal activations: [-1.0, 0.5, -0.3, 0.8, ...]
Outlier:            [..., 127.5, ...]  ← Ruins the scale!
```

**Solutions:**
- SmoothQuant: Shift difficulty from activations to weights
- AWQ: Protect channels with important activations
- Mixed precision: Keep outlier channels in FP16

### Saturation and Clipping

Values outside the quantization range get clipped, losing information:

```
INT8 range: [-128, 127]
Value 150 → clipped to 127 (lost information)
```

**Solutions:**
- Careful calibration with representative data
- Adaptive scale selection
- Group quantization for finer granularity

## Choosing the Right Approach

| Scenario | Recommended |
|----------|-------------|
| Maximum accuracy needed | INT8 (W8A16) |
| Balance accuracy/size | INT4 with g128 |
| Maximum compression | INT4 with g64 or smaller |
| Long context workloads | Add KV cache quantization |

## 🎯 Next Steps

Continue to **[LLM-Compressor](./2-llm-compressor.md)** to learn about PTQ algorithms and how they address these challenges.
