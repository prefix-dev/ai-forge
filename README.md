# A few AI examples for [pixi](pixi.sh) 

All of these examples use `pixi` - our new package manager.
Pixi is based on the (vast) conda & conda-forge ecosystem.

Pixi also comes with lockfiles and a little workflow / task running system (similar to `taskfile` or `make`). That makes it very easy to run these examples.

## Installation

To install `pixi`, run the following command:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

## Whisper

Whisper does text-to-speech. To run it locally, just navigate to the `whisper` directory and run:

```bash
pixi run start  # live transcription using base-en
```

Or if you want to transscribe a file:

```bash
pixi run convert myfile.mp3  # convert the file from any audio format to `output.wav` using ffmpeg
# then
pixi run transcribe -f output.wav  # transcribe the file using base-en
```

## Llama.cpp 

Follows ...

## Resnet

Follows ... 