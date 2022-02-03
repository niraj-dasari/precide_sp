import tweepy
import streamlit as st

# Consumer keys and access tokens, used for OAuth
api_key = 'E9qVlfLPCKPdSFrys4dIcu1g0'
api_key_secret = 'wa8hVKDOWDw7j1vnRWOkqtU9CxKy1DGA8oQNo4rY6I83zUl9Zg'

access_token = '1462031883135561737-13jGCSDwmyvDIMHlvZ9o4SCJfDTrhS'
access_token_secret = 'C8edgIa1uu6W2JndI00fc6nsCaOPpcMWFNUr7jeXsNvhK'



CONSUMER_KEY = api_key
CONSUMER_SECRET= api_key_secret
OAUTH_TOKEN=access_token
OAUTH_TOKEN_SECRET = access_token_secret
# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

'''# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

userid=st.text_input()
sButton = st.button()
if sButton:
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items():
        print(status.full_text)
        st.write(status.full_text)'''