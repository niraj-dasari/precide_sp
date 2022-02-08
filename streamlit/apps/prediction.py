import streamlit as st
import numpy as np


from .algorithms.logistic_regression import predict_lr
import streamlit.components.v1 as components
import requests
import easyocr as ocr 
from PIL import Image
import re


def text_input():
    return st.sidebar.text_area("", placeholder="Enter text here!")


def url_input():
    url = st.sidebar.text_input("", placeholder="Enter URL here!")
    if url != "":
        api = "https://publish.twitter.com/oembed?url={}".format(url)
        response = requests.get(api)
        res =response.json()['html']
        tweet_text = re.sub(r"\<[^<>]*\>", "", res)
        with st.sidebar:
            with st.expander("Tweet",expanded=False):

                components.html(res,height=500,scrolling=True)
        #st.write(tweet_text)
        return tweet_text
    return url

def image_input():
    reader = ocr.Reader(['en','hi'],gpu=True,model_storage_directory='.')
    image = st.sidebar.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])
    if image is not None:
        with st.expander('OCR', expanded=True):
            col1 , col2 = st.columns(2)

            with col1:
                input_image = Image.open(image) 
                st.image(input_image) 
                st.success("Image Loading Successfully")
            
            with col2:
                with st.spinner("Extracting the text..."):
                    

                    result = reader.readtext(np.array(input_image))

                    result_text = "" 


                    for text in result:
                        result_text += text[1]+" " 


                    st.write(result_text.lower())
                st.success("Text is extracted from image")
                return result_text
    else:
        st.write("")
    return "Please Select a image! 🙂"



def input_choice(option):
    if option == "Text":
        return text_input()
    elif option == "URL":
        return url_input()
    else:
        return image_input()


def app():
    #st.title("Prediction page")
    st.sidebar.write("<div><h2 style='color:white;text-align:center;padding:0px;'>Text Prediction</h2></div>",
                     unsafe_allow_html=True)

    st.sidebar.write(
        "<style>div.row-widget.stRadio > div{flex-direction:row;justify-content:space-evenly;}</style>",
        unsafe_allow_html=True,
    )
    option_input = st.sidebar.radio("", ("Text", "URL", "Image"))

    option_algorithm = st.sidebar.selectbox(
        "",
        (
            "Logistic Regression",
            "Naive Bayes",
            "Support Vector Machine",
            "Random Forest",
        ),
    )
    st.write("<div><h1 style='color:white;text-align:center;'>Predition Result</h1></div>",unsafe_allow_html=True)
    text = input_choice(option_input)
    if text is not None:
        # st.write(Text)
        if option_algorithm == "Logistic Regression":
            predict_lr(text)
        elif option_algorithm == "Naive Bayes":
            st.subheader("Naive Bayes")
        elif option_algorithm == "Support Vector Machine":
            st.subheader("Naive Bayes")
        else:
            st.subheader("Random Forest")
    
    