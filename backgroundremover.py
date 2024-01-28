import streamlit as st
from rembg import remove
from PIL import Image

# !pip install Pillow
# !pip install rembg
def removebackground(image_path,output_path):
    input = Image.open(image_path)
    output = remove(input)
    output.save(output_path)

def main():
    st.title('Background remover')
    uploaded_file = st.file_uploader("Upload an image : ",type=["jpg","jpeg","png"])
    if uploaded_file is not None :
        st.image(uploaded_file,caption="Uploaded file",use_column_width=True)
        
    if st.button("Remove Background"):
        img_name = "uploaded_image"
        input_path = f'/content/{img_name}.png'
        output_path = f'/content/{img_name}_removebackground.png'
    
        with open(input_path,"wb") as f:
            f.write(uploaded_file.getvalue())
        
        removebackground(input_path,output_path)
        st.image([input_path, output_path], caption=["Original Image", "Background Removed"], use_column_width=True)
        st.success("Image processed successfully! Check the result below.")

if __name__=="__main__":
    main()


''' from google.colab import drive
drive.mount('/content/drive')

# Upload the file using
from google.colab import files

uploaded = files.upload()

# Store path of the image in the variable input_path
name = input("Enter the name of the image")
input_path = '/content/'+name+'.jpeg'

# Store path of the output image in the variable output_path
output_path = '/content/'+name+'removebg.png'

  # Processing the image
input = Image.open(input_path)

  # Removing the background from the given Image
output = remove(input)

  #Saving the image in the given path
output.save(output_path)
'''


