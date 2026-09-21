####################################
# 2. CHOOSE A MODEL AND A MACHINE
####################################

There are many open-weight models. They can be compared on
[Hugging Face](https://huggingface.co/), where each model page gives
information about its purpose, size, input types, context length, licence, and
recommended software.

####################################
# MODEL DATA TYPES AND MEMORY
####################################

The model page may give the number of parameters and the data type used by the
weight files. The number of bytes used for each parameter depends on the data
type:

| Data type | Bits per parameter | Bytes per parameter |
|---|---:|---:|
| FP32 | 32 | 4 |
| FP16/BF16 | 16 | 2 |
| INT8 | 8 | 1 |
| 4-bit | 4 | 0.5 |

Start with this calculation:

```text
weight memory = number of parameters × bytes per parameter
```

Then allow approximately 20–25% extra for CUDA, the framework, temporary
tensors, and the KV cache:

```text
required GPU memory ≈ weight memory × 1.25
```

This is an estimate, not a guarantee. Long prompts, long responses, images,
and multiple simultaneous requests require more memory.

####################################
# EXAMPLE 1: QWEN
####################################

[Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) is a
general-purpose instruct model with approximately 14.7 billion parameters.

```text
14.7B parameters × 2 bytes for FP16
≈ 29.4 GB for the weights

29.4 GB × 1.25
≈ 36.8 GB required
```

This should fail on the 24 GB interactive GPU and should run on a 40 GB A100
with a short text prompt.

####################################
# EXAMPLE 2: GEMMA
####################################

[Gemma 3 4B IT](https://huggingface.co/google/gemma-3-4b-it) is a general-
purpose model from Google. It is approximately 4 billion parameters and uses
16-bit weights in the ordinary full-precision release.

```text
4B parameters × 2 bytes for BF16
≈ 8 GB for the weights

8 GB × 1.25
≈ 10 GB required
```

This should fit comfortably on the 24 GB interactive GPU, assuming a normal
text prompt and modest response length.

####################################
# EXAMPLE 3: MEDGEMMA
####################################

[MedGemma 4B IT](https://huggingface.co/google/medgemma-4b-it) is a specialist
medical model that accepts text and images. Its language component is about 4
billion parameters, with 16-bit weights.

```text
4B parameters × 2 bytes for BF16
≈ 8 GB for the language-model weights

8 GB × 1.25
≈ 10 GB baseline estimate
```

This is not a complete estimate because MedGemma also has a vision encoder and
image-processing components. It should fit on a 24 GB GPU for modest inputs,
but images and long contexts can require additional memory. We discuss this
model but do not run it in this tutorial.

####################################
# EXAMPLE 4: MUSE GLIMMER
####################################

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) is a
large multimodal model designed for general, reasoning, coding, and agentic
tasks. It has approximately 30 billion parameters, including a perception
encoder, and its full-precision weights are BF16.

```text
30B parameters × 2 bytes for BF16
≈ 60 GB for the weights

60 GB × 1.25
≈ 75 GB required
```

An 80 GB A100 is therefore the appropriate machine for a short full-precision
demonstration. Quantised versions require less memory, but are a different
deployment choice. We discuss Muse Glimmer but do not run it in this tutorial.

####################################
# WHAT TO COMPARE
####################################

When comparing candidate models on Hugging Face, look at:

- parameter count and weight data type;
- context length;
- instruct versus base training;
- language and task coverage;
- text-only or multimodal input;
- licence and permitted use;
- Transformers support and required software versions.

####################################
# CHOOSE A MACHINE
####################################

Choose a GPU with more memory than the estimated requirement. The estimate
must leave headroom for the prompt, generated response, framework overhead,
temporary tensors, and the KV cache.

For a short, single-user text-generation exercise, 20–25% headroom may be
adequate. Use more headroom for long documents, long responses, images, or
multiple requests. A model that technically fits may still be too slow or
unstable if the GPU is nearly full.

If a model does not fit, automatic CPU offloading may allow it to load, but
generation can become extremely slow. For a clear demonstration, it is better
to choose a machine where the model fits entirely on the GPU.

####################################
# MULTIMODALITY
####################################

Text-only models receive text and produce text. Multimodal models can receive
more than one kind of input, such as text and images.

Multimodal models need additional memory for components such as image or audio
encoders. Their model pages may also specify different software classes and
processors. Parameter count alone is therefore not enough to estimate their
complete memory requirement.

A PDF converted to text is still a text-only input. Supplying PDF pages as
images is a multimodal task.
