from googletrans import Translator
import altair as alt

import pandas as pd
import numpy as np
import streamlit as st

import joblib

tr = Translator()

pipl_lr = joblib.load(
    open(r'D:\projects\BEIT\precide\Backend\models\emotion.pkl', 'rb'))


def predict_suicide(snt):
    results = pipl_lr.predict([snt])
    return results[0]


def get_probability(snt):
    results = pipl_lr.predict_proba([snt])
    return results


def predict_lr(text):
    stext = text
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: rgb(204, 49, 49);
            width : 100px;
            margin-left : 100px
        }
        </style>""", unsafe_allow_html=True)
    submit_st = st.sidebar.button(label='Predict')
    if submit_st:
        st.write(f"<div><h1 style='color:white;text-align:center;font-size:60px'>{predict_suicide(stext)} </h1></div>",
                 unsafe_allow_html=True)
        """with st.expander('Result', expanded=True):
            colp, colv = st.columns(2)
            prediction = predict_suicide(stext)
            probability = get_probability(stext)
            with colp:
                st.success("Original Text")
                st.write(text)

                st.success("Prediction")
                st.write(prediction)
                st.write("confidence : {:.2f}".format(
                    (np.max(probability))*100), "%")
            with colv:
                st.success("Prediction Probability")
                # st.write(probability)
                proba_df = pd.DataFrame(probability, columns=pipl_lr.classes_)
                # st.write(proba_df.T)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["emotions", "probability"]
                fig = alt.Chart(proba_df_clean).mark_bar().encode(
                    x='emotions', y='probability', color='emotions')
                st.altair_chart(fig, use_container_width=True)

"""