# -*- coding: utf-8 -*-
BOT_NAME = 'kabum'

SPIDER_MODULES = ['kabum.spiders']
NEWSPIDER_MODULE = 'kabum.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 ' \
             'Safari/537.36 '

DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 30

CONCURRENT_REQUESTS_PER_DOMAIN = 1

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 15
AUTOTHROTTLE_DEBUG = True

COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False

ITEM_PIPELINES = {
    'kabum.pipelines.MongoDBBrandCollectionsPipeline': 100,
}

MONGODB_URI = ''
MONGODB_DATABASE = 'kabum'
MONGODB_COLLECTION = 'products'
MONGODB_ADD_TIMESTAMP = True
MONGODB_UNIQUE_KEY = 'id'
