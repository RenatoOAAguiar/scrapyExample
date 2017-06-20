__author__ = 'tixie'
from scrapy.spiders import Spider
from crawler.common.searResultPages import searResultPages
from crawler.common.searchEngines import SearchEngineResultSelectors
from scrapy.selector import  Selector
import json
import re

class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com','google.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

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
        sel = Selector(response)
        google_search_links_list = sel.xpath('//h3/a/@href').extract()
        google_search_links_list = [re.search('q=(.*)&sa',n).group(1) for n in google_search_links_list]
        
        ## Dump the output to json file
        with open("texto", "w") as outfile:
            json.dump({'output_url':google_search_links_list}, outfile, indent=4)
        
        for url in Selector(response).xpath(self.selector).extract():
            #cont = cont + 1
            #file = open(str(cont) + '.txt', 'wb')
            #file.write(response.xpath('//body').extract())
            yield {'url':url}

        pass
