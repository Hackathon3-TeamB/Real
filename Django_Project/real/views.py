from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import TweetData
from .forms import LogForm
from .tw import Tweet #追記部分

class TWU(View):
    def post(self, request):
        data = {"forms": LogForm,
               "TL":TweetData.objects.all()}
        form = LogForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        #ユーザー名
        u = post.enter

        #タイムラインを5件取得
        tl = Tweet(5)

        tld = tl.get_timeline(u)

        #データベースに登録をする

        for i in tld:
            TweetData.objects.create(screenname=i["screenname"], tweetid=i["ツイートID"], postdate=i["投稿日時"],
                                     body=i["text"], rt=i["RT数"], likes=i["いいね数"], url = i["url"])

        return render(request, 'real/index.html', data)
   

    def get(self, request):
        data = {"forms": LogForm,
                "TL": TweetData.objects.all()}

        return render(request,'real/index.html', data)
