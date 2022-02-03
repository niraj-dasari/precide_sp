from distutils.command.config import config
from httpx import Auth
import twitter

import tweepy 
from tweepy.auth import OAuthHandler
import streamlit as st
import streamlit.components.v1 as components
import requests
import re


api_key = 'E9qVlfLPCKPdSFrys4dIcu1g0'
api_key_secret = 'wa8hVKDOWDw7j1vnRWOkqtU9CxKy1DGA8oQNo4rY6I83zUl9Zg'

access_token = '1462031883135561737-13jGCSDwmyvDIMHlvZ9o4SCJfDTrhS'
access_token_secret = 'C8edgIa1uu6W2JndI00fc6nsCaOPpcMWFNUr7jeXsNvhK'



CONSUMER_KEY = api_key
CONSUMER_SECRET= api_key_secret
OAUTH_TOKEN=access_token
OAUTH_TOKEN_SECRET = access_token_secret

auth = twitter.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)


twitter_api =twitter.Twitter(auth=auth)

print(twitter_api)

statuses = twitter_api.statuses.user_timeline(screen_name='@realDonaldTrump')
print([status['text'] for status in statuses])


 
def theTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res =response.json()['html']
    return res

if input:
    res = theTweet(input)
    st.write(res)
    tweet_text = re.sub(r"\<[^<>]*\>", "", res)
    components.html(res,height=700)
    st.write(tweet_text)