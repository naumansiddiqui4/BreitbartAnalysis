import os
import datetime
import twitter

from Utils.Constants import *
from Utils.UtilityMethods import create_twitter_instance


def get_retweet_people_list(screen_name, list_tweet_ids):

    if os.path.isfile(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "Tweet_Status.txt"):
        file_tweet_status = open(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "Tweet_Status.txt", "a+")
    else:
        file_tweet_status = open(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "Tweet_Status.txt", "w")

    api = create_twitter_instance()
    for tweet_id in list_tweet_ids:
        try:
            response = api.GetStatus(tweet_id)
            file_tweet_status.write("Current Timestamp: " + str(datetime.datetime.now()) + "\n")
            file_tweet_status.write(str(response) + "\n\n")
        except twitter.error.TwitterError as err:
            file_tweet_status.write("Current Timestamp: " + str(datetime.datetime.now()) + "\n")
            file_tweet_status.write(str(err) + "\n\n")

    file_tweet_status.close()