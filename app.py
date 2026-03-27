import streamlit as st 
import os 
from PIL import Image
from rembg import remove
import io

st.title("🖼️ Background Remover")

uploded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploded_file:
    img = Image.open(uploded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing Background..."):
            output = remove(img)

        st.subheader("Background Removed Image")
        st.image(output)

        # Convert image to bytes for download
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Download button
        st.download_button(
            label="⬇️ Download Image",
            data=byte_im,
            file_name="background_removed.png",
            mime="image/png"
        )

st.markdown("---")

# Footer
st.markdown(
    """
    ### 👨‍💻 Created by Mr Shubham
    
    🔗 GitHub: https://github.com/shubham0182  
    📸 Instagram: https://instagram.com/_shubhhh_012
    """
)
