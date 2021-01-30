from conans.client.downloaders.cached_file_downloader import CachedFileDownloader
from conans.client.downloaders.file_downloader import FileDownloader
from conans.client.downloaders.remote_cache import RemoteCache


def run_downloader(requester, output, verify, config, user_download=False, use_cache=True, **kwargs):
    downloader = FileDownloader(requester=requester, output=output, verify=verify, config=config)
    if use_cache and config.download_cache:
        remote_cache = None
        if config.remote_cache_active:
            remote_cache = RemoteCache(config)
        downloader = CachedFileDownloader(config.download_cache, downloader,
                                          user_download=user_download, remote_cache=remote_cache)
    return downloader.download(**kwargs)
