from CrawlBot import CrawlBot
import time

address_extensions = ['extension1', 'extension2']
for extension in address_extensions:
    cb = CrawlBot(f"www/address_to_hit={address_extensions}")
    time.sleep(5)