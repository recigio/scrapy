# -*- coding: utf-8 -*-
from datetime import datetime
import re

import scrapy

from books.items import BooksItem


class BooksToscrapeComSpider(scrapy.Spider):

    name = 'books.toscrape.com'
    allowed_domains = ['books.toscrape.com']

    def __init__(self, *args, **kwargs):
        super(BooksToscrapeComSpider, self).__init__(*args, **kwargs)

        category = kwargs.get('category')
        if category:
            self.start_urls =['http://books.toscrape.com/catalogue/category/books/'+category+'/']
        else:
            self.start_urls =['http://books.toscrape.com/']

    def parse(self, response):
        for (i, book) in enumerate(response.css('.product_pod')):
            url_details = book.css('.image_container a::attr(href)').get()
            yield response.follow(url_details, self.parse_book)

        url = response.css('.pager .next a::attr(href)').get()

        if url is not None:
            yield response.follow(url)

    def parse_book(self, response):

        nome = response.css('.product_main').css('h1::text').get()
        preco = response.css('.product_main').css('.price_color::text').get().replace('£','')

        disponivel_selector = response.css('.product_main').css('.availability.instock')

        if disponivel_selector is not None:
            disponivel = True

            regex = re.compile('\d+')
            quantidade = regex.search(response.css('table tr:nth-child(6) td').get()).group()

        avaliacao = response.css('.star-rating').xpath("@class").get().replace('star-rating ', '')

        if avaliacao == 'One':
            avaliacao=1
        elif avaliacao == 'Two':
            avaliacao=2
        elif avaliacao == 'Three':
            avaliacao=3
        elif avaliacao == 'Four':
            avaliacao=4
        else:
            avaliacao=5

        categoria = response.css('.breadcrumb li:nth-child(3)').css('a::text').get()
        UPC = response.css('table tr:nth-child(1) td::text').get()
        url = response.request.url

        yield BooksItem(
            nome=nome,
            preco=float(preco),
            disponivel=disponivel,
            quantidade=int(quantidade),
            avaliacao=float(avaliacao),
            categoria=categoria,
            UPC=UPC,
            url=url,
            data=datetime.now().isoformat()
        )
