from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.shortcuts import redirect


def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
        post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    return HttpResponse(post_lists)


def newhomepage(request):
    posts = Post.objects.all()
    post_lists = list()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
