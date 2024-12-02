import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'


    allowed_domains = ['platesmania.com']
    start_urls = ['https://platesmania.com/gallery']


    def parse(self, response):
        # Ищем все элементы с изображениями номеров
        plates = response.css('div.gal-item')

        for plate in plates:
            # Получаем ссылку на изображение и страну
            img_url = plate.css('img::attr(src)').get()
            country = plate.css('span.flag::attr(title)').get()

            # Проверяем, что данные есть и формируем item
            yield {
                'image_url': img_url,
                'country': country,
            }

        # Для перехода к следующей странице, если они есть
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)