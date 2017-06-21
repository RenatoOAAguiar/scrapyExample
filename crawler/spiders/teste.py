import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.google.com.br/?gws_rd=ssl#q=37640083000193']

    def parse(self, response):
        for title in response.css('body'):
            yield {
            'endereco': title.css('body ::text').extract()
            }

        for next_page in response.css('h3.r > a'):
            yield response.follow(next_page, self.parse)