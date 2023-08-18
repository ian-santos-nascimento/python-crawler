
BOT_NAME = "book_crawler"

SPIDER_MODULES = ["book_crawler.spiders"]
NEWSPIDER_MODULE = "book_crawler.spiders"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

