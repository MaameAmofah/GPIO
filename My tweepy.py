import tweepy

consumer_key = 'YV5nrdzb4WkWIEtf8tUgHGwA9'
consumer_secret = 'KFLsiXQMfdAMdy35evya6NZf3a2qSARlkyav9H164aRYMqmrLt'
access_token = '1405240339-Rk94h2jjuLka6jFMIa1vr2J14DhL23r2qJEBY3h'
access_token_secret = 'm8fp8cVJIWuP4Ftw0VYNpr6Nwula78m4WAuIpjfUAczEI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print (user.name)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    
user = api.home_profile()
print (followers)


user = api.followers
print (followers)
