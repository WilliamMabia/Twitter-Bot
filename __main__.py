from pwd import get_passes
from twitterapi import *


def main():
    consumer_key, consumer_secret, access_token, access_secret = get_passes()
    api = TwitterConnector(consumer_key, consumer_secret, access_token, access_secret)

    message = ("Updated from Main")
    api.update_status(message)
