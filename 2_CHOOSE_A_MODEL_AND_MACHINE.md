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

This gives the raw weight estimate. Extra memory for CUDA, the framework,
temporary tensors, and the KV cache is discussed below under machine sizing.

## 1: QWEN

[Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) is a
general-purpose instruct model with approximately 14.7 billion parameters.

14.7B parameters @ FP16 ==> 14.7 × 2 ≈ 29.4 GB

## 2: GEMMA

[Gemma 3 4B IT](https://huggingface.co/google/gemma-3-4b-it) is a general-
purpose model from Google. It is approximately 4 billion parameters and uses
16-bit weights in the ordinary full-precision release.

4B parameters @ BF16 ==> 4 × 2 ≈ 8 GB

## 3: MEDGEMMA

[MedGemma 4B IT](https://huggingface.co/google/medgemma-4b-it) is a specialist
medical model that accepts text and images. Its language component is about 4
billion parameters, with 16-bit weights.

4B parameters @ BF16 ==> 4 × 2 ≈ 8 GB

MedGemma is multimodal: it includes additional components for processing
images. Its complete memory requirement is therefore higher than this simple
language-weight estimate. Multimodality is discussed here because it affects
machine choice.

## 4: MUSE GLIMMER

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) is a
large multimodal model designed for general, reasoning, coding, and agentic
tasks. It has approximately 30 billion parameters, including a perception
encoder, and its full-precision weights are BF16.

30B parameters @ BF16 ==> 30 × 2 ≈ 60 GB

####################################
# CHOOSE A MACHINE
####################################

The GPU must have more memory than the raw weight estimate. Allow headroom for
CUDA, the framework, temporary tensors, the prompt, the generated response,
and the KV cache.

For a short, single-user text-generation exercise, 20–25% headroom may be
adequate:

required GPU memory ≈ weight memory × 1.25

Use more headroom for long documents, long responses, images, or multiple
requests. A model that technically fits may still be too slow or unstable if
the GPU is nearly full.

## Qwen2.5-14B

29.4 GB × 1.25 ≈ 36.8 GB

The 24 GB `gpu_interactive` machine is too small. The 40 GB A100 is the
smallest sensible choice for a short prompt.

## Qwen2.5-32B

32B parameters @ FP16 ==> 32 × 2 ≈ 64 GB; 64 GB × 1.25 ≈ 80 GB

An 80 GB A100 is the appropriate machine for a short demonstration.

## Muse Glimmer 30B

30B parameters @ BF16 ==> 30 × 2 ≈ 60 GB; 60 GB × 1.25 ≈ 75 GB

An 80 GB A100 is a reasonable choice for a short full-precision demonstration.
Images and long contexts require additional headroom. Quantised versions may
fit on smaller GPUs, but that is a different deployment choice.

## Mistral Small 4 119B

Mistral Small 4 is a mixture-of-experts model with 119 billion total
parameters, although only about 6.5 billion are active for each token.

119B parameters @ BF16 ==> 119 × 2 ≈ 238 GB

The inactive experts still have to be stored, so the active-parameter count
does not reduce the weight-memory requirement. This is too large for any
single GPU in the basic BMRC list. It requires multiple GPUs, model
parallelism, and a serving system such as vLLM rather than the simple wrapper.

## CPU offloading

Automatic CPU offloading may allow a model to load when it does not fit fully
on the GPU. However, moving data between GPU and system RAM can make generation
extremely slow. For a clear demonstration, choose a machine where the model
fits entirely on the GPU.
