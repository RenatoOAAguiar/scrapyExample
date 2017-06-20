__author__ = 'tixie'
from scrapy.spiders import Spider
from crawler.common.searResultPages import searResultPages
from crawler.common.searchEngines import SearchEngineResultSelectors
from scrapy.selector import  Selector
import json

class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com','google.com','baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None


    def __init__(self, keyword, se = 'bing', pages = 50,  *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)

    def parse(self, response):
        for html in Selector(response).xpath('//html//text()').extract():
            with open("texto.json", "w") as outfile:
                json.dump({'html':html}, outfile)
                
        for url in Selector(response).xpath(self.selector).extract():
            yield {'url':url}

        pass