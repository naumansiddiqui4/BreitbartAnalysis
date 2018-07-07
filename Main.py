from AnalyzeDeletedTweets.FindTweetDeletionPattern import find_deleted_tweet_pattern
from AnalyzeDeletedTweets.FindTweetStatus import get_retweet_people_list
from AnalyzeDeletedTweets.WriteTOCSV import write_to_csv

from FetchLiveTweets.FetchLiveTweets import get_timeline


def main(screen_handle):

    '''
    is_pattern_found = True
    if not is_pattern_found:
        get_timeline(screen_handle)
        find_deleted_tweet_pattern(screen_handle)

    is_tweet_status_found = True
    if not is_tweet_status_found:
        list_tweet_ids = ["976194605791268865", "976197398459535361", "976521157741547520", "976798242913619970",
                          "977266998047641600"]
        get_retweet_people_list(screen_handle, list_tweet_ids)
    '''

    write_to_csv(screen_handle)


if __name__ == "__main__":
    # main("NolteNC")
    main("carney")