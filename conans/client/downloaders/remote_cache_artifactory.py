import os

from conans.client.downloaders.remote_cache_base import RemoteCacheBase

class RemoteCacheArtifactory(RemoteCacheBase):
    def __init__(self, config, output):
        self._output = output
        super(RemoteCacheArtifactory, self).__init__(config, output)

    def _loadConfig(self):
        # This part is where each implementation gather the config needed
        self._user = self._config.remote_cache_usr
        self._endpoint = self._config.remote_cache_endpoint
        self._password = self._config.remote_cache_password
        
    def _getFileFromCache(self, url):
        # In this part of the code, the  passed as an argument, will be search in the remote server.
        # The return object should be the filePath of the downloaded resource (usually Temporary as 
        # as later it will be stored in the LocalCache -already in place-) 
        pass

    def _saveToCache(self, url, sourceFile):
        # After download the file needs to be stored in the remote cache.
        # Here it comes one of the most delicate process of each implementation, since the strategy to 
        # name the remote resource should be consistent, and extensible if needed.
        # It's important to be consistent in the naming of the remote resource, because if the name 
        # it's changed the resource won't be found in a new version

        # This is the part where each implementation will need to connect to the remote server, and upload
        # the files
        pass
