

'''
from Utils.Constants import *
import os
import time
import csv
import datetime


def write_deleted_pattern_2_csv(screen_name):

    list_memento_timestamps = []
    list_tweet_ids = []
    list_tweet_timestamps = []
    timestamp_considered = "20180314222933"

    for root, dirs, files in os.walk(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR):
        for f in files:
            if f.endswith(LIVE_TWEET_FILE_EXTENSION) and f.startswith(screen_name):
                list_memento_timestamps.append(f.split(".")[0].split("_")[1])
    list_memento_timestamps = sorted(list_memento_timestamps)
    with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + screen_name + UNDERSCORE_OPERATOR +
              timestamp_considered + LIVE_TWEET_FILE_EXTENSION) as file_object:
        for line in file_object:
            line_split = line.split("|")
            tweet_id = line_split[0].split(": ")[-1]
            list_tweet_ids.append(tweet_id)
            timestamp = line_split[1].split(": ")[-1]
            temp_timestamp = timestamp - (time.timezone)
            temp_timestamp = datetime.datetime.fromtimestamp(temp_timestamp).strftime('%Y/%m/%d')
            list_tweet_timestamps.append(temp_timestamp)
    idx = list_memento_timestamps.index(timestamp_considered)
    with open


    for timestamp in list_tweet_timestamps_millis:
        temp_timestamp = timestamp - (time.timezone)
        temp_timestamp = datetime.datetime.fromtimestamp(temp_timestamp).strftime('%Y/%m/%d')
        list_tweet_timestamps.append(temp_timestamp)
                
                with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + f) as file_object:
                    for line in file_object:
                        line_split = line.split("|")
                        tweet_id = line_split[0].split(": ")[-1]
                        if tweet_id in list_deleted_tweets:
                            
    if os.path.isfile(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "TweetLifeTime.csv"):
        csvfile = open(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "TweetLifeTime.csv", 'a+')
        fieldnames = ['TweetId']
        for tweet_ids in list_tweet_timestamps:
            fieldnames.append(tweet_ids)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    else:
        csvfile = open(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "TweetLifeTime.csv", 'w')
        fieldnames = ['TweetId']
        for tweet_ids in list_tweet_timestamps:
            fieldnames.append(tweet_ids)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    file_name = screen_name + UNDERSCORE_OPERATOR + list_memento_timestamps[0] + LIVE_TWEET_FILE_EXTENSION
    with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + file_name) as file_object:
        for line in file_object:

            list_tweet_timestamps.append(temp_timestamp)
    politowoops_tweets = {"Handle": screen_name, "TweetId": tweet_id, "Tweet": tweets_text, "Timestamp":
        tweet_timestamp, "TypoError": typo_error}
    try:
        writer.writerow(politowoops_tweets)
    except csv.Error as e:
        print(e)
    except Exception as e:
        print(e)

'''