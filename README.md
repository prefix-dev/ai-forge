# AI examples for [pixi](https://pixi.sh)

This repository contains local AI examples and the rattler-build recipes used by
some of them. Pixi provides packages from conda-forge, reproducible
environments, and a small task runner.

## Installation

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

## DeepSeek

Run a quantized DeepSeek reasoning model locally with `llama.cpp`:

```bash
cd deepseek
pixi run start
# Or ask a one-shot question:
pixi run start "Explain quicksort in simple terms."
```

The first run downloads the 1.1 GB
`DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M` model. See
[`deepseek/README.md`](deepseek/README.md) for model customization.

## Whisper

Whisper performs speech-to-text. To start live transcription:

```bash
cd whisper
pixi run start
```

To transcribe a file:

```bash
pixi run convert myfile.mp3
pixi run transcribe -f output.wav
```

## Llama.cpp

The `llama` environment runs the packaged LLaVA model:

```bash
cd llama
pixi run start
```

## ResNet

Run image classification with a pretrained ResNet model:

```bash
cd resnet
pixi run detect horse.jpg
```

## Building recipes

```bash
cd recipes
pixi run rattler-build build --recipe-dir . -c conda-forge
```
