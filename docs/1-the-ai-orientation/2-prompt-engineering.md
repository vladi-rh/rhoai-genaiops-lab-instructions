# 🧠 What is Prompt Engineering?

<div class="terminal-curl"></div>

Prompt engineering is the practice of designing effective inputs (prompts) to elicit useful, relevant, and accurate outputs from a language model.

You can think of it like writing instructions for a very smart but very literal assistant. The way you phrase a prompt can drastically affect the tone, format, depth, or even the correctness of the model’s response.

There are typically two key parts to prompting:

* **System Prompt**: This sets the context or behavior for the model. It defines *how* the model should act (e.g., “You are a helpful teaching assistant for computer science students.”).
* **User Prompt**: This is the actual question or task you’re giving to the model (e.g., “Explain recursion to a beginner.”).

Together, they guide the model’s behavior and shape its response.

## 🎯 Why Prompt Engineering Matters for RDU’s Canopy AI

At Redwood Digital University, we’re building **Canopy AI**, a platform designed to adapt to diverse student needs and teaching styles. That means our LLMs must be **fine-tuned not just at the model level—but also at the prompt level.**

With effective prompts, we can:

* Make content more accessible for different learning levels.
* Generate study guides, quiz questions, summaries, or personalized feedback.
* Help educators save time while maintaining quality and consistency.

But before we can trust an AI to assist learners, we need to explore how it behaves under different prompting conditions.


## 🧪 Hands-On: The Prompt Playground

We’ve created a **Gradio-based interface** where you can experiment with different prompting strategies.

Here’s what you can configure:

* 🔗 **Model Endpoint**: Connect to your chosen LLM (local or remote).
* 🧾 **System Prompt**: Set the model’s “persona” or behavior.
* 💬 **User Prompt**: Ask a question, give a command, or provide input.
* 🔢 **Max Tokens**: Control the length of the model’s output.
* 🔥 **Temperature**: Adjust creativity vs. precision. Lower = more focused, Higher = more creative.



Use the Prompt Playground to:

* Compare how different **system prompts** change the behavior of the same model.
* Adjust **temperature** and **max tokens** to explore how output varies.
* Decide on a system prompt template that will work well for **Canopy AI’s learning assistant** in future modules.

📌 **Tip**: Try changing the tone, specificity, or format of your system prompt to see how much it shapes the output. Don’t be afraid to get creative!


<!-- # "https://gradio-app.ai501.<CLUSTER_DOMAIN>" -->
<iframe 
  src="http://0.0.0.0:7860"  
  width="100%" 
  height="600px" 
  frameborder="0"
  style="border: 1px solid #ddd; border-radius: 8px;">
</iframe>

