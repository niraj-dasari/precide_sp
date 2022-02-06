import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets


def app():
    st.write("<div><h1 style='color:white;text-align:center;'>Data Result</h1></div>", unsafe_allow_html=True)
    st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: rgb(204, 49, 49);
                width : 100px;
                margin-left : 100px
            }
            </style>""", unsafe_allow_html=True)
    submit_st = st.sidebar.button(label='Load Data')
    if submit_st:
        with st.spinner(text="In progress..."):
            df = pd.read_csv(r"D:\projects\BEIT\precide\dataset\Suicide_Detection.csv")
            df[' '] = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
            st.write(df[['text',' ','class']])

