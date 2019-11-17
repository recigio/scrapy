BOT_NAME = 'quotes'

SPIDER_MODULES = ['quotes.spiders']
NEWSPIDER_MODULE = 'quotes.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'quotes (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 15

AUTOTHROTTLE_ENABLED = True