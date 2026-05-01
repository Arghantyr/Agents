# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from tools import get_memory_usage
from google.adk.models.lite_llm import LiteLlm

MODEL = LiteLlm(model="ollama_chat/qwen2.5")

root_agent = Agent(
    name="helpful_agent",
    model=MODEL,
    description=(
        "Agent to answer user's questions."
    ),
    instruction=(
        "You are an AI assistant equipped with several tools. Assist the user in their requests."
    ),
    tools=[get_memory_usage],
)
