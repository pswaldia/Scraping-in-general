# -*- coding: utf-8 -*-
import scrapy
from ..items import DlbooksItem

class DlScrapperSpider(scrapy.Spider):
    name = 'dl-scrapper'
    start_urls = ['https://www.flipkart.com/search?q=deep+learning+books&otracker=AS_Query_HistoryAutoSuggest_1_0&otracker1=AS_Query_HistoryAutoSuggest_1_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY']
    page_num=2
    def parse(self, response):
        items=DlbooksItem()
        
        all_div=response.css('._1R0K0g')
        for book in all_div:
            name=book.css('._2cLu-l::text').extract()
            author=book.css('._1rcHFq::text').extract()
            price=book.css('._1vC4OE::text').extract()
            items['name']=name
            items['author']=author[0].split(',')[2:]
            items['price']=price[0][1:]
            yield items

            next_page='https://www.flipkart.com/search?q=deep+learning+books&otracker=AS_Query_HistoryAutoSuggest_1_0&otracker1=AS_Query_HistoryAutoSuggest_1_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page='+str(DlScrapperSpider.page_num)

            if(DlScrapperSpider.page_num<=4):
                yield response.follow(next_page,callback=self.parse)
        


        
