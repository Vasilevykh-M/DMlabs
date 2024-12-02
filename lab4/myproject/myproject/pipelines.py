import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open('output.json', 'w', encoding='utf-8')
        self.writer = json.JSONEncoder()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        json.dump(item, self.file, ensure_ascii=False)
        self.file.write('\n')
        return item