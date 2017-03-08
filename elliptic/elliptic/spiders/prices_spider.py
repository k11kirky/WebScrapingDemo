import scrapy
import unicodedata

class PricesSpider(scrapy.Spider):
    name = "prices"

    def start_requests(self):
        urls = [
            'https://cex.io/btc-usd'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'price_output.txt'
        with open(filename, 'wb') as f:
            for row in response.xpath('//*[@id="pairs"]'):
                for tr in row.xpath('.//li'):
                    name = tr.xpath('.//a/text()').extract()[0].encode('ascii', 'ignore')
                    price = tr.xpath('.//a/span/text()').extract()[0].encode('ascii', 'ignore')
                    f.write('Name: ' + name + '\n')
                    f.write('Price: ' + price + '\n\n')
        self.log('Saved file %s' % filename)