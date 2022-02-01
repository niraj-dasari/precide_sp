import imp
import streamlit as st
import streamlit.components.v1 as components
import requests
import re
 
def theTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res =response.json()['html']
    return res

input = st.text_input("Enter here the url of your tweet")

if input:
    res = theTweet(input)
    st.write(res)
    tweet_text = re.sub(r"\<[^<>]*\>", "", res)
    components.html(res,height=700)
    st.write(tweet_text)