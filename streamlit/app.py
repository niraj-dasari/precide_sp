import streamlit as st
from multiapp import MultiApp
from apps import home, data, prediction, sentiment_analysis, user # import your app modules here

st.set_page_config(initial_sidebar_state="collapsed",layout="wide")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}    
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

app = MultiApp()
# Add all your application here
app.add_app("Home", home.app)
app.add_app("prediction", prediction.app)
app.add_app("Data", data.app)
app.add_app("Sentiment Analysis", sentiment_analysis.app)
app.add_app("Profile Analysis", user.app)


# The main app
app.run()