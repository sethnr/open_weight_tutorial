####################################
# 2. CHOOSE A MODEL AND A MACHINE
####################################

Part 1 used one small model so that the basic process was easy to follow. In
practice, the model you choose affects answer quality, memory, speed, context
length, and the GPU machine you need.

####################################
# START WITH THE MODEL PAGE
####################################

Models are downloaded from [Hugging Face](https://huggingface.co/). A model
page normally tells you:

- what the model is designed to do;
- how many parameters it has;
- what sort of input it accepts;
- its context length;
- its licence;
- how much memory it may require;
- how to use it with Transformers.

Do not choose a model from its name alone. Read the model card and check that
the model is an instruct or chat model if you want to give it ordinary
questions and instructions.

####################################
# FOUR EXAMPLES
####################################

## Qwen: medium general-purpose model

[Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) is a
general-purpose instruct model with approximately 14 billion parameters. In
FP16, its weights require roughly 30 GB before runtime overhead. It is expected
to fail on the 24 GB interactive GPU, but should run on a 40 GB A100 for a
short prompt.

This is the practical example of choosing a machine with enough GPU memory.
Participants do not need to download it before the demonstration.

## Gemma: a general-purpose model family

[Gemma](https://huggingface.co/google) is a family of open-weight models from
Google. The family includes models of different sizes and capabilities, so the
exact model page must be checked before choosing a machine. Gemma is a useful
example of a model family rather than one single model.

## MedGemma: a specialist multimodal model

[MedGemma 4B IT](https://huggingface.co/google/medgemma-4b-it) is a medical
multimodal model that can work with medical text and images. It is an example
of choosing a model for a specialist application rather than choosing only by
parameter count.

We will discuss MedGemma but will not run it in this tutorial. It requires a
different processor and model class from the simple text-only wrapper, and its
Hugging Face access terms must be accepted before downloading it.

## Muse Glimmer: a very large multimodal model

[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) is a
large multimodal model designed for general, reasoning, coding, and agentic
tasks. It has approximately 30 billion parameters, plus a perception encoder.
The full-precision version is an example of a model requiring a high-memory
GPU; an 80 GB A100 is a reasonable machine for a short demonstration, while
quantised versions target smaller machines.

We will discuss Muse Glimmer but will not ask participants to download or run
it. It requires a different multimodal wrapper and would be a very large
download.

####################################
# WHAT TO COMPARE
####################################

When comparing candidate models, look at:

- parameter count and weight format;
- context length;
- instruct versus base training;
- language and task coverage;
- text-only or multimodal input;
- licence and permitted use;
- expected GPU memory;
- Transformers support and required software versions.

The smallest model is not automatically the best choice. A smaller model may
be faster and cheaper to run, but it may provide weaker answers. A larger model
may be more capable, but it may need a larger GPU and take longer to load and
generate text. A specialist or multimodal model may be the right choice even
when a general-purpose model is smaller.

The next section will connect these model characteristics to the BMRC machines
available for running them.
