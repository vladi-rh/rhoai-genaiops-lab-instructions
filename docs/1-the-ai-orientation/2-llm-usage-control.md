# 💭 Using and Controlling LLMs

## 📚 Contents
- [💭 Using and Controlling LLMs](#-using-and-controlling-llms)
  - [📚 Contents](#-contents)
  - [💭 Prompting Techniques](#-prompting-techniques)
  - [🚨 Understanding Hallucinations](#-understanding-hallucinations)
  - [🛡️ Implementing Guardrails](#️-implementing-guardrails)
  - [🔍 Hands-on Exercises](#-hands-on-exercises)

## 💭 Prompting Techniques

Prompting is how we shape model behavior. There are two key parts:
- **System Prompt**: Defines the assistant's role (e.g., "You are a helpful tutor…")
- **User Prompt**: The actual input or question

Small changes in wording can **dramatically** change the output. That's why prompt engineering is crucial in education — it determines how clearly, accurately, and appropriately the model responds to students and instructors.

📚 We'll dive much deeper into **prompt engineering strategies** in later chapters.

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">📝 Quiz: What's the difference between system and user prompts?</h3>

<style>
.quiz-container-prompting { position: relative; }
.quiz-option-prompting {
  display: block;
  margin: 4px 0;
  padding: 8px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-prompting:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-prompting { display: none; }
.quiz-radio-prompting:checked + .quiz-option-prompting[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-prompting:checked + .quiz-option-prompting:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-prompting {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#prompting-correct:checked ~ .feedback-prompting[data-feedback="correct"],
#prompting-wrong1:checked ~ .feedback-prompting[data-feedback="wrong"],
#prompting-wrong2:checked ~ .feedback-prompting[data-feedback="wrong"] {
  display: block;
}
.feedback-prompting[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-prompting[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-prompting">
   <input type="radio" name="quiz-prompting" id="prompting-wrong2" class="quiz-radio-prompting">
   <label for="prompting-wrong2" class="quiz-option-prompting" data-correct="false">📊 Both system and user prompts serve the same purpose and can be used interchangeably</label>

   <input type="radio" name="quiz-prompting" id="prompting-wrong1" class="quiz-radio-prompting">
   <label for="prompting-wrong1" class="quiz-option-prompting" data-correct="false">🔄 System prompts are user questions and user prompts define the assistant's role</label>

   <input type="radio" name="quiz-prompting" id="prompting-correct" class="quiz-radio-prompting">
   <label for="prompting-correct" class="quiz-option-prompting" data-correct="true">🎭 System prompts define the assistant's role, user prompts are the actual questions or inputs</label>

   <div class="feedback-prompting" data-feedback="correct">✅ <strong>Perfect!</strong> System prompts establish the AI's behavior and role, while user prompts provide the specific task or question.</div>
   <div class="feedback-prompting" data-feedback="wrong">❌ <strong>Try again!</strong> Think about how system prompts set the context and user prompts provide the specific input.</div>
</div>
</div>

---

## 🚨 Understanding Hallucinations

LLMs sometimes **hallucinate** — confidently generate text that's incorrect or fictional.

Why it happens:
- They optimize for coherence, not factual accuracy
- They don't "know" facts—they predict likely token sequences

Mitigation tips:
- Include accurate facts in the prompt
- Use guardrails (see below)
- Add retrieval or validation layers

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">🚨 Quiz: Why do LLMs hallucinate?</h3>

<style>
.quiz-container-hallucination { position: relative; }
.quiz-option-hallucination {
  display: block;
  margin: 4px 0;
  padding: 8px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-hallucination:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-hallucination { display: none; }
.quiz-radio-hallucination:checked + .quiz-option-hallucination[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-hallucination:checked + .quiz-option-hallucination:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-hallucination {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#hallucination-correct:checked ~ .feedback-hallucination[data-feedback="correct"],
#hallucination-wrong1:checked ~ .feedback-hallucination[data-feedback="wrong"],
#hallucination-wrong2:checked ~ .feedback-hallucination[data-feedback="wrong"] {
  display: block;
}
.feedback-hallucination[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-hallucination[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-hallucination">
   <input type="radio" name="quiz-hallucination" id="hallucination-wrong1" class="quiz-radio-hallucination">
   <label for="hallucination-wrong1" class="quiz-option-hallucination" data-correct="false">🐛 It's a bug that will be fixed in future models</label>

   <input type="radio" name="quiz-hallucination" id="hallucination-correct" class="quiz-radio-hallucination">
   <label for="hallucination-correct" class="quiz-option-hallucination" data-correct="true">🎯 They optimize for coherence and predict likely token sequences, not factual accuracy</label>

   <input type="radio" name="quiz-hallucination" id="hallucination-wrong2" class="quiz-radio-hallucination">
   <label for="hallucination-wrong2" class="quiz-option-hallucination" data-correct="false">💾 They have corrupted training data</label>

   <div class="feedback-hallucination" data-feedback="correct">✅ <strong>Excellent!</strong> LLMs generate plausible-sounding text based on patterns, not facts they "know" to be true.</div>
   <div class="feedback-hallucination" data-feedback="wrong">❌ <strong>Try again!</strong> Think about how LLMs fundamentally work - they predict tokens, not retrieve facts.</div>
</div>
</div>

---

## 🛡️ Implementing Guardrails

To keep your assistant safe and on-task, you can apply **guardrails**, such as:
- Prompt templates with strict instructions
- Output filters (block offensive or harmful content)
- External validation (e.g., fact-checking or classifiers)

For Canopy AI, these guardrails are essential to ensure alignment with educational standards.

<div style="background: linear-gradient(135deg, #e8f2ff 0%, #f5e6ff 100%); padding: 20px; border-radius: 10px; margin: 20px 0; border: 1px solid #d1e7dd;">

<h3 style="color: #5a5a5a; margin-top: 0;">🛡️ Quiz: What are guardrails in AI systems?</h3>

<style>
.quiz-container-guardrails { position: relative; }
.quiz-option-guardrails {
  display: block;
  margin: 4px 0;
  padding: 8px 16px;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid #e9ecef;
  color: #495057;
}
.quiz-option-guardrails:hover { background: #fff; transform: translateY(-1px); border-color: #dee2e6; }
.quiz-radio-guardrails { display: none; }
.quiz-radio-guardrails:checked + .quiz-option-guardrails[data-correct="true"] { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.quiz-radio-guardrails:checked + .quiz-option-guardrails:not([data-correct="true"]) { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
.feedback-guardrails {
  margin: 4px 0;
  padding: 8px 16px;
  border-radius: 6px;
  display: none;
}
#guardrails-correct:checked ~ .feedback-guardrails[data-feedback="correct"],
#guardrails-wrong1:checked ~ .feedback-guardrails[data-feedback="wrong"],
#guardrails-wrong2:checked ~ .feedback-guardrails[data-feedback="wrong"] {
  display: block;
}
.feedback-guardrails[data-feedback="correct"] { background: #d1f2eb; color: #0c5d56; border: 1px solid #a3d9cc; }
.feedback-guardrails[data-feedback="wrong"] { background: #fce8e6; color: #58151c; border: 1px solid #f5b7b1; }
</style>

<div class="quiz-container-guardrails">
   <input type="radio" name="quiz-guardrails" id="guardrails-wrong1" class="quiz-radio-guardrails">
   <label for="guardrails-wrong1" class="quiz-option-guardrails" data-correct="false">🚀 Performance optimizations that make models run faster</label>

   <input type="radio" name="quiz-guardrails" id="guardrails-wrong2" class="quiz-radio-guardrails">
   <label for="guardrails-wrong2" class="quiz-option-guardrails" data-correct="false">📊 Data preprocessing techniques used during model training</label>

   <input type="radio" name="quiz-guardrails" id="guardrails-correct" class="quiz-radio-guardrails">
   <label for="guardrails-correct" class="quiz-option-guardrails" data-correct="true">🛡️ Safety mechanisms that control and constrain model behavior and outputs</label>

   <div class="feedback-guardrails" data-feedback="correct">✅ <strong>Excellent!</strong> Guardrails are essential safety measures that help ensure AI systems behave appropriately and safely in production environments.</div>
   <div class="feedback-guardrails" data-feedback="wrong">❌ <strong>Try again!</strong> Think about how guardrails help control what an AI system can and cannot do or say.</div>
</div>
</div>

## 🔍 Hands-on Exercises

**Exercise 1**: Memory Test
1. In Gradio, send a message asking "What did you learn today?"
2. Send a new message asking "What did I say in the last message?"
3. Compare this with how Canopy UI handles conversation memory

**Exercise 2**: Consistency Check
1. Ask the model a specific question
2. Note the response
3. Ask the same question again
4. Compare the responses to understand how consistency works in LLMs

[🔝 Back to Contents](#contents)