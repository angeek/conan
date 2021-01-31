import os

from abc import ABCMeta, abstractmethod

class RemoteCacheBase(object):
    def __init__(self, config, output):
        self._output = output
        self._config = config
        self._loadConfig()

    @abstractmethod
    def _loadConfig(self):
        # Method to be overwritten by each implementation for loading configuration needed
        raise NotImplementedError()

    @abstractmethod
    def _getFileFromCache(self, url):
        # Method to be overwritten by each implementation to download from the remote cache
        # the requested resoure
        raise NotImplementedError()

    @abstractmethod
    def _saveToCache(self, url, sourceFile):
        # Method to be overwritten by each implementation to store in the cache
        raise NotImplementedError()