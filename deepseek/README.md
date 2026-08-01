# DeepSeek

This example runs the 4-bit `DeepSeek-R1-Distill-Qwen-1.5B` model locally with
`llama.cpp`. The first run downloads approximately 1.1 GB from Hugging Face.

Start an interactive conversation:

```bash
pixi run start
```

Or pass a one-shot prompt:

```bash
pixi run start "Explain why the sky is blue in three sentences."
```

To try another DeepSeek GGUF model, change `REPOSITORY`, `REVISION`, and
`FILENAME` in `download_model.py`. Larger models need substantially more RAM.
