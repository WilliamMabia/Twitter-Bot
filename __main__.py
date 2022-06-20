import passes
from twitterconnector import *



def main():
    consumer_key, consumer_secret, access_token, access_secret = passes.get_passes()
    api = TwitterConnector(consumer_key, consumer_secret, access_token, access_secret)

    message = ("Updated from Main")
    api.tweet(message)

    print("successful")

main()

