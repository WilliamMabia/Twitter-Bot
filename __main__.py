import authentication
from twitterconnector import *



def main():
    # Get the latest pass from the passes.py file
    consumer_key, consumer_secret, access_token, access_secret = authentication.get_passes()

    # Create a new TwitterConnector object to connect to twitter API and use custom API functions
    api = TwitterConnector(consumer_key, consumer_secret, access_token, access_secret)

    message = ("Testing TwitterConnector")
    api.tweet(message)


main()

