import streamlit as st


st.title("coding library")


col1, col2 = st.columns([1, 1])

col1.write("##### import streamlit as st")
col2.write("This imports the streamlit library and allows us to use all of its functions")
col1.markdown("---")
col2.markdown("---")

col1.markdown("  ")
col2.markdown("  ")

col1.subheader("String Functions")

col1.write("##### st.title('')")
col2.write("This function allows us to add a title to the top of the page")
col1.markdown("---")
col2.markdown("---")

col1.write("##### st.subheader('')")
col2.write("This function allows us to add a subheader to the page")
col1.markdown("---")
col2.markdown("---")

col1.write("##### st.write('')")
col2.write("this is the most basic function allows us to write text to the page. Also the Use of ## from the markdown language allows us to create headers in the write function")

col1.markdown("  ")
col2.markdown("  ")
col1.subheader("Interactive Functions")
col1.markdown("  ")
col2.markdown("  ")

col1.write("##### st.button('')")
col2.write("This function creates a button that can be clicked, with a varible that callable")
is_click = col2.link_button("Click Me" ,"https://www.youtube.com/shorts/SXHMnicI6Pg")
col1.markdown("---")
col2.markdown("---")


col1.write("##### st.text_input('')")
col2.write("This function creates a text input box that can be filled out by the user, with a varible that is callable")

fav_color = st.text_input('My names Buddy whats your favorit color?')
st.write(f"{fav_color} is my favorite color too!")


