import twitter
import datetime
'''
Create Twitter Instance. All the fields can be collected from the developer site of Twitter
'''


def create_twitter_instance():
    api = twitter.Api(consumer_key='xxxxxxxx',
                      consumer_secret='xxxxxxx',
                      access_token_key='xxxxxxx',
                      access_token_secret='xxxxxxxx',
                      sleep_on_rate_limit=True)
    return api


def convert_memento_time_millis(memento_time):
    memento_epoch_time = datetime.datetime.fromtimestamp(float(memento_time))
    memento_epoch_time = memento_epoch_time.strftime('%Y/%m/%d')
    return memento_epoch_time
