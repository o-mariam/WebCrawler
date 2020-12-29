import scrapy
from scrapy.http import Request
from webcrawler.items import  WebcrawlerItem

class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['bbc.co.uk']
    start_urls = ['https://www.bbc.co.uk']


    def start_requests(self):

        url="https://www.bbc.co.uk/news/?page={}"

        link_urls = [url.format(i) for i in range(0,100)]
        for link_url in link_urls:
            print(link_url)

            request=Request(link_url,cookies={'store_language':'en'},callback=self.parse_main_pages)
            yield request
        
    def parse_main_pages(self,response):
        item=WebcrawlerItem()

        content=response.xpath('//div[@id="latest-stories-tab-container"]')
        for article_link in content.xpath('.//a[@class="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"]'):
            item['article_url'] =article_link.xpath('.//@href').extract_first()

            item['article_url'] = "https://www.bbc.co.uk" + item['article_url']
            yield(item)


    def parse(self, response):
     pass 





  