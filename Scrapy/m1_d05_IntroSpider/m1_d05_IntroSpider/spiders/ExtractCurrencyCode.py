import scrapy
fileName = 'CurencyCode.csv'
class IntroSpider(scrapy.Spider):
    name="ExtractCurrencyCode"
    def start_requests(self):
        urls = [
            'https://www.iban.com/currency-codes',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        currencyCodeList = response.xpath('/ html/body/div[1]/div[2]/div/div/div/div/table/tbody/tr/td/text()').extract()
        with open(fileName, 'a+')as f:
            f.write('Country,Currency,Code,Number' + "\n")
            i=0;
            str='';
            for x in currencyCodeList:
                # f.write(x+'\n')
                if(i==0):
                    str += x + ','
                    i += 1;
                elif(i==1):
                    str += x + ','
                    i += 1;
                elif (i == 2):
                    str += x + ','
                    i += 1;
                elif (i == 3):
                    str += x
                    f.write(str + "\n")
                    str = ''
                    i=0






