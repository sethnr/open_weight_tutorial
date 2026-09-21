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

The number of bytes used for each parameter depends on the model's data type:

| Data type | Bits per parameter | Bytes per parameter |
|---|---:|---:|
| FP32 | 32 | 4 |
| FP16/BF16 | 16 | 2 |
| INT8 | 8 | 1 |
| 4-bit | 4 | 0.5 |

Start with:

weight memory = number of parameters × bytes per parameter

For example:

14.7B parameters @ FP16 ==> 14.7 × 2 ≈ 29.4 GB

This is the raw weight estimate. The machine also needs memory for CUDA, the
framework, temporary tensors, the prompt, the generated response, and the KV
cache.

####################################
# MODELS
####################################

## 1: QWEN

[Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)
is a medium-sized general-purpose instruct model.

14.7B parameters @ FP16 ==> 14.7 × 2 ≈ 29.4 GB

## 2: GEMMA

[Gemma 3 4B IT](https://huggingface.co/google/gemma-3-4b-it) is a general-
purpose model family from Google.

4B parameters @ BF16 ==> 4 × 2 ≈ 8 GB

## 3: MEDGEMMA

[MedGemma 4B IT](https://huggingface.co/google/medgemma-4b-it) is a specialist
medical model that accepts text and images.

4B parameters @ BF16 ==> 4 × 2 ≈ 8 GB

This is only the language-model estimate. The vision encoder and image-
processing components require additional memory. We discuss MedGemma but do not
run it in this tutorial.

## 4: MUSE GLIMMER

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) is a
large multimodal model for general, reasoning, coding, and agentic tasks.

30B parameters @ BF16 ==> 30 × 2 ≈ 60 GB

This includes a perception encoder in the total model. We discuss Muse Glimmer
but do not run it in this tutorial.

####################################
# CHOOSE A MACHINE
####################################

Choose a GPU with more memory than the raw weight estimate. As a rule of thumb,
allow 20–25% headroom for a short, single-user text-generation exercise:

required GPU memory ≈ weight memory × 1.25

Use more headroom for long documents, long responses, images, or multiple
requests. A model that technically fits may still be too slow or unstable if
the GPU is nearly full.

Examples using the BMRC machines:

- **Gemma 3 4B (8 GB)** → `gpu_interactive` (24 GB); roughly 16 GB headroom
  for runtime allocations and context.
- **MedGemma 4B (8 GB baseline)** → `gpu_interactive` (24 GB) for modest
  inputs; additional headroom is needed for images.
- **Qwen2.5-14B (29.4 GB)** → `gpu_a100_40gb`; roughly 10 GB remains before
  other runtime needs, so use short prompts and outputs.
- **Muse Glimmer 30B (60 GB)** → `gpu_a100_80gb`; roughly 20 GB remains,
  although its multimodal components and long contexts need more care.
- **Mistral Small 4 119B (238 GB in BF16)** → no single GPU in the basic BMRC
  list; it requires multiple GPUs and a serving system such as vLLM.

Automatic CPU offloading may allow a model to load when it does not fit fully
on the GPU, but moving data between GPU and system RAM can make generation
extremely slow. For a clear demonstration, choose a machine where the model
fits entirely on the GPU.
