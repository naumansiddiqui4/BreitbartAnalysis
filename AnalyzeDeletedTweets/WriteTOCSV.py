import csv
import os
from Utils.Constants import *
from Utils.UtilityMethods import convert_memento_time_millis


def write_to_csv(screen_name):
    list_memento_timestamps = []
    list_tweets_data = []

    for root, dirs, files in os.walk(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR):
        for f in files:
            if f.endswith(LIVE_TWEET_FILE_EXTENSION) and f.startswith(screen_name):
                list_memento_timestamps.append(f.split(".")[0].split("_")[1])
    list_memento_timestamps = sorted(list_memento_timestamps)
    for timestamps in list_memento_timestamps:
        list_tweet_ids = []
        with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + screen_name + UNDERSCORE_OPERATOR +
                  timestamps + LIVE_TWEET_FILE_EXTENSION) as file_object:
                for line in file_object:
                    line_split = line.split("|")
                    if timestamps == list_memento_timestamps[0]:
                        tweet_dictionary = {"TweetId": str(line_split[0].split(": ")[-1]), "Start":
                            convert_memento_time_millis(line_split[1].split(": ")[-1])}
                        list_tweets_data.append(tweet_dictionary)
                    list_tweet_ids.append(line_split[0].split(": ")[-1])
        for tweet_data in list_tweets_data:
            if tweet_data["TweetId"] not in list_tweet_ids and "End" not in tweet_data.keys():
                end_time = timestamps[:4] + FORWARD_SLASH_OPERATOR + timestamps[4:6] + FORWARD_SLASH_OPERATOR + \
                           timestamps[6:8]
                tweet_data["End"] = end_time
    print(list_tweets_data)
    csv_file = open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + screen_name + "_pattern.csv", 'w')
    fieldnames = ['TweetId', 'Start', 'End']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for tweet_data in list_tweets_data:
        writer.writerow(tweet_data)
    csv_file.close()