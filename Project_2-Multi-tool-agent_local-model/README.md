# About
This repo serves as a playground for testing AI agent systems.

# Getting started
## (Optional) Create (and navigate to) a new directory
```bash
mkdir Test
cd Test
```

## Clone this repository
### Using SSH
```bash
gh repo clone git@github.com:Arghantyr/Agents.git
```

or

```bash
gh repo clone Arghantyr/Agents
```

### Using HTTPS
```bash
git clone https://github.com/Arghantyr/Agents.git
```

## Navigate to a Project of choice
```bash
cd ./Agents/{Project of choice...}
```

## Create (and activate) a new virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Pip install dependencies from the 'requirements.txt'
```bash
pip install -r requirements.txt
```

## Create a '.env' environment file for your Google API key
```bash
touch .env
echo 'GOOGLE_API_KEY="<Your Google API Key>"' > .env
```
Google API keys are generated per project in Google AI Studio (verified on 2026.04.04).

## Install ollama service to manage local models
```bash
sudo /bin/bash install_dependencies.sh
```

## Pull Qwen2.5 model from ollama servers
```bash
ollama pull qwen2.5
```

## Run the agent project using 'adk run'
Example: for "Project\_2-Multi-tool-agent\_local-model" this is "multi\_tool\_agent"
```bash
adk run multi_tool_agent
```
That's it! You're good to go!


# Changelog
- 2026.05.01  Project 2 begins. Local model served with Ollama and LiteLLM.

# Projects
1. Project 2: Multi-tool agent (local model, downloaded from web)

# Examples
## Memory usage
```python
[user]: Hello.
22:56:25 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
[helpful_agent]: Hello! How can I assist you today?
[user]: I want to perform some work on this system. How can you assist me with that?
22:56:31 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
[helpful_agent]: Of course! To better assist you, could you please provide more details about the tasks you plan to perform? For example, are you looking to optimize performance, manage memory usage, or execute a specific program or script?
[user]: Yes, use available tools to fetch the memory stats.
22:57:22 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
22:57:26 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
[helpful_agent]: Here are the current memory statistics for this system:

- **Total Memory**: 15.8 GB
- **Available Memory**: 9.74 GB
- **Used Memory**: 6.01 GB (36.2%)
- **Free Memory**: 5.62 GB
- **Active Memory**: 16 MB
- **Inactive Memory**: 9.55 GB
- **Buffers**: 21.87 MB
- **Cached Memory**: 4.73 GB
- **Shared Memory**: 0.35 MB
- **Slab Kernel Memory**: 93.59 MB

Would you like to proceed with any specific task based on this information?
[user]: exit
```
