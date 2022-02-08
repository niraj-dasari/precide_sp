import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
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
            df = pd.read_csv(r'D:\projects\BEIT\precide\dataset\Suicide_Detection.csv')
            data = pd.DataFrame()
            data['sentence'] = df['text']
            data['prediction'] = df['class']
            st.dataframe(data)
            df1 = pd.read_excel(r'D:\projects\BEIT\precide\notebooks\Suicide prediction Prediction\output.xlsx')
            pie_chart = px.pie(df1,title="Total No. of Tweets",values="count",names="class")
            st.plotly_chart(pie_chart)
