import scrapy


class CloudmusicspiderItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    url = scrapy.Field()  # 链接
    listener = scrapy.Field()  # 人数
    author = scrapy.Field()  # 作者
    photo = scrapy.Field()  # 图片
