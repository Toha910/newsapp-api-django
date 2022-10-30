from django.shortcuts import render
import requests

API_KEY = '9ef19887b3fe479d954c17be1d684a25'  


def index(request):

    # search for the keyword by country
    country_search = request.GET.get('country-search')
    category_search = request.GET.get('category-search')
    if country_search:
        url = f'https://newsapi.org/v2/top-headlines?country={country_search}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category_search:
        url = f'https://newsapi.org/v2/top-headlines?category={category_search}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles,
    }

    return render(request, 'index.html', context)
