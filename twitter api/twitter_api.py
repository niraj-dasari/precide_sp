from distutils.command.config import config
from httpx import Auth
import tweepy


api_key = 'E9qVlfLPCKPdSFrys4dIcu1g0'
api_key_secret = 'wa8hVKDOWDw7j1vnRWOkqtU9CxKy1DGA8oQNo4rY6I83zUl9Zg'

access_token = '1462031883135561737-13jGCSDwmyvDIMHlvZ9o4SCJfDTrhS'
access_token_secret = 'C8edgIa1uu6W2JndI00fc6nsCaOPpcMWFNUr7jeXsNvhK'

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id='sundarpichai', tweet_mode ='extended').items(1)

for i in cursor:
    print(i.full_text)