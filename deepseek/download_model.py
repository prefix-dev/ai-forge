"""Download the small, quantized DeepSeek model used by this example."""

from pathlib import Path

from huggingface_hub import hf_hub_download

REPOSITORY = "bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF"
REVISION = "9cc28b17e86fa2415fcb070f8ee5ec27c965aa61"
FILENAME = "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf"

path = hf_hub_download(
    repo_id=REPOSITORY,
    revision=REVISION,
    filename=FILENAME,
    local_dir=Path(__file__).parent / "models",
)
print(f"Model ready at {path}")
