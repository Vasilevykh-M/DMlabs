import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'

    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        # Ищем все элементы с изображениями номеров
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }

            # Переход на следующую страницу (если есть)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)