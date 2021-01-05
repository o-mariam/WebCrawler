import scrapy
from scrapy.http import Request
from webcrawler.items import  WebcrawlerItem

class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['trtworld.com']
    start_urls = ['http://trtworld.com/']


    def start_requests(self):

        url="https://www.trtworld.com/europe?page={}"
        

        link_urls = [url.format(i) for i in range(0,3)]
        for link_url in link_urls:
            print(link_url)

            request=Request(link_url,cookies={'store_language':'en'},callback=self.parse_main_pages)
            yield request
        
    def parse_main_pages(self,response):
        item=WebcrawlerItem()
        
        content=response.xpath('//div[@class="caption"]')
        for article_link in content.xpath('.//a[@class="gtm-topic-latest-article"]'):
            item['article_url'] =article_link.xpath('.//@href').extract_first()

            
            item['article_url'] ="https://www.trtworld.com"+item['article_url']
            yield item
   
    def parse(self, response):
     pass 




  