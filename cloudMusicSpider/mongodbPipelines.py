import pymongo
from scrapy.conf import settings

# 保存到mongodb
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self) -> None:
        self.url_set = set()

    def process_item(self, item, spider):
        if self.url_set.__contains__(item['url']):
            raise DropItem("重复:%s" % item)
        else:
            self.url_set.add(item['url'])
            self.coll.insert(dict(item))
            return item

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL']]

    def close_spider(self, spider):
        self.client.close()
