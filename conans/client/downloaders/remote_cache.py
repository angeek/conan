import os

import six

from conans.client.downloaders.remote_cache_base import RemoteCacheBase
from conans.client.downloaders.remote_cache_artifactory import RemoteCacheArtifactory
 
# from conans.client.rest import response_to_str


class RemoteCache(object):
    def __init__(self, config):
        self._config = config
        self._remote_cache_manager = self.createRemoteCacheManager(self._config.remote_cache_type)

    def createRemoteCacheManager(self, cache_type):
        if cache_type == "artifactory" :
            return RemoteCacheArtifactory(self._config.remote_cache_url,self._config.remote_cache_usr,
                                          self._config.remote_cache_password)
        else :
            #TODO Implement other types of cache
            return None