import streamlit as st 
from PIL import Image
from rembg import remove
import io

st.title("🖼️ Background Remover")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing Background..."):

            input_bytes = uploaded_file.getvalue()
            output_bytes = remove(input_bytes)

            output = Image.open(io.BytesIO(output_bytes))

        st.subheader("Background Removed Image")
        st.image(output)

        st.download_button(
            label="⬇️ Download Image",
            data=output_bytes,
            file_name="background_removed.png",
            mime="image/png"
        )

st.markdown("---")
st.markdown("""
### 👨‍💻 Created by Mr Shubham
🔗 GitHub: https://github.com/shubham0182  
📸 Instagram: https://instagram.com/_shubhhh_012
""")
