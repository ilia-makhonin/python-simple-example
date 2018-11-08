import os
import urllib.request
from threading import Thread

class DownloadThread(Thread):
    def __init__(self, name, url):
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        handle = urllib.request.urlopen(self.url)
        fname = 'download/' + os.path.basename(self.url)

        with open(fname, 'wb') as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = '%s закончил загрузку %s' % (self.name, self.url)
        print(msg)

def download_thread(urls):
    for item, url in enumerate(urls):
        name = 'Поток %s' % (item + 1)
        thread = DownloadThread(name, url)
        thread.start()