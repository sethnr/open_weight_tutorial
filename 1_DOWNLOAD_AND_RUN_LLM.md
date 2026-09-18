############################
# 1. DOWNLOAD AND RUN LLM
############################

This tutorial uses one model throughout:

```text
Qwen/Qwen2.5-3B-Instruct
```

########################
# DOWNLOAD THE MODEL
########################

Download the model from Hugging Face:

Model files are large, so do not store them in your home directory. Before
downloading, make sure that `./models` is a directory or symlink pointing to
storage with enough space:

```bash
ls -ld ./models
hf download Qwen/Qwen2.5-3B-Instruct \
  --local-dir ./models/Qwen2.5-3B-Instruct
```

########################
# RUN THE MODEL
########################

Send the model a prompt:

```bash
python run_model.py \
  --model ./models/Qwen2.5-3B-Instruct \
  --prompt "Mary had a little lamb. What color was its fleece?"
```

The wrapper reports the GPU, loads the model, and prints its response.

Try changing the prompt:

```bash
python run_model.py \
  --model ./models/Qwen2.5-3B-Instruct \
  --prompt "Explain in three sentences why a lamb might be kept as a household pet."
```

########################
# INTRODUCE TEMPERATURE
########################

Run the same prompt three times with temperature `0`:

```bash
python run_model.py \
  --model ./models/Qwen2.5-3B-Instruct \
  --temperature 0 \
  --runs 3 \
  --prompt "Give three different imaginative explanations for why a lamb might have followed someone home."
```

Now run it three times with a higher temperature:

```bash
python run_model.py \
  --model ./models/Qwen2.5-3B-Instruct \
  --temperature 1.2 \
  --runs 3 \
  --prompt "Give three different imaginative explanations for why a lamb might have followed someone home."
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

The next exercise will deliberately provide a prompt longer than the model's
available context. We will use the wrapper to test what happens when the
context limit is exceeded and improve its error message if necessary.
