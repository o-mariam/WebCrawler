
import scrapy
import json

from scrapy.http import Request
from webcrawler.items import  WebcrawlerItem


class DatabSpider(scrapy.Spider):
    name = 'Datab'
    allowed_domains = ['vox.com']
    start_urls = ['https://www.vox.com']

    def start_requests(self):
   

        with open('C:\\Users\\kleas\\OneDrive\\Έγγραφα\\Ceid\\10 ΕΠΙΛΟΓΗΣ\\Γλωσσική Τεχνολογία\\webcrawler\\article_links.json',) as json_file:
            data = json.load(json_file)
          

            for p in data:
                print('URL: ' + p['article_url'])

                request=Request(p['article_url'],cookies={'store_language':'en'},callback=self.parse_article_page)
               
                yield request
         
    def parse_article_page(self,response):

        item=WebcrawlerItem()


        item['article_title']=response.xpath('//h1[@class="c-page-title"]/text()').extract()
    

        item['article_body']=response.xpath('//div[@class="c-entry-content "]//p/text()').extract()
        item['article_body']="".join( item['article_body'])
    
        yield(item)
   

        
    def parse(self, response):
        pass
