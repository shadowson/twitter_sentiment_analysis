from workers.twitter_query import main as twitter_query
from workers.tweet_processor import main as tweet_processor
from workers.archive import main as archiver
from queue import Queue
import threading
import os


def main(query, limit, interval, path):
    threads = []
    tweet_q = Queue(maxsize=0)
    archive_q = Queue(maxsize=0)

    threads.append(threading.Thread(target=twitter_query, args=(query, limit, tweet_q, interval)))
    threads.append(threading.Thread(target=tweet_processor, args=(tweet_q, archive_q)))
    threads.append(threading.Thread(target=archiver, args=(archive_q, path)))
    for thread in threads:
        thread.start()

if __name__ == '__main__':
    log_path = os.path.join(os.path.dirname(__file__), 'tweet_records.txt')

    main(
        query="@Everbridge (-from:Everbridge) (-from:EBHealthcare)",
        limit=100,
        interval=10,
        path=log_path
    )
