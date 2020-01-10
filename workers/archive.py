from queue import Queue
import json


def main(archive_q:Queue, path):
    while True:
        record = archive_q.get(block=True, timeout=None)
        file = open(path, 'a')
        file.write("{}\n".format(json.dumps(record.serialize())))