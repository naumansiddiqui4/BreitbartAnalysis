import twitter
import datetime
'''
Create Twitter Instance. All the fields can be collected from the developer site of Twitter
'''


def create_twitter_instance():
    api = twitter.Api(consumer_key='5Q3CFnvq02nKj6kI9gRpGNHXH',
                      consumer_secret='4OBnuBjedjwZUZmtslwzzPmWxeQtN7LHUeYHf4jsqZjQkEyW4v',
                      access_token_key='907341293717737473-for4ikiKhPAHxD54pnRqhJSPpr1QmNB',
                      access_token_secret='jV6TplxXfCQOu8C8zArB2wzlwGisq2Y0kRHUtrvuKYQNr',
                      sleep_on_rate_limit=True)
    return api


def convert_memento_time_millis(memento_time):
    memento_epoch_time = datetime.datetime.fromtimestamp(float(memento_time))
    memento_epoch_time = memento_epoch_time.strftime('%Y/%m/%d')
    return memento_epoch_time
