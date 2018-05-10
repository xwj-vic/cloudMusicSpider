import scrapy

from cloudMusicSpider.items import CloudmusicspiderItem


class MusicSpider(scrapy.Spider):
    name = "CloudMusicSpider"
    allowed_domains = ["music.163.com"]
    start_urls = ["http://music.163.com/#/discover/playlist/?order=hot",
                  "http://music.163.com/#/discover/playlist/?order=new"]

    def parse(self, response):
        item = CloudmusicspiderItem()
        for body in response.xpath('//ul[@id="m-pl-container"]/li'):
            for itemNode in body.xpath('.//p[@class="dec"]/a'):
                item['url'] = 'http://music.163.com/#' + itemNode.xpath('.//@href').extract()[0].strip()
                item['title'] = itemNode.xpath('.//text()').extract()[0].strip()
            for itemNode2 in body.xpath('.//div[@class="u-cover u-cover-1"]'):
                item['listener'] = itemNode2.xpath('.//div/span[@class="nb"]/text()').extract()[0].strip()
                item['photo'] = itemNode2.xpath('.//img/@src').extract()[0].strip()
            item['author'] = body.xpath('.//p[last()]/a/text()').extract()[0].strip()
            yield item
        url = response.xpath('//div[@class="u-page"]/a[@class="zbtn znxt"]/@href').extract()
        if url:
            page = 'http://music.163.com/#' + url[0]
            yield scrapy.Request(page, callback=self.parse, dont_filter=True)
