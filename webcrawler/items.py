# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    article_title = scrapy.Field()
    article_url = scrapy.Field()
    article_body = scrapy.Field()
    pass
