import os

from conans.client.downloaders.remote_cache_base import RemoteCacheBase

class RemoteCacheArtifactory(RemoteCacheBase):
    def __init__(self, url, usr = None, password = None):
        super(RemoteCacheArtifactory, self).__init__(url)
        self._usr = usr
        self._password = password