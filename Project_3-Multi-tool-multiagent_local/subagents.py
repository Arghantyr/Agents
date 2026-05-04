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

from google.adk.agents import LlmAgent
from tools import get_memory_usage
from google.adk.models.lite_llm import LiteLlm

memory_manager = LlmAgent(
    name="MemoryManager",
    model=LiteLlm(model="ollama_chat/functiongemma"),
    description=(
        "Subagent specializing in function calls related to memory management."
    ),
    instruction=(
        "You are an AI subagent equipped with memory management tools. Assist the supervising agent in their requests."
    ),
    tools=[get_memory_usage],
    output_key='memory_manager_results'
)
