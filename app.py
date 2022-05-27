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

feature = st.text_input('feature')
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

data={'title': title,
      'description': description,
      'feature': feature,
      'category': category,
      'brand': brand,
      'image': image_input}

url = 'https://deepseoimage-5ost5gg5jq-ew.a.run.app/'
urll="evaluation?title=" + data.get("title") + "&description=" + data.get("description") + "&feature=" + data.get("feature") + "&category="+ data.get("category")+"&brand="+ data.get("brand")+"&image"+ data.get("image")
new_url=url + urll
# /evaluation?title=Socks&description=Pink socks stripes&feature=Long pink sock&category=clothing&brand=uniqlo&image=2

import requests
x= requests.get(new_url)
print (x.json()["ranking"])

'''
## The predicted ranking for your Amazon product is ...
'''
if st.button('Submit'):
    # print is visible in the server output, not in the page
    st.write('Best Selling product ever! :D')
    st.write(x.json()["ranking"])
