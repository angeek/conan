import os

import six

from conans.client.downloaders.remote_cache_base import RemoteCacheBase
from conans.client.downloaders.remote_cache_artifactory import RemoteCacheArtifactory
 
# from conans.client.rest import response_to_str


class RemoteCache(object):
    def __init__(self, config, output):
        self._config = config
        self._output = output
        self._remote_cache_manager = self.createRemoteCacheManager()

    def createRemoteCacheManager(self):
        if self._config.remote_cache_type.lower() == "artifactory" :
            self._output.info("Creating Remote Cache for artifactory")
            return RemoteCacheArtifactory(self._config, self._output)
        else :
            #TODO Implement other types of cache
            return None
    def saveToCache(self, url, filePathToSave):
        self._remote_cache_manager._saveToCache(url, sourceFile = filePathToSave)

    def getFromRemoteCache(self, url):
        return self._remote_cache_manager._getFileFromCache(url)