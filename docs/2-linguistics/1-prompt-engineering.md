# 🧠 What is Prompt Engineering?

<div class="terminal-curl"></div>

Prompt engineering is the practice of designing effective inputs (prompts) to elicit useful, relevant, and accurate outputs from a language model.

You can think of it like writing instructions for a very smart but very literal assistant. The way you phrase a prompt can drastically affect the tone, format, depth, or even the correctness of the model’s response.

There are typically two key parts to prompting:

* **System Prompt**: This sets the context or behavior for the model. It defines *how* the model should act (e.g., “You are a helpful teaching assistant for computer science students.”).
* **User Prompt**: This is the actual question or task you’re giving to the model (e.g., “Explain recursion to a beginner.”).

Together, they guide the model’s behavior and shape its response.

## 🎯 Why Prompt Engineering Matters for RDU’s Canopy

At Redwood Digital University, we’re building **Canopy**, a platform designed to adapt to diverse student needs and teaching styles. That means that we not only need a good LLM, but also need to refine our prompts.

With effective prompts, we can:

* Make content more accessible for different learning levels.
* Generate study guides, quiz questions, summaries, or personalized feedback.
* Help educators save time while maintaining quality and consistency.

But before we can trust an AI to assist learners, we need to explore how it behaves under different prompting conditions.


## 🧪 Hands-On: The Prompt Playground

We’ve created a **Gradio-based interface** where you can experiment with different prompting strategies.  
Your goal is to find the **best system prompt** and configuration to **summarize** a given text.

Here’s what you can configure:

* 🔗 **Model Info**: Connect to your chosen LLM (local or remote).
* 🧾 **System Prompt**: Set the model’s “persona” or behavior.
* 💬 **User Prompt**: Ask a question, give a command, or provide input.
* 🔢 **Max Tokens**: Control the length of the model’s output.
* 🔥 **Temperature**: Adjust creativity vs. precision. Lower = more focused, Higher = more creative.

And here is the text you want the model to summarize (i.e. the text you want to send into the User Prompt):

```
Making a cup of tea is easy. First, boil some water. Then, place a tea bag in a cup. Pour the hot water over the tea bag. Let it steep for a few minutes. After that, take out the tea bag. You can add sugar or milk if you like. Now the tea is ready to drink.
```

Use the Prompt Playground to:

* Compare how different **system prompts** change the behavior of the same model.
* Adjust **temperature** and **max tokens** to explore how output varies.
* Decide on a system prompt template that will work well for **Canopy’s learning assistant** in future modules.

📌 **Tip**: Try changing the tone, specificity, or format of your system prompt to see how much it shapes the output. Don’t be afraid to get creative!

Enter the following info:

- Model Name: `llama32`
- Model URL: `https://llama32-ai501.<CLUSTER_DOMAIN>/v1/chat/completions`

..and for the rest, it is up to what you feel like trying 🧪  

#### What is the best system prompt and settings you can find to summarize the above text?

<details>
<summary> 📜 Here are a few example System Prompts you can try.</summary>  
<br>
```
Write a short version of this.
```

```
Summarize the text in a few sentences.
```

Can you come up with something that explains the text even better without loosing important info?
</details>

<div class="iframe-scroll-container">
  <iframe 
    src="https://gradio-app-ai501.<CLUSTER_DOMAIN>/prompt-playground"  
    width="1600px" 
    height="800px" 
    frameborder="0"
    style="border: 1px solid transparent; border-radius: 1px;">
  </iframe>
</div>
