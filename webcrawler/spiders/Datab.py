
import scrapy
import json

from scrapy.http import Request
from webcrawler.items import  WebcrawlerItem


class DatabSpider(scrapy.Spider):
    name = 'Datab'
    allowed_domains = ['trtworld.com']
    start_urls = ['http://trtworld.com/']

    def start_requests(self):
   

        with open('C:\\Users\\kleas\\OneDrive\\Έγγραφα\\Ceid\\10 ΕΠΙΛΟΓΗΣ\\Γλωσσική Τεχνολογία\\webcrawler\\article_link.json',) as json_file:
            data = json.load(json_file)
          

            for p in data:
                print('URL: ' + p['article_url'])

                request=Request(p['article_url'],cookies={'store_language':'en'},callback=self.parse_page)
               
                yield request
         
    def parse_page(self,response):

        item=WebcrawlerItem()

        

        item['article_title']=''.join(response.xpath('//div[@class="row tabletRow"]//h3[@class="article-description "]/text()').extract())
    

        item['article_body']=''.join(response.xpath('//div[@class="contentBox bg-w noMedia"]//p/text()').extract())
       
    
        yield(item)
   

        
    def parse(self, response):
        pass
