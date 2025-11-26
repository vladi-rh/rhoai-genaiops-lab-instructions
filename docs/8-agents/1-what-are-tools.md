# What are tools?

## Tool basics

LLMs are pretty smart, but they have some awkward limitations. Ask an LLM "What's 847 × 923?" and watch it confidently give you the wrong answer. Or ask it to look up real-time information, interact with databases, or call external APIs - it simply can't.

We've already seen how RAG helps with knowledge limitations by giving LLMs access to documents. Now let's generalize this concept: **tools**.

A **tool** is any service we want the LLM to interact with - calculators, databases, ERP systems, weather APIs, you name it. We wrap these services with a simple communication layer (JSON in/out) that makes it easier for LLMs to format requests.

The LLM becomes a **coordinator** that uses tools and knows how to interpret their results.

This is all very high level, so let's look at some examples!  
Go to your workbench and run through the notebook: **`canopy/8-agents/1-intro-to-tools.ipynb`**

## MCP servers

Now that you've seen how a tool works in practice, let's scale it up!

**MCP (Model Context Protocol) servers** are collections of tools that can be called either remotely or locally. Instead of defining tools one-by-one, MCP servers provide entire suites of functionality - like a toolbox instead of a single tool.

In our case, we already have an MCP server deployed in the namespace AI501 (don't worry, you will get to deploy your own soon).  
Let's connect to it and use its tools!

Open up the notebook: **`canopy/8-agents/2-MCP.ipynb`**