import tweepy  #記事にはない追記部分
import os
Consumer_key = os.environ.get('Consumer_key')
Consumer_secret = os.environ.get('Consumer_secret')
Access_token = os.environ.get('Access_token')
Access_secret = os.environ.get('Access_secret')
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

class TweeterMain:
  def __init__(self):

      self.api = tweepy.API(auth)

  def timeline_screen(self, user, num):
      tweets = []

      # タイムライン
      for status in tweepy.Cursor(self.api.user_timeline, screen_name=user).items(num):
          tweets.append({"screenname": status.user.screen_name, "ツイートID": status.id, "投稿日時": str(status.created_at),
                         "text": status.text, "RT数": status.retweet_count, "いいね数": status.favorite_count,
                         "url": "<https://twitter.com/twitter/statuses/>" + str(status.id)})

      return tweets

class Tweet:

   def __init__(self, num):
       self.t = TweeterMain()
       self.tweets = []
       self.num = num

   def get_timeline(self, name):

          for i in (self.t.timeline_screen(name, self.num)):
              #print(i)
              self.tweets.append(i)

          return self.tweets