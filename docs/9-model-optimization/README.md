# Module 9 - Model Optimization

> Running the smartest AI means nothing if it's too slow or expensive to deploy. Model optimization transforms powerful but heavy LLMs into lean, efficient engines ⚡

# 🧑‍🍳 Module Intro

This module covers model quantization and optimization for production GenAI applications. You'll learn how to compress LLMs, evaluate trade-offs, and deploy optimized models through your GenAIOps pipeline.

**Key Question:** *Which quantization method should I choose for my use case?*

# 🖼️ Big Picture
<!-- TODO: Add architecture diagram showing quantization workflow -->
![big-picture-quantization.jpg](images/big-picture-quantization.jpg)

# 🔮 Learning Outcomes

* Understand quantization and precision formats (FP32 → FP16 → FP8 → INT8 → INT4)
* Examine llm-compressor configurations and quantization recipes
* Analyze trade-offs between PTQ algorithms (GPTQ, AWQ, SmoothQuant)
* Integrate quantized models into your GenAIOps deployment pipeline
* Evaluate quantized models using lm-evaluation-harness

# 🔨 Tools used in this module

* **llm-compressor**: Quantization toolkit from the vLLM project
* **lm-evaluation-harness**: Benchmarking framework for LLM accuracy
* **GuideLLM**: Performance testing (TTFT, ITL, throughput)
* **vLLM/KServe**: Model serving infrastructure
* **Argo CD**: GitOps deployment for model promotion
