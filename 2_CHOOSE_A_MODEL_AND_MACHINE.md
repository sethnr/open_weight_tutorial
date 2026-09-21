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

Choose a GPU with more memory than the model's raw weight estimate. The
following examples use machines available on the GPRU cluster.

| Machine | GPU memory | Models that should fit | Typical use |
|---|---:|---|---|
| `gpu_interactive` | 24 GB | SmolLM2-1.7B, Gemma 3 4B, MedGemma 4B, Qwen2.5-3B | Small models and short text prompts |
| `gpu_a100_40gb` | 40 GB | All of the above, plus Qwen2.5-14B | Medium models with limited context |
| `gpu_a100_80gb` | 80 GB | All of the above, plus Qwen2.5-32B and Muse Glimmer 30B | Large models and longer prompts |
| `gpu_gh200_144gb` | 144 GB | Models up to roughly 70B, depending on precision and context | Very large models; not enough for Mistral Small 4 in BF16 |

These are approximate choices for one model, one user, and a short prompt. A
model that fits by weight size may still need more memory for long documents,
long responses, images, or multiple requests.

Automatic CPU offloading may allow a model to load when it does not fit fully
on the GPU, but moving data between GPU and system RAM can make generation
extremely slow. For a clear demonstration, choose a machine where the model
fits entirely on the GPU.

Mistral Small 4 has 119B total parameters. In BF16 its raw weight estimate is
approximately 238 GB, so it requires multiple GPUs and a serving system such
as vLLM rather than the simple wrapper used in this tutorial.

Automatic CPU offloading may allow a model to load when it does not fit fully
on the GPU, but moving data between GPU and system RAM can make generation
extremely slow. For a clear demonstration, choose a machine where the model
fits entirely on the GPU.
