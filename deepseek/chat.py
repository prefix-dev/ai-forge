"""Start an interactive DeepSeek chat, or answer a prompt passed on the command line."""

import subprocess
import sys
from pathlib import Path

MODEL = Path(__file__).parent / "models" / "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf"

command = ["llama-cli", "--model", str(MODEL), "--conversation"]
if len(sys.argv) > 1:
    command.extend(["--prompt", " ".join(sys.argv[1:])])

raise SystemExit(subprocess.call(command))
