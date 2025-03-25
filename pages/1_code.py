import streamlit as st

st.title("Coding Library")

st.write("#### import treamlit as st")

st.write("This imports the Streamlit library and allows us to use all of its functions.")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.subheader("String Functions")

st.write("#### st.title('')")
st.write("This function allows us to add a title to the top of the page.")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.write("#### st.subheader('')")
st.write("This function allows us to add a subheader to the page.")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.write("#### st.write('')")
st.write("This is the most basic function that allows us to write text to the page. Also, using `##` in Markdown allows us to create headers in the `write` function.")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.subheader("Interactive Functions")

st.write("#### st.button('')")
st.write("This function creates a button that can be clicked, with a variable that is callable.")

is_click = st.link_button("Click Me", "https://www.youtube.com/shorts/SXHMnicI6Pg")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

st.write("#### st.text_input('')")
st.write("This function creates a text input box that can be filled out by the user, with a variable that is callable.")

fav_color = st.text_input("My name's Buddy. What's your favorite color?")
st.write(f"{fav_color} is my favorite color too!")

