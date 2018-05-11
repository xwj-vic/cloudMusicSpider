import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class CloudMusicImgsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['photo'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        else:
            item['image_path'] = image_paths
        return item
