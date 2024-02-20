# -*- coding: utf-8 -*-
"""UTUBE_audio_streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ruWTrc7OdQK1hes91evkCFEYvzKGBJgH
"""

!pip install streamlit

!pip install pytube

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# from pytube import YouTube
# import os
# 
# def download_audio(video_url, download_directory):
#     try:
#         # Create a YouTube object
#         youtube = YouTube(video_url)
# 
#         # Get the highest resolution audio stream
#         audio_stream = youtube.streams.filter(only_audio=True, file_extension='mp4').first()
# 
#         # Specify a user-friendly filename
#         filename = f"{youtube.title}.mp3"
#         filepath = os.path.join(download_directory, filename)
# 
#         # Download the audio stream
#         audio_stream.download(output_path=download_directory, filename=filename)
# 
#         return True, f"Audio downloaded for video: {youtube.title}", filepath
# 
#     except Exception as e:
#         return False, f"Error downloading audio for video {youtube.title}: {str(e)}", None
# 
# def main():
#     st.title("YouTube Audio Downloader")
# 
#     # Input field for the YouTube video URL
#     video_url = st.text_input("Enter YouTube Video URL:")
# 
#     # Specify the directory where you want to save the audio file
#     download_directory = 'audio_downloads'
# 
#     # Create the directory if it doesn't exist
#     if not os.path.exists(download_directory):
#         os.makedirs(download_directory)
# 
#     if st.button("Click Here"):
#         if video_url:
#             with st.spinner("Downloading..."):
#                 result, message, filepath = download_audio(video_url, download_directory)
#             st.success(message)
# 
#             if result and filepath:
#                 # Display the download button
#                 st.download_button(
#                     label="Download Audio File",
#                     data=open(filepath, 'rb').read(),
#                     key="download_button",
#                     file_name=os.path.basename(filepath),
#                     mime="audio/mp3"
#                 )
# 
#     #st.text("Audio will be downloaded to the 'audio_downloads' folder.")
# 
# if __name__ == "__main__":
#     main()

!npm install localtunnel

!streamlit run app.py &>/content/logs.txt & npx localtunnel --port 8501 & curl ipv4.icanhazip.com