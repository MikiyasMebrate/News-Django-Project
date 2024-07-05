from django.shortcuts import render
from .models import News, Team, About, Contact, SocialMedia
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
def homepage(request):
    sport = News.objects.filter(category = 2)
    technology = News.objects.filter(category = 4)
    music = News.objects.filter(category = 7)
    politics = News.objects.filter(category = 6)
     
    top_politics = []
    dashboard_politics = []
    
    for iterate,news in enumerate(politics):
        if  iterate < 2:
            top_politics.append(news)
        elif iterate > 1:
            dashboard_politics.append(news)
        if iterate == 6: break

    top_news = []
    for iterate,news in enumerate( News.objects.all()):
        top_news.append(news)
        if iterate == 5: break
    
    header_news = []
    for iterate,news in enumerate( News.objects.all()):
        header_news.append(news)
        if iterate == 10: break

    latest_posts = []
    for iterate,news in enumerate( News.objects.all()):
        news.description = news.description[0:75]
        latest_posts.append(news)
        if iterate == 1: break


    context = {
        'all_news' : top_news,
        'sports' : sport,
        'technologies' : technology,
        'musics' : music,
        'politics' : top_politics,
        'politics_dash' : dashboard_politics,
        'latest_posts' : latest_posts,
        'header' : header_news
    }
    return render(request, 'base/index.html', context)

def about(request):
    # send_mail(
    #     "Django",
    #     "Test From Django Project.",
    #     "mikiyasmebrate2656@gmail.com",
    #     ["mikiyasmebrate@gmail.com"],
    #     fail_silently=False,
    # )
    header_news = []
    for iterate,news in enumerate( News.objects.all()):
        header_news.append(news)
        if iterate == 10: break

    context = {
        'teams' : Team.objects.all(),
        'content' : About.objects.all(),
        'header' : header_news
    }
    return render(request, "base/about-us.html",context)

def contact(request):
    header_news = []
    for iterate,news in enumerate( News.objects.all()):
        header_news.append(news)
        if iterate == 10: break

    context = {
        'contact' : Contact.objects.get(id = 1),
        'social_media' : SocialMedia.objects.all(),
        'header' : header_news
        
    }
    return render(request, 'base/contact.html', context)

def detail_news(request, pk):
    news = News.objects.get(id=pk)

    top_news = []
    for iterate,news_like in enumerate( News.objects.all()):
        top_news.append(news_like)
        if iterate == 5: break

    header_news = []
    for iterate,news_header in enumerate( News.objects.all()):
        header_news.append(news_header)
        if iterate == 10: break

    context = {
        'news' : news,
        'news_like' : top_news,
        'header' : header_news
    }

    return render(request, 'base/detail_news.html', context)





def homepage_json(request):
    latest_post = list( News.objects.all().values()[:3])
    context = {
        'latest_post' : latest_post
    }
    return JsonResponse(context)


