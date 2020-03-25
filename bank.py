import json

import scrapy


class BankCodeSpider(scrapy.Spider):
    name = "BankCodeSpider"
    start_urls = ["https://www.atmbersama.com/layanan"]

    def parse(self, response):
        results = []
        for bank in response.css('.bank-item'):
            results.append({
                'icon': bank.css('.image img::attr(src)').get(),
                'name': str(bank.css('.text > .bank::text').get()).strip(),
                'code': str(bank.css('.text > .bankcode::text').get()).strip()
            })

        with open('results.json', 'w') as f:
            f.write(json.dumps(results))
