import streamlit as st

st.title("Coding Library")

col1, col2 = st.columns([1, 1])

col1.write("##### import streamlit as st")
col2.write("This imports the streamlit library and allows us to use all of its functions")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)  # Full-width dashed line

col1.subheader("String Functions")

col1.write("##### st.title('')")
col2.write("This function allows us to add a title to the top of the page")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)

col1.write("##### st.subheader('')")
col2.write("This function allows us to add a subheader to the page")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)

col1.write("##### st.write('')")
col2.write("This is the most basic function that allows us to write text to the page. Also, using `##` in Markdown allows us to create headers in the `write` function.")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)

col1.subheader("Interactive Functions")

col1.write("##### st.button('')")
col2.write("This function creates a button that can be clicked, with a variable that is callable.")

is_click = col2.link_button("Click Me", "https://www.youtube.com/shorts/SXHMnicI6Pg")

st.markdown('<hr style="border:1px dashed #ccc;">', unsafe_allow_html=True)

col1.write("##### st.text_input('')")
col2.write("This function creates a text input box that can be filled out by the user, with a variable that is callable.")

fav_color = st.text_input("My name's Buddy. What's your favorite color?")
st.write(f"{fav_color} is my favorite color too!")
