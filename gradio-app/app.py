import gradio as gr
import requests
import json

def chat_with_model(model_name, model_url, system_prompt, user_prompt):
    """
    Function to send prompts to a model API and get response
    """
    if not model_url or not user_prompt:
        return "Please provide both model URL and user prompt."
    
    try:
        # Prepare the payload (this is a generic format, adjust based on your API)
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt or "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 100,
            "temperature": 0.7
        }
        
        headers = {
            "Content-Type": "application/json",
        }
        
        # Make the API call
        response = requests.post(model_url, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            # Extract response (adjust based on your API response format)
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            elif 'response' in result:
                return result['response']
            else:
                return f"Response received but format unexpected: {result}"
        else:
            return f"Error {response.status_code}: {response.text}"
            
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create the Gradio interface
with gr.Blocks(title="Play with Prompts") as demo:
    gr.Markdown("# 🤖 Play with Prompts")
    gr.Markdown("Enter your model URL, system prompt, and user prompt to get AI responses.")

    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            model_name = gr.Textbox(
                label="Model Name",
                placeholder="tinyllama",
                lines=1
            )
            model_url = gr.Textbox(
                label="Model API URL",
                placeholder="https://api.example.com/v1/chat/completions",
                lines=1
            )
            system_prompt = gr.Textbox(
                label="System Prompt",
                placeholder="You are a helpful assistant...",
                lines=3,
                value="You are a helpful assistant."
            )
            user_prompt = gr.Textbox(
                label="User Prompt",
                placeholder="Enter your question or message here...",
                lines=3
            )
            submit_btn = gr.Button("Send", variant="primary")

        with gr.Column(scale=1.5):
            output = gr.Textbox(
                label="AI Response",
                lines=18,
                max_lines=30,
                interactive=False,
                placeholder="AI response will appear here...",
                show_copy_button=True
            )

    # Set up the event handler
    submit_btn.click(
        fn=chat_with_model,
        inputs=[model_name, model_url, system_prompt, user_prompt],
        outputs=output
    )
    
    # Also allow Enter key to submit
    user_prompt.submit(
        fn=chat_with_model,
        inputs=[model_name, model_url, system_prompt, user_prompt],
        outputs=output
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(
        share=True,  # Set to True if you want a public link
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860  # Default Gradio port
    )