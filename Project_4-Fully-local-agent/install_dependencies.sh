#!/bin/bash

apt-get install zstd

curl -fsSL https://ollama.com/install.sh | sh

ollama create -f models/modelfiles/qwen2.5-gguf.modelfile qwen2.5-gguf
