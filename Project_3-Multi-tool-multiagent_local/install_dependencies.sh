#!/bin/bash

apt-get install zstd

curl -fsSL https://ollama.com/install.sh | sh

ollama pull qwen2.5
ollama pull functiongemma

