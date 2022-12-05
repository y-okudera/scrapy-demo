import json
import scrapy


class QiitaItemsSpider(scrapy.Spider):
    name = 'qiita_items'
    allowed_domains = ['qiita.com']

    def start_requests(self):
        base_url = 'https://qiita.com/api/v2/items?page=1&per_page=100&query=Python'
        request_headers = {
            'Content-Type': 'application/json',
        }
        yield scrapy.Request(url=base_url, headers=request_headers, callback=self.parse)

    def parse(self, response):
        json_response = json.loads(response.text)
        for article in json_response:
            id = article['id']
            title = article['title']
            likes_count = article['likes_count']
            yield {
                'id': id,
                'title': title,
                'likes_count': likes_count
            }
