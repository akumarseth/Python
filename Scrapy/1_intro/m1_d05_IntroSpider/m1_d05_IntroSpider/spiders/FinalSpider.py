import requests
from scrapy.http import Request

import scrapy
#from FinalSpider.items import Page  # Defined in items.py

URL = "http://url.com/PopUp.aspx?IDCoupon=%d"
starting_number = 60000
number_of_pages = 80

class FinalSpider(scrapy.Spider):
    name = "FinalSpider"
    allowed_domains = ['url.com']
    start_urls = ['url.com/=%d' % (n)
                  for n in range(0, 20)] #* #MEANS from 0 to 20

    def __init__(self):
        self.page_number = starting_number

    def start_requests(self):
        for i in range (self.page_number, number_of_pages, -1):
            yield scrapy.Request(url = URL % i, callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)