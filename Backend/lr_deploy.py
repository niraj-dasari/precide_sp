
from altair.vegalite.v4.schema.channels import Color
import streamlit as st
import altair as alt

import pandas as pd
import numpy as np

import joblib

pipl_lr = joblib.load(open('models/lr_model.pkl','rb'))

def predict_suicide(snt):
    results = pipl_lr.predict([snt])
    return results[0]

def get_probability(snt):
    results = pipl_lr.predict_proba([snt])
    return results



def main():
    st.title("Suicide Prediction System")
    menu = [ "Home" , "Monitor" , "About"]
    choice = st.sidebar.selectbox("Menu" , menu)
    choice = 'Home'
    if choice == "Home":
        st.subheader("Home Page")
        with st.sidebar.form( key = "Text form"):
            stext = st.text_area(" type hear...")
            submit_st=st.form_submit_button( label= 'Submit')
        
        if submit_st:
            colp , colv = st.columns(2)
            prediction = predict_suicide(stext)
            probability = get_probability(stext)

            with colp:
                st.success("Original Text")
                st.write(stext)
                

                st.success("Prediction")
                st.write(prediction)
                st.write("confidence : {:.2f}".format((np.max(probability))*100),"%")

            with colv:
                st.success("Prediction Probability")
                # st.write(probability)
                proba_df = pd.DataFrame(probability,columns=pipl_lr.classes_)
                # st.write(proba_df.T)
                proba_df_clean =proba_df.T.reset_index()
                proba_df_clean.columns = ["emotions" , "probability"]
                fig = alt.Chart(proba_df_clean).mark_bar().encode(x = 'emotions' , y = 'probability' , color = 'emotions')
                st.altair_chart(fig,use_container_width=True)
    elif choice == "Monitor":
        st.subheader("Monitor Page")
    
    else:
        st.subheader("About Page")

if __name__ == '__main__':
    main()

   