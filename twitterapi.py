import tweepy

class TwitterConnector:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret) #authenticate To Twitter
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth) #create connection to twitter api

    def update_status(self, message):
        self.api.update_status(message)

