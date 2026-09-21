#!/usr/bin/env python3

import argparse
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
parser.add_argument("--prompt", required=True)
parser.add_argument("--temperature", type=float, default=0.0)
parser.add_argument("--runs", type=int, default=1)
args = parser.parse_args()

prompt_path = Path(args.prompt)
if prompt_path.is_file():
    prompt = prompt_path.read_text(encoding="utf-8")
else:
    prompt = args.prompt

############################
# CHECK CUDA AND LOAD MODEL
############################

try:
    # CHECK THAT A CUDA GPU IS AVAILABLE
    if not torch.cuda.is_available():
        raise RuntimeError("No CUDA GPU is available")
    else:
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(
            f"GPU memory: "
            f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB"
        )

    # Mapping the whole model to CUDA prevents automatic CPU offloading.
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.float16,
        device_map={"": "cuda:0"},
        low_cpu_mem_usage=True,
    )
    model.eval()

    device_map = getattr(model, "hf_device_map", None)
    if device_map:
        print(f"Model device map: {device_map}")
    else:
        print(f"Model device: {next(model.parameters()).device}")

except torch.cuda.OutOfMemoryError:
    print("The model is too large for the available GPU memory.")
    raise SystemExit(1)

########################################
# SUBMIT PROMPT AND PRINT THE RESPONSE
########################################

tokenizer = AutoTokenizer.from_pretrained(args.model)

inputs = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to("cuda")

for run in range(args.runs):
    settings = {
        "max_new_tokens": 200,
        "pad_token_id": tokenizer.eos_token_id,
    }

    if args.temperature == 0:
        settings["do_sample"] = False
    else:
        settings.update(
            do_sample=True,
            temperature=args.temperature,
            top_p=0.95,
        )

    with torch.inference_mode():
        output = model.generate(**inputs, **settings)

    new_tokens = output[0, inputs["input_ids"].shape[1] :]
    response = tokenizer.decode(new_tokens, skip_special_tokens=True)

    print(f"\n--- Response {run + 1} ---")
    print(response)
