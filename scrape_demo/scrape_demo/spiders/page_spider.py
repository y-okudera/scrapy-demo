import datetime
import scrapy
import json


class PageSpiderSpider(scrapy.Spider):
    name = 'page_spider'
    allowed_domains = ['qiita.com']

    def start_requests(self):
        base_url = 'https://qiita.com/api/v2/items?page=1&per_page=10&query=user%3Ay-okudera'
        request_headers  = {
            'Content-Type': 'application/json',
        }
        yield scrapy.Request(url=base_url, headers=request_headers, callback=self.parse)

    def parse(self, response):
        json_response = json.loads(response.text)
        self.write_json(json_response)

    def write_json(self, json_response):
        now = datetime.datetime.now()
        filename = './output/log_' + now.strftime('%Y%m%d_%H%M%S') + '.json'
        with open(filename, 'w') as f:
            json.dump(json_response, f, indent=4)
