import os
import datetime
import time
from Utils.Constants import *


def convert_memento_timemillis(memento_time):
    memento_date = datetime.datetime.strptime(memento_time, "%Y%m%d%H%M%S")
    epoch = datetime.datetime.utcfromtimestamp(0)
    memento_epoch_time = int((memento_date - epoch).total_seconds())
    return memento_epoch_time


def convert_millis_to_time(milli_time):
    seconds = int(milli_time % 60)
    minutes = int((milli_time / 60) % 60)
    hours = int((milli_time / (60 * 60)) % 24)
    days = int((milli_time / (60 * 60 * 24)) % 30)
    return seconds, minutes, hours, days


def find_deleted_tweet_pattern(screen_name):

    list_memento_timestamps = []
    list_same_mementos = []
    list_same_mementos_count = []
    file_logs = open(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "Log.txt", "w")
    file_deleted_logs = open(DIRECTORY_OUTPUTS + screen_name + UNDERSCORE_OPERATOR + "Deleted_patternLog.txt", "w")
    # Fetch timestamp of all the mementos
    for root, dirs, files in os.walk(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR):
        for f in files:
            if f.endswith(LIVE_TWEET_FILE_EXTENSION) and f.startswith(screen_name):
                list_memento_timestamps.append(f.split(".")[0].split("_")[1])
    # Sort the memento timestamps
    list_memento_timestamps = sorted(list_memento_timestamps)
    print(str(list_memento_timestamps))
    print(len(list_memento_timestamps))
    # Traverse through the mementos to compare two consecutive mementos to find deleted tweets
    for idx in range(0, len(list_memento_timestamps)-1):
        file_1 = screen_name + UNDERSCORE_OPERATOR + list_memento_timestamps[idx] + LIVE_TWEET_FILE_EXTENSION
        file_2 = screen_name + UNDERSCORE_OPERATOR + list_memento_timestamps[idx + 1] + LIVE_TWEET_FILE_EXTENSION
        list_file1_tweet_id = []
        list_file2_tweet_id = []
        list_file1_tweet_timestamp = []
        list_file2_tweet_timestamp = []

        # Open the first memento
        with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + file_1) as file_prev:
            for line in file_prev:
                line_split = line.split("|")
                list_file1_tweet_id.append(line_split[0].split(": ")[-1])
                temp_timestamp = int(line_split[1].split(": ")[-1]) - (time.timezone)
                list_file1_tweet_timestamp.append(temp_timestamp)
        # Open the second memento
        with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + file_2) as file_next:
            for line in file_next:
                line_split = line.split("|")
                list_file2_tweet_id.append(line_split[0].split(": ")[-1])
                temp_timestamp = int(line_split[1].split(": ")[-1]) - (time.timezone)
                list_file2_tweet_timestamp.append(temp_timestamp)


        # Find the difference between memento 1 and memento 2
        diff_list = list(set(list_file1_tweet_id) - set(list_file2_tweet_id))
        # If the same tweets list is greater than 0 then delete the diff tweets from that list
        if len(list_same_mementos) > 0:
            for tweets in diff_list:
                if tweets in list_same_mementos:
                    index_temp = list_same_mementos.index(tweets)
                    list_same_mementos.remove(tweets)
                    list_same_mementos_count.pop(index_temp)
            for i in range(0, len(list_same_mementos_count)):
                list_same_mementos_count[i] += 1
        # Find the common tweets
        new_list_count = []
        new_list = list(set(list_file2_tweet_id) - set(list_file1_tweet_id))
        # Add the common tweets to same tweets list
        list_same_mementos.extend(new_list)
        for i in range(0, len(new_list)):
            new_list_count.append(1)
        list_same_mementos_count.extend(new_list_count)
        list_diff_tweet_timestamps = []
        list_diff_next_memento = []
        # Fetch timestamps for diff tweets
        if diff_list:
            for tweets in diff_list:
                index_tweets = list_file1_tweet_id.index(tweets)
                list_diff_tweet_timestamps.append(list_file1_tweet_timestamp[index_tweets])
                memento_timestamp = convert_memento_timemillis(list_memento_timestamps[idx + 1])
                list_diff_next_memento.append(int(memento_timestamp) - int(list_file1_tweet_timestamp[index_tweets]))
        else:
            for timestamps in list_file1_tweet_timestamp:
                memento_timestamp = convert_memento_timemillis(list_memento_timestamps[idx + 1])
                list_diff_next_memento.append(int(memento_timestamp) - int(timestamps))

        if list_diff_next_memento:
            min_time_diff = list_diff_next_memento[0]
            max_time_diff = list_diff_next_memento[0]
            for timestamp in list_diff_next_memento:
                if timestamp < min_time_diff:
                    min_time_diff = timestamp
                elif timestamp > max_time_diff:
                    max_time_diff = timestamp

        else:
            min_time_diff = 0
            max_time_diff = 0

        file_logs.write("\n\nTimestamp of previous tweet fetch using Twitter API: " + list_memento_timestamps[idx] +
                        "\n")
        file_logs.write("No. of tweets fetched using Twitter API: " + str(len(list_file1_tweet_id)) + "\n")
        file_logs.write("Timestamp of current tweet fetch using Twitter API : " + list_memento_timestamps[idx + 1] +
                        "\n")
        file_logs.write("No. of tweets fetched using Twitter API : " + str(len(list_file2_tweet_id)) + "\n")
        file_logs.write("Number of missing tweets from current tweet fetch vs previous tweet fetch: " +
                        str(len(diff_list)) + "\n")
        file_logs.write("New Tweets in Memento 2: " + str(len(new_list)) + "\n")
        file_logs.write("Count of tweets same as previous memento: " + str(len(list_file2_tweet_id) - len(new_list)) +
                        "\n")
        file_logs.write("Diff list: " + str(diff_list) + "\n")
        file_logs.write("Timestamp of Diff List: " + str(list_diff_tweet_timestamps) + "\n")
        file_logs.write("Time diff with next memento: " + str(list_diff_next_memento) + "\n")
        file_logs.write("Minimum Time difference od deleted tweets(in milliseconds): " + str(min_time_diff) + "\n")
        seconds, minutes, hours, days = convert_millis_to_time(min_time_diff)
        file_logs.write("Minimum Timestamp difference of deleted tweets with current time: " + str(days) + "days " +
                        str(hours) + " hours " + str(minutes) + "minutes " + str(seconds) + "seconds" + "\n")
        seconds, minutes, hours, days = convert_millis_to_time(max_time_diff)

        file_logs.write("Minimum Timestamp difference of deleted tweets with current time: " + str(days) + "days " +
                        str(hours) + " hours " + str(minutes) + "minutes " + str(seconds) + "seconds" + "\n")
    file_deleted_logs.write("Deletion pattern: \n\n")
    for i in range(0, len(list_same_mementos)):
        index_temp = list_file1_tweet_id.index(list_same_mementos[i])
        if list_same_mementos[i] == "980217260487991298":
            print(list_file1_tweet_timestamp[index_temp])
        time_diff = int(convert_memento_timemillis(list_memento_timestamps[len(list_memento_timestamps) - 1])) - \
                    int(list_file1_tweet_timestamp[index_temp])
        seconds, minutes, hours, days = convert_millis_to_time(time_diff)
        file_deleted_logs.write( str(list_same_mementos[i]) + "   " + str(list_same_mementos_count[i]) + "  " +
                                 str(days) + "days " + str(hours) + " hours " + str(minutes) + "minutes " +
                                 str(seconds) + "seconds" + "\n")


def write_tweets_to_csv(list_memento_timestamps, screen_name):

    for root, dirs, files in os.walk(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR):
        for f in files:
            if f.endswith(LIVE_TWEET_FILE_EXTENSION) and f.startswith(screen_name):
                list_tweet_id = []
                list_tweet_timestamp = []
                with open(DIRECTORY_OUTPUTS + screen_name + FORWARD_SLASH_OPERATOR + f) as file_next:
                    for line in file_next:
                        line_split = line.split("|")
                        list_tweet_id.append(line_split[0].split(": ")[-1])
                        list_tweet_timestamp.append(line_split[1].split(": ")[-1])

