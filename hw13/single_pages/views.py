from django.shortcuts import render
import pandas as pd
from django.conf import settings
import os

# Create your views here.

def about_me(request):
    return render(
        request,
        "single_pages/landing.html"
    )

def landing(request):
    return render(
        request,
        "single_pages/about_me.html"
    )

def landing_page(request):
    return render(request, 'single_pages/index.html', {'title': 'home'})
def dodo_page(request):
    return render(request, 'single_pages/dodo.html', {'title': 'dodo'})
def flower_page(request):
    return render(request, 'single_pages/flower.html', {'title': '누룩 꽃 피는날'})
def king_page(request):
    return render(request, 'single_pages/king.html', {'title': 'king'})
def onedanggo_page(request):
    return render(request, 'single_pages/onedanggo.html', {'title': 'onedanggo'})
def posts_page(request):
    
    df = pd.read_csv('single_pages/data.csv')

    posts = []
    for i, row in df.iterrows():
        posts.append({
            "title": row['title'],
            "content": row['content']
        })
    
    return render(request, 'single_pages/posts.html', {'posts': posts})

def soba_page(request):
    return render(request, 'single_pages/so_ba.html', {'title': 'soba'})
def soonday_page(request):
    return render(request, 'single_pages/soonday.html', {'title': 'soonday'})



