import streamlit as st

st.title("Cool Features")

st.write("#### Below are some cool features that Streamlit offers.")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.subheader("Fundamentals") 

st.link_button("Click me!", "https://docs.streamlit.io/get-started/fundamentals/additional-features")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.subheader("Components")

st.link_button("Click me!", "https://streamlit.io/components?category=authentication")

