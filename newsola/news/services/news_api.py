from dataclasses import dataclass
from newsapi import NewsApiClient
from loguru import logger
import datetime
import requests

from news.models import LANGUAGE_CHOICE, CustomUser

LANGS = ('ru','en','es','de','fr','it')
api = NewsApiClient(api_key='4db418996f7844b2a86bbf6df8c0ba79')

@dataclass
class Record:
    title:str
    description:str
    url:str
    urlToImage:str
    pub_date:str

    def __str__(self):
        return  self.title + self.description


def get_headlines(request,cat:str = 'general') -> list:
    user_lang = 'en'
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username = request.user.get_username())
        user_lang = user.language

        if user_lang in LANGS:
            pass
        else:
            user_lang = 'en'
        logger.debug(user_lang)
    
    with requests.Session() as session:
        if cat=='general':
            # news_headlines = api.get_top_headlines(language=str(user_lang),sources='bbc-news,associated-press,bbc-sport,cnn,google-news-ru,hacker-news,ign,lenta,polygon,reuters,techcrunch,')
            news = api.get_everything(language=str(user_lang),page_size=30,domains='techcrunch.com,dtf.ru,pikabu.ru,bbc.com,medium.com,ign.com,thehackernews.com,lenta.ru,polygon.com,reuters.com,techcrunch.com,ria.ru,ru.euronews.com,sputnik.by,belta.by')
        else:
            news = api.get_top_headlines(language=str(user_lang),category=cat,page_size=20)
            #news_everything = api.get_everything(language=str(user_lang),category=cat,domains='techcrunch.com,dtf.ru,pikabu.ru,bbc.com,medium.com')
            

    if(news.get('status')=='ok'):
        logger.debug("NewsAPI request status:OK")
        articles = news.get('articles')
        articles_list = []
        
        for article in articles:
            title = article.get('title')
            desc = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            pub_date = article.get('publishedAt')
            if urlToImage == None:
                continue
            record = Record(title,desc,url,urlToImage,pub_date)
            if len(articles_list) >= 35:
                break
            articles_list.append(record)
    logger.debug("Articles are added in list")
    return articles_list

#Search
def search_news(request,str_to_search:str) -> list:
    user_lang = 'en'
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username = request.user.get_username())
        user_lang = user.language

        if user_lang in LANGS:
            pass
        else:
            user_lang = 'en'
        logger.debug(user_lang)
    
        current_date = datetime.datetime.now()
        date_delta = datetime.timedelta(days = 7)
        seven_days_ago_date = current_date - date_delta

    with requests.Session() as session:
        news = api.get_everything(page_size=10,q=str_to_search,from_param=seven_days_ago_date.strftime('%Y-%m-%d'),to=current_date.strftime('%Y-%m-%d'))
            
    if(news.get('status')=='ok'):
        logger.debug("NewsAPI request status:OK")
        articles = news.get('articles')
        articles_list = []
        
        for article in articles:
            title = article.get('title')
            desc = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            pub_date = article.get('publishedAt')
            if urlToImage == None:
                continue
            record = Record(title,desc,url,urlToImage,pub_date)
            if len(articles_list) >= 35:
                break
            articles_list.append(record)
    logger.debug("Articles are added in list")
    return articles_list
    



