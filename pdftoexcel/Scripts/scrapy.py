import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://www.example.com']

    def parse(self, response):
        # Extract and print the title of the page
        title = response.css('title::text').get()
        print(title)

        # Extract and print the text of the first paragraph
        first_paragraph = response.css('p::text').get()
        print(first_paragraph)