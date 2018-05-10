from scrapy.exceptions import DropItem
import json

# 保存到文件
class CloudmusicspiderPipeline(object):

    def __init__(self) -> None:
        self.file = open('data.json', 'w', encoding='utf-8')
        self.ids_seen = set()

    def process_item(self, item, spider):
        if self.ids_seen.__contains__(item['url']):
            raise DropItem("重复:%s" % item)
        else:
            self.ids_seen.add(item['url'])
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            # return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
