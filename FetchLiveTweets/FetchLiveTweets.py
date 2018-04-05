import os
import datetime
import twitter
from Utils.UtilityMethods import create_twitter_instance
from Utils.Constants import *


'''
Create file for live tweets fetched based on Twitter handle passed appended with the curent datetime stamp
'''


def create_livetweet_file(screen_name):
    try:
        # Check if live twitter outputs folder present or not
        if not os.path.exists(DIRECTORY_OUTPUTS):
            os.makedirs(DIRECTORY_OUTPUTS)

        # Check if live twitter outputs folder present or not
        if not os.path.exists(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR):
            os.makedirs(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR)

        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y%m%d%H%M%S")

        # Create text file for storing live tweets
        file_name = screen_name + UNDERSCORE_OPERATOR + timestamp + LIVE_TWEET_FILE_EXTENSION
        file_live_twitter = open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + file_name, "w")
        return file_live_twitter
    except Exception as err:
        print("create_livetweet_file: " + str(err))
        return


'''
Fetches recent 3200 tweets for the Twitter Handle 
'''


def get_timeline(screen_name):

    last_status_id = 0

    file_live_tweets = create_livetweet_file(screen_name)
    api = create_twitter_instance()

    # Get Timeline of the User

    while True and file_live_tweets is not None:
        try:
            if last_status_id == 0:
                twitter_response = api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=True)
                last_status_id = twitter_response[len(twitter_response) - 1].id
            else:
                twitter_response = api.GetUserTimeline(screen_name=screen_name, max_id=last_status_id, count=200)
                if last_status_id == twitter_response[len(twitter_response) - 1].id:
                    break
            last_status_id = twitter_response[len(twitter_response) - 1].id

            for k in twitter_response:

                # Insert to Database

                # Remove character undefined issue for encoding errors
                file_live_tweets.write("Id: " + str(k.id) + "|")
                file_live_tweets.write("Timestamp: " + str(k.created_at_in_seconds) + "|")

                file_live_tweets.write("Tweet Count: " + str(k.user.statuses_count) + "|")
                file_live_tweets.write("Follower Count: " + str(k.user.followers_count) + "|")
                file_live_tweets.write("Friend Count: " + str(k.user.friends_count) + "|")
                # Remove whitespace characters from Tweets
                if "\n" in k.text:
                    file_live_tweets.write("Tweet: " + k.text.replace("\n", " "))
                    file_live_tweets.write("\n")
                else:
                    file_live_tweets.write("Tweet: " + k.text)
                    file_live_tweets.write("\n")

        # Incase of error delete the live tweets output text file and remove the collection
        except twitter.error.TwitterError as err:
            print("Twitter Error: " + str(err))
            return

        except Exception as err:
            print("Error: " + str(err))
            return

    file_live_tweets.close()
