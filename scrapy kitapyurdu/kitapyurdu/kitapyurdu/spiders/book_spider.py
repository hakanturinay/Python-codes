import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_count = 0
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&page=1"
    ]
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        books_name = response.css("div.name.ellipsis a span::text").get()
        author_name = response.css("div.author.compact.ellipsis a::text").get()
        publisher_name = response.css("div.publisher a span::text").get.all()
        i = 0
        while(i<len(books_name)):
            yield {
                "name" : books_name[i],
                "author" : author_name[i],
                "publisher" : publisher_name[i],
            }
            i += 1