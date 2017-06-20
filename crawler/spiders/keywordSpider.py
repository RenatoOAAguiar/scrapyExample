__author__ = 'tixie'
from scrapy.spiders import Spider
from crawler.common.searResultPages import searResultPages
from crawler.common.searchEngines import SearchEngineResultSelectors
from scrapy.selector import  Selector
import json
import re
import html2text

class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com','google.com','*.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None
    cont = 0

    def __init__(self, keyword, se = 'bing', pages = 1,  *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)
            

    def parse(self, response):
        body = Selector(response).xpath('//body//p//text()').extract()
        ## Dump the output to json file
        self.cont = self.cont + 1
        with open(self.cont + "texto.json", "wb") as outfile:
            json.dump({'url_body':body}, outfile, indent=4)
        for url in Selector(response).xpath(self.selector).extract():
            yield {'url':url}

        pass
