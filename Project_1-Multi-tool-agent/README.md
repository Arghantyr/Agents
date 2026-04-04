# About
This repo serves as a playground for testing AI agent systems.

# Changelog
2026.04.04  Add tool 'get\_memory\_usage' to monitor memory-related statistics.
2026.04.04  Project 1 begins. Testing Google's Agent Development Kit.

# Projects
1. Project 1: Multi-tool agent

# Examples
## Memory usage
```python
[user]: Hello
[helpful_agent]: Hello! How can I help you today?
[user]: I want to perform some work on this system. How can you assist me with that?
[helpful_agent]: I can assist you in several ways depending on your needs. Since I have access to a set of system tools, I can help you with tasks like:

*   **System Monitoring:** I can check the system's current state, such as memory usage, to help you understand how your resources are being utilized.
*   **Information Gathering:** I can provide details about the system or help you navigate tasks related to its configuration.

**To get started, you could ask me something like:**
*   "What is the current memory usage of this system?"
*   "Can you help me understand how much memory is available?"

Please let me know what specific work you are looking to perform, and I will do my best to assist you!
[user]: How much memory is currently used?
[helpful_agent]: The system is currently using approximately 636 MB of memory out of the total 16.6 GB available, which means about 3.8% of the memory is in use.
[user]: Can you provide detailed statistics?
[helpful_agent]: Here are the detailed memory statistics for the system:

*   **Total Memory:** 16.61 GB (16,613,867,520 bytes)
*   **Used Memory:** 636.30 MB (636,297,216 bytes)
*   **Available Memory:** 15.98 GB (15,977,570,304 bytes)
*   **Free Memory:** 16.04 GB (16,043,442,176 bytes)
*   **Memory Usage Percentage:** 3.8%
*   **Active Memory:** 54.04 MB
*   **Inactive Memory:** 209.03 MB
*   **Buffers:** 0.62 MB
*   **Cached:** 127.74 MB
*   **Shared Memory:** 3.65 MB
*   **Slab:** 80.46 MB

Let me know if you need any further information!
[user]: exit
```
