## Agentic Frameworks and Llamas

We have now seen how we can build an Agent from scratch.  
Let's use some libraries to make this easier!  
We of course have llamastack that can help by exposing everything over a unified endpoint, but llamastack unfortuantely doesn't have any agentic framework built into it. Luckily for us, there are plenty other agentic frameworks we can leverage and that integrate with llamastack.  
On of the more popular ones are LangGraph, let's see how our previous example would look like using that instead!

The usecase we are implementing is: a knowledge-based chatbot which will schedule meetings with specific professors if it can't find the knowledge itself.

### Enable MCP in LlamaStack

1. Go to OpenShift Console -> Helm -> Releases

2. For `llama-stack-operator-instance` click on the three dots on the rightmost side and select Upgrade

3. Open up the MCP section, select `enabled` and click Upgrade

### Try it out

Now that you have everything enabled, let's see how it looks like:

1. Go through notebook `experiments/8-agents/4-agentic-llamas.ipynb`.