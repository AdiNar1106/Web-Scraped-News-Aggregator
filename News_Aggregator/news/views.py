from django.shortcuts import render, redirect
import requests as r
from bs4 import BeautifulSoup
from news.models import Headline
# Create your views here.

def web_scraper(request):
	session = r.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    news = soup.find_all('div', {"class":"curation-module__item"})

    for article in news:
    	main = article.find_all('a')[0]
    	link = main['href']
    	img_src = str(main.find('img')['srcset']).split(" ")[-4]
    	title = main['title']
    	new_headline = Headline()
    	new_headline.title = title
    	new_headline.url = link
    	new_headline.image = img_src
    	new_headline.save()

    return redirect("../")

def get_news(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)
