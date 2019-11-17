import scrapy


class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    scrapy_date = scrapy.Field()
    url = scrapy.Field()
    rank = scrapy.Field()
