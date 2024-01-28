import streamlit as st
from simple_image_download import simple_image_download as simp
import os
from zipfile import ZipFile

def download_images(lst, count, label):
    response = simp.simple_image_download

    # Create a directory for downloaded images
    download_dir = "simple_images"
    os.makedirs(download_dir, exist_ok=True)

    for rep in lst:
        response().download(rep + str(label), count)

    # Zip the downloaded images
    zip_filename = "simple_images.zip"
    with ZipFile(zip_filename, 'w') as zip:
        for root, dirs, files in os.walk(download_dir):
            for file in files:
                zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), download_dir))

    return zip_filename

def main():
    st.title("Simple Image Downloader App")

    # Get user input
    keywords = st.text_input("Enter the keywords (comma-separated):")
    keyword_list = keywords.split(",")
    image_count = st.number_input("Enter the number of images:", min_value=1, step=1)
    label = st.text_input("Enter the label:")

    if st.button("Download Images"):
        zip_filename = download_images(keyword_list, image_count, label)
        st.success(f"Images downloaded and zipped successfully! You can download the zip file [here](sandbox:/content/{zip_filename}).")

if __name__ == "__main__":
    main()
