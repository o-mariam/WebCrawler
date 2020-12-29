import scrapy
from scrapy.http import Request
from webcrawler.items import  WebcrawlerItem

import json

class DatabSpider(scrapy.Spider):
    name = 'Datab'
    allowed_domains = ['bbc.co.uk']
    start_urls = ['https://www.bbc.co.uk']

def start_requests(self):
   

    with open("C:\\Users\\kleas\\OneDrive\\Έγγραφα\\Ceid\\10 ΕΠΙΛΟΓΗΣ\\Γλωσσική Τεχνολογία\\webcrawler\\article_links.json",r) as json_file:
        data = json.load(json_file)

    for p in data:
        print('URL: ' + p['article_url'])

        request=Request(p['article_url'],cookies={'store_language':'en'},callback=self.parse_article_page)
    yield request
         
def parse_article_page(self,response):

    item=WebcrawlerItem()


    item['article_title']=response.xpath('//div[@class="css-uf6wea-RichTextComponentWrapper e1xue1i83"]//h1[@class="css-1pl2zfy-StyledHeading e1fj1fc10"]/text()').extract();
    

    item['article_body']=response.xpath('//div[@class="css-uf6wea-RichTextComponentWrapper e1xue1i83"]//p/text()').extract();
    
    yield(item)
   

        
def parse(self, response):
  pass

