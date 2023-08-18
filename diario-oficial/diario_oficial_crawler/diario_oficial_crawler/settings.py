# Scrapy settings for diario_oficial_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "diario_oficial_crawler"

SPIDER_MODULES = ["diario_oficial_crawler.spiders"]
NEWSPIDER_MODULE = "diario_oficial_crawler.spiders"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
#Disable debug and verbose logging
LOG_LEVEL = 'INFO'
ITEM_PIPELINES = {"scrapy.pipelines.files.FilesPipeline": 1}
FILES_STORE = "pdfs"
