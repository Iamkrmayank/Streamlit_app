import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Streamlit app title
st.title("GPT-3.5 Turbo Chatbot")

# Function to interact with GPT-3.5 Turbo
def generate_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

# Streamlit input box for user prompt
user_input = st.text_input("Enter your prompt:")

# Button to generate response
if st.button("Get Response"):
    # Display the response
    response = generate_response(user_input)
    st.text("Model's Response:")
    st.write(response)

# Example prompt for users to try
st.text("Example prompt: 'Translate the following English text to French: [Your English text here]'")
