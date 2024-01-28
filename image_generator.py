import streamlit as st
from openai import OpenAI

# Replace 'your_openai_api_key' with your actual OpenAI API key
openai_api_key = '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'
client = OpenAI(api_key=openai_api_key)

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return image_url

def main():
    st.title("Image Generation App with OpenAI DALL-E")

    # Get user input
    prompt = st.text_input("Enter a prompt:")

    if st.button("Generate Image"):
        st.spinner("Generating image...")

        # Generate image
        image_url = generate_image(prompt)

        st.success("Image generated successfully!")
        st.image(image_url, caption="Generated Image", use_column_width=True)

if __name__ == "__main__":
    main()