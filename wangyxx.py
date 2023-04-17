import scrapy


class WangyxxSpider(scrapy.Spider):
    name = 'wangyxx'
    allowed_domains = ['qq.cn']
    start_urls = ['http://qq.cn/']

    def parse(self, response):
        pass
