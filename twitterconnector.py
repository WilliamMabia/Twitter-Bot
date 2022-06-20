import tweepy
import logging

#Logging
logging.basicConfig(filename='logs/twitterconnector.log',level=logging.DEBUG) #Logging to file

class TwitterConnector:
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

        #authenticate To Twitter
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)

        #create connection to twitter api
        self.api = tweepy.API(self.auth) 

        logging.debug("TwitterConnector initialized")


    def tweet(self, message):
        self.api.update_status(message)
        logging.info("Tweeted: " + message)

