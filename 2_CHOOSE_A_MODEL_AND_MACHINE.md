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

You can calculate the size of each model from the model card - check for the
number of parameters and the model's data type. Multiply the number of
parameters by the number of bytes to get the total model size:

| Data type | Bits per parameter | Bytes per parameter |
|---|---:|---:|
| FP32 | 32 | 4 |
| FP16/BF16 | 16 | 2 |
| INT8 | 8 | 1 |
| 4-bit | 4 | 0.5 |

The calculation is:

weight memory = number of parameters × bytes per parameter

####################################
# MODELS
####################################

## 1: GEMMA

[https://huggingface.co/google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it)

4B parameters @ BF16 ==> 4 × 2 ≈ 8 GB

General-purpose model from Google.

## 2: LLAMA

[https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)

8B parameters @ FP16 ==> 8 × 2 ≈ 16 GB

General-purpose instruct model from Meta.

## 3: QWEN

[https://huggingface.co/Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)

14.7B parameters @ FP16 ==> 14.7 × 2 ≈ 29.4 GB

Medium-sized general-purpose instruct model.

## 4: MEDGEMMA

[https://huggingface.co/google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it)

4B parameters @ BF16 ==> 4 × 2 ≈ 8 GB

Specialist medical model that accepts text and images.

The size estimate is for the language model only. The vision encoder and image-
processing components require additional memory.

## 5: MUSE GLIMMER

[https://huggingface.co/meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)

30B parameters @ BF16 ==> 30 × 2 ≈ 60 GB

Large multimodal model for general, reasoning, coding, and agentic tasks.

The model includes a perception encoder, so the size estimate is not a complete
runtime requirement.

####################################
# CHOOSE A MACHINE
####################################

Choose a GPU with more memory than the raw weight estimate. The following
examples use machines available on the GPRU cluster:

The raw weight estimate is not the complete runtime requirement. The machine
also needs memory for CUDA, the framework, temporary tensors, the prompt, the
generated response, and the KV cache.

| Machine | GPU memory | Models that should fit |
|---|---:|---|
| `gpu_interactive` | 24 GB | SmolLM2-1.7B, Gemma 3 4B, Llama 3.1 8B, MedGemma 4B |
| `gpu_a100_40gb` | 40 GB | The above models, plus Qwen2.5-14B |
| `gpu_a100_80gb` | 80 GB | The above models, plus Qwen2.5-32B and Muse Glimmer 30B |
| `gpu_gh200_144gb` | 144 GB | Larger models, depending on precision and context |

These are approximate choices for one model, one user, and a short prompt.
Long documents, long responses, images, and multiple requests require more
headroom.
