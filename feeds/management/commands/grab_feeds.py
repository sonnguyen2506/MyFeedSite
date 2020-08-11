import feedparser
import logging
from django.core.management.base import BaseCommand
#from feeds.models import Feed

import sqlite3
import pandas as pd

logger = logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('feedreader')

class Feed():
    def __init__(self, title, description, link, guid, pubDate):
        self.title = title
        self.description = description
        self.link = link
        self.guid = guid
        self.pubDate = pubDate

class Command(BaseCommand):
    help = 'Grab feeds from given urls to SQLite'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def parseFeeds(feed_url):
        return feedparser.parse(feed_url)

    def handle(self, *arg, **options):
        try:
            conn = sqlite3.connect('feed_db.sqlite3')
            feeds_urls = []

            #testing
            # feeds_urls = options['urls']

            for url in options['urls']:
                feeds_urls.append(url)
                #print(url)

            feedRows = []
            for url in feeds_urls.items(): #options['urls']
                print(url)
                feeds = feedparser.parse('https://www.feedforall.com/sample.xml')  # 'https://www.feedforall.com/sample.xml'
                for feed in feeds.entries:
                    #print(feed.title)
                    feedRows.append((feed.title, feed.link, '123', 'Today'))  # , feed.guid, feed.pubDate

            #Testing
            #print('Feeds Length: ' + str(len(feeds['entries'])))
            # print('Content of feedRows[]')
            # print(*feedRows, sep="\n")

            df = pd.DataFrame(feedRows, columns=['title','link','guid','pubDate']) #,'guid','pubDate'
            print("Grap feeds to df !")
            logger.info('Grap feeds to df !')

            # Save Feeds to SQLite
            df.to_sql(name='feeds_feed', con=conn, if_exists='append', index=False)
            conn.commit()
            print("Finished save feeds to db !")
            logger.info('Finished save feeds to db !')

            # Closing the connection
            conn.close()

        except Exception as e:
            logger.error("Exception occurred", exc_info=True)