import scrapy
fileName= 'book_title.txt'
class IntroSpider(scrapy.Spider):
    name="IntroSpider"
    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            # 'http://books.toscrape.com/catalogue/page-3.html',
            # 'http://books.toscrape.com/catalogue/page-4.html',
            # 'http://books.toscrape.com/catalogue/page-5.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        book_list = response.css('article.product_pod > h3 > a::attr(title)').extract()

        with open(fileName, 'a')as f:
            for book_title in book_list:
                f.write(book_title + "\n")