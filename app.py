import streamlit as st
from PIL import Image

'''
# DEEP SEO
# We rank your products :)
'''

st.markdown('''
Please fill in the blanks below.
''')

title = st.text_input('Title')
# st.write('Title', title)

description = st.text_input('Description')
# st.write('Description ', description)

features = st.text_input('features')
# st.write('Features ', features)

category = st.text_input('Category')
# st.write('Category ', category)

brand = st.text_input('Brand')
# st.write('Brand is ', brand)

image_input = st.text_input('Image Link')
if st.button('Show image'):
    # print is visible in the server output, not in the page
    if image_input=="":
        st.write("Please input your image URL~")
    if image_input:
        st.image(image_input, caption='Your Amazon Product Picture', use_column_width=False)


'''
## The predicted ranking for your Amazon product is ...
'''
if st.button('Submit'):
    # print is visible in the server output, not in the page
    st.write('Best Selling product ever! :D')
