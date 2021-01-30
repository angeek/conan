import os

class RemoteCacheBase(object):
    def __init__(self, url):
        self._url = url

    def download(self, urlToDowload):
        pass

    def upload(self):
        pass
