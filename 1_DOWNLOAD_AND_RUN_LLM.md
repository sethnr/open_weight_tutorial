############################
# 1. DOWNLOAD AND RUN LLM
############################

This tutorial uses one small model throughout:

```text
HuggingFaceTB/SmolLM2-1.7B-Instruct
```

We are downloading it from [Hugging Face](https://huggingface.co/), a
repository of open-weight models. See the [SmolLM2-1.7B-Instruct model
page](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) for its
description and technical details.

########################
# DOWNLOAD THE MODEL
########################

Download the model from Hugging Face:

Create a local models directory:

```bash
mkdir -p models
hf download HuggingFaceTB/SmolLM2-1.7B-Instruct \
  --local-dir ./models/SmolLM2-1.7B-Instruct
```

########################
# RUN THE MODEL
########################

Send the model a prompt:

```bash
python run_model.py \
  --model ./models/SmolLM2-1.7B-Instruct \
  --prompt "Mary had a little lamb. What color was its fleece?"
```

The wrapper reports the GPU, loads the model, and prints its response.

Try changing the prompt:

```bash
python run_model.py \
  --model ./models/SmolLM2-1.7B-Instruct \
  --prompt "Explain in three sentences why a lamb might be kept as a household pet."
```

########################
# INTRODUCE TEMPERATURE
########################

Run the same prompt three times with temperature `0`:

```bash
python run_model.py \
  --model ./models/SmolLM2-1.7B-Instruct \
  --temperature 0 \
  --runs 3 \
  --prompt "Give one reason why a lamb might follow someone home."
```

Now run it three times with a higher temperature:

```bash
python run_model.py \
  --model ./models/SmolLM2-1.7B-Instruct \
  --temperature 1.2 \
  --runs 3 \
  --prompt "Give one reason why a lamb might follow someone home."
```

Compare the results. Temperature affects how the model selects its next token;
it does not give the model new knowledge. A higher temperature usually creates
more variation, but can also produce weaker responses.

########################
# RUN OUT OF CONTEXT
########################

The model has a maximum context window. The context contains the prompt and the
response being generated. If the input is too long, the model cannot process it
as one request.

Use the extended wool-industry document as an oversized prompt:

```bash
python run_model.py \
  --model ./models/SmolLM2-1.7B-Instruct \
  --prompt ./british_wool_industry_long_prompt.md
```

The model supports an approximately 8,192-token context. The test document is
much longer than that. Transformers should warn that the input is too long.
Depending on the model and software version, the run may be very slow, fail,
or produce meaningless repetitive output. Do not interpret that output as a
successful answer.

This is a common practical failure mode when a large document, such as a PDF
converted to text, is included in a prompt. The model may still load entirely
onto the GPU while the prompt itself exceeds the usable context window.
