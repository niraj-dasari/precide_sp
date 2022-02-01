import streamlit as st
from .algorithms.logistic_regression import predict_lr


def text_input():
    return st.sidebar.text_area("", placeholder="Enter text here!")


def url_input():
    return st.sidebar.text_input("", placeholder="Enter URL here!")


def input_choice(option):
    if option == "Text":
        return text_input()
    elif option == "URL":
        return url_input()
    else:
        pass


def app():
    #st.title("Prediction page")

    st.sidebar.write(
        "<style>div.row-widget.stRadio > div{flex-direction:row;}</style>",
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
    st.write("<div><h1 style='color:white;text-align:center;'>Analysis Result</h1></div>",unsafe_allow_html=True)
    text = input_choice(option_input)
    if text is not None:
        # st.write(Text)
        if option_algorithm == "Logistic Regression":
            predict_lr(text)
        elif option_algorithm == "Naive Bayes":
            st.subheader("Naive Bayes")
        elif option_algorithm == "Support Vector Machine":
            st.subheader("svm")
        else:
            st.subheader("Random Forest")
    
    