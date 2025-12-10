# 🧮 Understanding Quantization

You've got a shiny 7B parameter model that answers student questions beautifully. There's just one problem: it needs 14GB of GPU memory, and your deployment budget says "absolutely not."

Welcome to quantization—the art of making models smaller without making them dumber.

Think of it like compression for your model's brain. Instead of storing every weight as a precise 16-bit number, we round them to 8 or even 4 bits. It's like the difference between keeping exact change ($14.37) versus rounding to the nearest dollar ($14). You lose some precision, but your wallet gets a lot lighter.

For Canopy, this means we can serve more students with the same hardware, respond faster, and maybe even run on that "spare" GPU that IT forgot about.

## Why Should You Care?

| Benefit | What It Means for You |
|---------|----------------------|
| **Memory** | That 14GB model? Now it's 3.5GB. Hello, cheaper GPUs! |
| **Speed** | Smaller numbers = faster math = snappier responses |
| **Cost** | Fit more models on fewer GPUs = happy finance team |
| **Accuracy** | The catch: you might lose some quality (but less than you'd think) |

The question isn't *whether* to quantize—it's *how much* you can get away with before students start noticing.

## The Precision Menu

Think of precision formats like coffee sizes—you pick based on what you actually need:

| Format | Bits | Memory vs FP32 | When to Use It |
|--------|------|----------------|----------------|
| FP32 | 32 | 100% | Training (you need all the precision) |
| FP16/BF16 | 16 | 50% | Standard inference (the default choice) |
| FP8 | 8 | 25% | Fancy new GPUs (H100, MI300) |
| INT8 | 8 | 25% | Solid quantization (safe bet) |
| INT4 | 4 | 12.5% | Aggressive compression (living dangerously) |

Most production deployments land somewhere between INT8 and INT4. Let's understand what we're actually compressing.

## What Can Be Quantized?

An LLM has three things we can squeeze down, each with its own risk/reward:

### 1. Weight Quantization (The Easy One)
The model's learned parameters—billions of numbers that encode everything the model knows. These are static, predictable, and *love* being quantized.

- **Most common and safest** approach
- Do it once, save forever
- Example: W8A16 means 8-bit weights, 16-bit activations

### 2. Activation Quantization (The Tricky One)
The values that flow through the model during inference. They're dynamic, unpredictable, and occasionally throw tantrums (outliers).

- **More challenging**—activations can spike unexpectedly
- Requires calibration data to get right
- Example: W8A8 means both weights AND activations are quantized

### 3. KV Cache Quantization (The Memory Hog)
When students write essays or ask follow-up questions, the model stores attention state. For long conversations, this cache can eat more memory than the model itself.

- Particularly useful for chatbots (like Canopy!)
- Reduces memory for long conversations
- Often overlooked, but can be a game-changer

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

## When Things Go Wrong

Quantization isn't magic—sometimes it breaks things. Here are the usual suspects:

### The Outlier Problem

Imagine you're grading on a curve, and one student scores 10,000%. Now everyone else looks like they got zero. That's what outlier activations do to quantization.

```
Normal activations: [-1.0, 0.5, -0.3, 0.8, ...]
That one outlier:       [..., 127.5, ...]  ← Ruins everything!
```

**How we fix it:**
- **SmoothQuant**: Redistribute the problem from activations to weights
- **AWQ**: Protect the channels that matter most
- **Mixed precision**: Let the troublemakers stay in FP16

### Saturation (The Clipping Problem)

When values exceed what our format can represent, they get clipped. It's like trying to fit a giraffe in a phone booth.

```
INT8 can hold: [-128, 127]
Your value:    150 → gets squished to 127 (oops)
```

**How we fix it:**
- Calibrate with data that looks like real usage
- Pick scales that minimize clipping
- Use finer granularity (smaller groups)

## The Decision Tree

Not sure what to pick? Here's the cheat sheet:

| Your Situation | Go With |
|----------------|---------|
| "I need accuracy, size can wait" | INT8 (W8A16) |
| "Balance is key" | INT4 with g128 |
| "Squeeze it till it screams" | INT4 with g64 |
| "Students write novels" | Add KV cache quantization |

## 🎯 Ready to Actually Do This?

Enough theory—let's compress some models!

Continue to **[LLM-Compressor](./2-llm-compressor.md)** to get hands-on with quantization tools and see these concepts in action.
