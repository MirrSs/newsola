from dataclasses import dataclass
from newsapi import NewsApiClient
from loguru import logger

from news.models import LANGUAGE_CHOICE, CustomUser


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
    api = NewsApiClient(api_key='4db418996f7844b2a86bbf6df8c0ba79')
    user_lang = 'en'
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username = request.user.get_username())
        user_lang = user.language

        if user_lang =='ru' or user_lang == 'en' or user_lang == 'de' or user_lang =='es' or user_lang == 'fr' or user_lang == 'it':
            pass
        else:
            user_lang = 'en'
        logger.debug(user_lang)
    
    if cat=='general':
        news = api.get_top_headlines(language=str(user_lang),sources='bbc-news,associated-press,bbc-sport,cnn,google-news-ru,hacker-news,ign,lenta,polygon,reuters,techcrunch,')
    else:
        news = api.get_top_headlines(language=str(user_lang),category=cat)
    # top_headlines = newsapi.get_top_headlines(q='bitcoin',
    #                                       sources='bbc-news,the-verge',
    #                                       category='business',
    #                                       language='en',
    #                                       country='us')

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
            articles_list.append(record)
    logger.debug("Articles are added in list")
    return articles_list



