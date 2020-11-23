import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        base_url = 'https://www.goodreads.com'
        with open('books', 'r') as file:
            urls = [base_url + book_url for book_url in file]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'title': response.css('#bookTitle::text').get().strip(),
            'description': [' '.join(item.css('::text').getall()) for item in response.css('#description').css('span')],
            'book_id' : response.url.split('/')[-1],
            'language' : response.xpath('//div[@itemprop="inLanguage"]/text()').get(),
            'pages' : response.xpath('//span[@itemprop="numberOfPages"]/text()').re_first(r'\d+'),
            'authors' : response.xpath('//a[@class="authorName"]/span/text()').getall(),
            'rating' : response.xpath('//span[@itemprop="ratingValue"]/text()').get().strip(),
            'rating_count' : response.xpath('//meta[@itemprop="ratingCount"]/parent::a/text()').getall(),
            'review_count' : response.xpath('//meta[@itemprop="reviewCount"]/parent::a/text()').getall(),
            'shelves' : response.css('div.rightContainer').css('div.stacked').css('div.bigBoxBody').css('div.elementList').css('a::text').getall()
            }