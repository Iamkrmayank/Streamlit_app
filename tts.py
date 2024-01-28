import streamlit as st
from openai import OpenAI
from tempfile import NamedTemporaryFile

# Initialize OpenAI client
openai_api_key = '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'  # Replace with your OpenAI API key
client = OpenAI(api_key=openai_api_key)

def tts(query):
    with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=query
        )

        temp_file.write(response.content)
        temp_file_path = temp_file.name

    return temp_file_path

def main():
    st.title("Text-to-Speech App with OpenAI")

    # Get user input
    query = st.text_input("Enter text:")

    if st.button("Generate Speech"):
        st.spinner("Generating speech...")

        # Generate speech
        speech_file_path = tts(query)

        st.success("Speech generated successfully!")
        st.audio(speech_file_path, format="audio/mp3")

if __name__ == "__main__":
    main()
