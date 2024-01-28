import streamlit as st
from rembg import remove
from PIL import Image
import os

def remove_background(image_path, output_path):
    # Processing the image
    input_image = Image.open(image_path)

    # Removing the background from the given image
    output_image = remove(input_image)

    # Saving the image in the specified output path
    output_image.save(output_path)

def main():
    st.title("Background Removal App")

    # Upload the image using Streamlit file uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Remove background button
        if st.button("Remove Background"):
            # Store the uploaded image in the content directory
            image_name = "uploaded_image"
            input_path = f'/content/{image_name}.png'
            output_path = f'/content/{image_name}_removebg.png'

            with open(input_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            # Remove background
            remove_background(input_path, output_path)

            # Display the original and background-removed images
            st.image([input_path, output_path], caption=["Original Image", "Background Removed"], use_column_width=True)

            # Provide a link to download the background-removed image
            st.success(f"Background removed successfully! You can download the image [here](sandbox:/content/{image_name}_removebg.png).")

if __name__ == "__main__":
    main()
