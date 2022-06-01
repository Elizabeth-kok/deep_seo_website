from streamlit_option_menu import option_menu
from tokenize import Imagnumber
import streamlit as st
from PIL import Image

img=Image.open("a.gif")
st.set_page_config(page_title="DEEP SEO",page_icon=img,layout="centered")

# st.set_page_config(
#     page_title="Quick reference", # => Quick reference - Streamlit
#     page_icon="🐍",
#     layout="centered", # wide
#     initial_sidebar_state="auto") # collapsed

EXAMPLE_NO = 3

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Our service", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Our service", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Our service", "Contact"],  # required
            icons=["house", "search", "emoji-sunglasses"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected

selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Our service":

    st.title("What is SEO")

    """
    Search engine optimization (SEO) is the process of improving the quality and quantity of website traffic to a website or a web page from search engines.
    SEO targets unpaid traffic (known as "natural" or "organic" results) rather than direct traffic or paid traffic.
    Unpaid traffic may originate from different kinds of searches, including image search, video search, academic search,news search, and industry-specific vertical search engines.
    As an Internet marketing strategy, SEO considers how search engines work, the computer-programmed algorithms that dictate search engine behavior, what people search for, the actual search terms or keywords typed into search engines, and which search engines are preferred by their targeted audience.
    SEO is performed because a website will receive more visitors from a search engine when websites rank higher on the search engine results page (SERP).
    These visitors can then potentially be converted into customers.
    Immediately see which product listings need improvement.
    Get recommendations for changing your product title, bullet points, description and Seller Central backend search terms.
    """

    st.title("What is the issue")

    """
    An amazon seller wants to evaluate the quality of the landing pages of their products.
    Very cost to rely on experts or use their intuition.
    """
    st.title("Brainstorming")

    """
    If seller knows in advance whether their product will sell well or not allows sellers to revise their plans before the launch.
    """

    st.title("Our goal")

    """
    Developing a deep learning model that uses current data from similar products to evaluate the quality for a new product landing page in Amazon.
    Low cost solution to improve the chances of selling based on search results in relation to the rest of the competitors so they can appear in the results when a client looks for a product.
    """

    st.title("Solution overview")

    """
    Seller provides the information they have for a landing page
    The data goes through the model that classifies the product
    Seller gets an evaluation on the “searchability” of the product compared with similar products
    """


if selected == "About us":

    st.title("Who we are")

    st.markdown('''
    ## Cris

    LinkedIn:
    ''')

    st.markdown('''
    ## Elizabeth

    LinkedIn:
    ''')

    st.markdown('''
    ## Nayoung

    LinkedIn:
    ''')

if selected == "Home":
    '''
    # DEEP SEO
    ## We rank your products :)
    '''
    col1, col2, col3 = st.columns(3)

    st.markdown('''
    Fill in the blanks below.
    ''')

    title = st.text_input('Title')
    # st.write('Title', title)

    description = st.text_input('Description')
    # st.write('Description ', description)

    feature = st.text_input('Feature')
    # st.write('Features ', features)

    image_input1 = st.text_input('Image Link 1')
    if st.button('Show image 1'):
        # print is visible in the server output, not in the page
        if image_input1=="":
            st.write("Please input your image URL")
        else:
            try:
                st.image(image_input1, caption='Your Amazon Product Picture', use_column_width=False,width=200)
            except:
                st.write("Please input a correct image URL")

    image_input2 = st.text_input('Image Link 2')
    if st.button('Show image 2'):
        # print is visible in the server output, not in the page
        if image_input2=="":
            st.write("Please input your image URL")
        else:
            try:
                st.image(image_input2, caption='Your Amazon Product Picture', use_column_width=False,width=200)
            except:
                st.write("Please input a correct image URL")

    image_input3 = st.text_input('Image Link 3')
    if st.button('Show image 3'):
        # print is visible in the server output, not in the page
        if image_input3=="":
            st.write("Please input your image URL")
        else:
            try:
                st.image(image_input3, caption='Your Amazon Product Picture', use_column_width=False,width=200)
            except:
                st.write("Please input a correct image URL")

    data={'title': title,
        'description': description,
        'feature': feature,
        'imageone': image_input1,
        'imagetwo': image_input2,
        'imagethree': image_input3,}

    url = 'https://deepseosecond-5ost5gg5jq-ew.a.run.app/seo_eval'
    urll="?title=" + data.get("title") + "&description=" + data.get("description") + "&feature=" + data.get("feature") + "&imageone=" + data.get("imageone") + "&imagetwo="+ data.get("imagetwo")+"&imagethree="+ data.get("imagethree")
    new_url=url + urll
# /seo_eval?title=fake title for a fake product &description=this description is awesome&feature=I have no features&imageone=https://cdn-image02.casetify.com/usr/4787/34787/~v3/22690451x2_iphone13_16003249.png.1000x1000-w.m80.jpg&imagetwo=https://m.media-amazon.com/images/I/81MLO3k15iL._AC_SL1500_.jpg&imagethree=https://m.media-amazon.com/images/I/71HiwDwAcoL._AC_SL1500_.jpg

    import requests
    x= requests.get(new_url)
    print (x.json()["Classification"])

    '''
    ## The predicted ranking for your Amazon product is ...
    '''
    if st.button('Submit'):
        # print is visible in the server output, not in the page
        st.write('Best Selling product ever! :D')
        st.write(x.json()["Classification"])
        st.write(x.json()["Rank Image 1"])
        st.write(x.json()["Rank Image 2"])
        st.write(x.json()["Rank Image 3"])

# url = 'https://deepseofirst-5ost5gg5jq-ew.a.run.app/seo_eval'
# urll="?title=" + data.get("title") + "&description=" + data.get("description") + "&feature=" + data.get("feature") + "&imageone=" + data.get("imageone") + "&imagetwo="+ data.get("imagetwo")+"&imagethree="+ data.get("imagethree")

# import requests
# x= requests.get(new_url)
# print (x.json())
