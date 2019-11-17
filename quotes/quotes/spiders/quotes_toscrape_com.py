from datetime import datetime

import scrapy

from quotes.items import QuotesItem

class QuotesToscrapeComSpider(scrapy.Spider):
    name = 'quotes.toscrape.com'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for (i,quote) in enumerate(response.css('.quote')):
            text = quote.css('span.text::text').get()
            author = quote.css('.author::text').get()

            yield QuotesItem(
                text=text,
                author=author,
                url=response.url,
                rank=i,
                scrapy_date=datetime.now().isoformat()
            )

        url = response.css('.pager .next a::attr(href)').get()

        if url is not None:
            yield response.follow(url)

    #def start_requests(self):
     #   yeld
     #   for url in self.start_urls:
