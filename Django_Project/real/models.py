from django.db import models

class Log(models.Model):
   enter = models.CharField(max_length=150)

   def __str__(self):
       return self.enter

class TweetData(models.Model):
   screenname = models.CharField(max_length=150)
   tweetid = models.IntegerField()
   postdate = models.DateTimeField()
   body = models.TextField()
   rt = models.IntegerField()
   likes = models.IntegerField()
   url = models.URLField()

   def __str__(self):
       return self.screenname