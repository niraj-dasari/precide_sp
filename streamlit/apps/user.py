import tweepy
import streamlit as st
import streamlit.components.v1 as components
import requests
import joblib


pipl_lr = joblib.load(
    open(r'D:\projects\BEIT\precide\Backend\models\lr_model.pkl', 'rb'))


def predict_suicide(snt):
    results = pipl_lr.predict([snt])
    return results[0]

api_key = 'E9qVlfLPCKPdSFrys4dIcu1g0'
api_key_secret = 'wa8hVKDOWDw7j1vnRWOkqtU9CxKy1DGA8oQNo4rY6I83zUl9Zg'

access_token = '1462031883135561737-13jGCSDwmyvDIMHlvZ9o4SCJfDTrhS'
access_token_secret = 'C8edgIa1uu6W2JndI00fc6nsCaOPpcMWFNUr7jeXsNvhK'

CONSUMER_KEY = api_key
CONSUMER_SECRET = api_key_secret
OAUTH_TOKEN = access_token
OAUTH_TOKEN_SECRET = access_token_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def app():
    # st.title("Prediction page")
    userid = st.sidebar.text_input(label="Enter user url ex-@abc")
    sButton = st.sidebar.button(label="search")
    if sButton:
        api = tweepy.API(auth)
        predlist=[]
        tweets_list = api.user_timeline(screen_name=userid, tweet_mode="extended", count=10)
        st.write("<div><h1 style='color:white;text-align:center;'>Profile analysis</h1></div>", unsafe_allow_html=True)
        with st.expander("See explanation"):
            for tweet in tweets_list:
                tweet_url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}"
                api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
                response = requests.get(api)
                res = response.json()['html']
                st.write(tweet.full_text)
                components.html(res, height=700)
                pred = predict_suicide(tweet.full_text)
                predlist.append(pred)
        if predlist.count("non-suicide") >= predlist.count("suicide"):
            st.write(f"<div><h1 style='color:white;text-align:center;font-size:60px'>User does not have any intension "
                     f"of commiting suicide </h1></div>",unsafe_allow_html=True)
        else:
            st.write(
                f"<div><h1 style='color:white;text-align:center;font-size:60px'>Warning! user have intension of "
                f"commiting suicide </h1></div>",
                unsafe_allow_html=True)


