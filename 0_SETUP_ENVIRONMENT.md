########################
# 0. SETUP ENVIRONMENT
########################

Complete this preliminary step before running a model.

########################
# CREATE THE ENVIRONMENT
########################

From the tutorial directory:

```bash
conda env create -f environment.yml
```

If it already exists:

```bash
conda env update -f environment.yml --prune
```

########################
# TEST THE INSTALLATION
########################

Activate the environment and check Python, Hugging Face, and PyTorch:

```bash
conda activate open-model-tutorial
python --version
hf --version
python -c "import torch; print(torch.__version__)"
```

Python should report version 3.11. CUDA is tested after a GPU machine has been
allocated.

########################
# INTERACTIVE GPU MACHINE
########################

Request an interactive session using the BMRC command for the
`gpu_interactive` partition. The exact command depends on the BMRC cluster
configuration.

Once the session starts, activate the environment and check the GPU:

```bash
conda activate open-model-tutorial
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
python -c "import torch; print(f'{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB')"
```

The first command should print `True`. The interactive GPU used for the first
exercise should have approximately 24 GB of memory.
