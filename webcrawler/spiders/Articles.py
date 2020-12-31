import scrapy
from scrapy.http import Request
from webcrawler.items import  WebcrawlerItem

class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['vox.com']
    start_urls = ['https://www.vox.com']


    def start_requests(self):

        url="https://www.vox.com/news/?page={}"

        link_urls = [url.format(i) for i in range(0,100)]
        for link_url in link_urls:
            print(link_url)

            request=Request(link_url,cookies={'store_language':'en'},callback=self.parse_main_pages)
            yield request
        
    def parse_main_pages(self,response):
        item=WebcrawlerItem()
        
        content=response.xpath('//div[@class="c-entry-box--compact__body"]')
        for article_link in content.xpath('.//h2[@class="c-entry-box--compact__title"]//a'):
            item['article_url'] =article_link.xpath('.//@href').extract_first()

            item['article_url'] =  item['article_url']
            yield(item)
            
        
            next_page = response.xpath('//div[@class="c-pagination__next c-pagination__link p-button"]//@href').extract_first()     
            if next_page is not None:
                yield scrapy.Request("https://www.vox.com/" + next_page, callback=self.parse)


    def parse(self, response):
     pass 





  