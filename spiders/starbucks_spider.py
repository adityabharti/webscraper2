import scrapy

from modified.items import StarbucksItem

class StarbucksSpider(scrapy.Spider):
    name = "starbucks"
    allowed_domains = ["starbucks.in"]
    start_urls = ["http://www.starbucks.in/coffeehouse/store-locations/"]
    
    def parse(self, response):
	for sel in response.xpath('//div[@class = "region size2of3"]/*[self::strong]'):
		item = StarbucksItem()
    		item['sublocality'] = sel.xpath('following-sibling::div[position() = 1  and not(starts-with(., "Timings"))]/text()').extract()
		item['locality'] = sel.xpath('following-sibling::div[position() = 2 and not(starts-with(., "Timings"))]/text()').extract()
		item['city'] = sel.xpath('following-sibling::div[position() = 3 and not(starts-with(., "Timings"))]/text()').extract()

		yield item
