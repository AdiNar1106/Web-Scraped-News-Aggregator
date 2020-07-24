from django.urls import path
from news.views import web_scraper, get_news

urlpatterns = [
  path('web_scraper/', web_scraper, name="web_scraper"),
  path('', get_news, name="home"),
]
