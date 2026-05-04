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

## Install ollama service to manage local models
```bash
sudo /bin/bash install_dependencies.sh
```

## Run the agent project using 'adk run'
Example: for "Project\_3-Multi-tool-multiagent\_local" this is "multi\_tool\_multiagent"
```bash
adk run multi_tool_multiagent
```
That's it! You're good to go!


# Changelog
- 2026.05.04  Project 3 begins. Local model served with Ollama and LiteLLM using a tool-using local subagent.

# Projects
1. Project 3: Multi-tool multi-agent (local models, tool-using subagent)

# Examples
## Memory usage
```python
[user]: Hello. Who are you?
21:00:49 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
[helpful_agent]: I am helpful_agent, an agent designed to answer your questions. How can I assist you today?
[user]: What are your capabilities, i.e.: what tools and subagents can you use?
21:02:04 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
[helpful_agent]: I can use various tools and subagents when needed. For instance, if you have a question related to memory management, I would transfer it to MemoryManager. Currently, the available tool for me to use is the `MemoryManager` subagent. Is there something specific you'd like to know or ask about?
[user]: Show me current memory usage stats in GB and rounding up the results to 2 decimal places.
21:04:12 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= qwen2.5; provider = ollama_chat
21:04:18 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= functiongemma; provider = ollama_chat
21:04:21 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= functiongemma; provider = ollama_chat
[user]: Show me current memory stats.
21:04:36 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= functiongemma; provider = ollama_chat
21:04:36 - LiteLLM:INFO: utils.py:3995 -
LiteLLM completion() model= functiongemma; provider = ollama_chat
[MemoryManager]: I have retrieved the current memory statistics.

Here are the details:
- Total memory: 16613863424
- Available memory: 9646624768
- Used memory: 6967238656
- Free memory: 4559265792
- Active memory: 5160665088
- Inactive memory: 6462599168
- Buffers: 6807552
- Slab memory: 177807360

I also apologize, but could not retrieve the current memory usage statistics. The tool I used to access this information could not provide the requested data.
[user]: exit
```
