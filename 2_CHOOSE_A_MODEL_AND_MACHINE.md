####################################
# 2. CHOOSE A MODEL AND A MACHINE
####################################

Part 1 used one small model so that the basic process was easy to follow. In
practice, the model you choose affects the answer quality, memory required,
speed, context length, and GPU machine you need.

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
# THREE EXAMPLES
####################################

## SmolLM2

[SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)
is a small instruct model. It is useful for learning because it is quick to
download and run, and its model configuration specifies an approximately
8,192-token context. It is a good choice for simple experiments and for
demonstrating what happens when a document is too long.

## Qwen

[Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) is a
larger instruct model with stronger general-purpose capability than the small
model used in Part 1. It also has a much larger context window, so it may be
able to accept a document that breaks SmolLM2. Its larger weights and longer
possible prompts require more GPU memory.

## Gemma

[Gemma](https://huggingface.co/google) is a family of open-weight models from
Google. The family includes models of different sizes and with different
capabilities. Some Gemma models are text-only; others support additional input
types. Check the exact model page rather than assuming that all Gemma models
behave in the same way.

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
generate text.

The next section will connect these model characteristics to the BMRC machines
available for running them.
