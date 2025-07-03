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

We’ve created a **Gradio-based interface** where you can experiment with different prompting strategies. Your aim is to find the best system prompt and configuration to summarize the given text as good as possible.

Here’s what you can configure:

* 🔗 **Model Info**: Connect to your chosen LLM (local or remote).
* 🧾 **System Prompt**: Set the model’s “persona” or behavior.
* 💬 **User Prompt**: Ask a question, give a command, or provide input.
* 🔢 **Max Tokens**: Control the length of the model’s output.
* 🔥 **Temperature**: Adjust creativity vs. precision. Lower = more focused, Higher = more creative.

Here is the prompt to summarize:

```
Canopy (Biology)

In biology and ecology, the canopy refers to the upper layer or “roof” formed by the crowns of trees in a forest or wooded area. This layer plays a critical role in regulating the ecosystem by controlling light penetration, humidity, temperature, and wind flow within the forest environment. The canopy is typically made up of the tallest trees and their branches and leaves, which often form a dense, continuous cover that can be several meters thick.

One of the primary ecological functions of the canopy is to provide habitat and food sources for a wide range of organisms. Many species of birds, insects, mammals, and epiphytes (plants that grow on other plants) are specially adapted to live in this elevated environment. The canopy also acts as a barrier that reduces the impact of heavy rain on the forest floor, helping to prevent soil erosion and maintain soil fertility.

Moreover, the canopy plays a crucial role in photosynthesis on a large scale by capturing sunlight and converting it into chemical energy, which sustains the forest’s plant life and, consequently, the animals that depend on it. In tropical rainforests, the canopy is often so dense that very little sunlight reaches the forest floor, shaping the types of plants and animals that can survive in the understory and ground layers.

Scientists study canopies using specialized tools and methods such as canopy cranes, drones, and climbing equipment to better understand their structure, biodiversity, and ecological functions. This knowledge is vital for conservation efforts, particularly as canopies are sensitive to deforestation, climate change, and human activities that threaten their integrity.

Understanding the canopy’s complexity helps ecologists appreciate the interdependent relationships within forests and the critical services these ecosystems provide, including carbon storage, oxygen production, and climate regulation. Protecting the canopy is essential to maintaining biodiversity and the health of our planet.
```

Use the Prompt Playground to:

* Compare how different **system prompts** change the behavior of the same model.
* Adjust **temperature** and **max tokens** to explore how output varies.
* Decide on a system prompt template that will work well for **Canopy AI’s learning assistant** in future modules.

📌 **Tip**: Try changing the tone, specificity, or format of your system prompt to see how much it shapes the output. Don’t be afraid to get creative!

Enter the following info:

- Model Name: `llama32-full`
- Model URL: `https://llama32-ai501.<CLUSTER_DOMAIN>/v1/chat/completions`

..and for the rest, it is your creativity :)

<div class="iframe-scroll-container">
  <iframe 
    src="https://gradio-app-ai501.<CLUSTER_DOMAIN>/prompt-playground"  
    width="1600px" 
    height="800px" 
    frameborder="0"
    style="border: 1px solid transparent; border-radius: 1px;">
  </iframe>
</div>
