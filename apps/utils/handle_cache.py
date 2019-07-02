class CacheKeyHandle(object):
    """
    缓存的键  设置
    注意：子类只是需要定义object_header_cache_key和list_header_cache_key即可，定义一下键的开头
    """
    object_header_cache_key = ""
    list_header_cache_key = ""
    object_cache_key = ""
    list_cache_key = ""

    def object_cache_key_func(self, **kwargs):
        self.object_cache_key = self.object_header_cache_key + self.object_cache_key
        for key, val in dict(self.request.query_params).items():
            self.object_cache_key = self.object_cache_key + '{key}={val}&'.format(key=key, val=val[0])
        return self.object_cache_key

    def list_cache_key_func(self, **kwargs):
        self.list_cache_key = self.list_header_cache_key + self.list_cache_key
        for key, val in dict(self.request.query_params).items():
            self.list_cache_key = self.list_cache_key + '{key}={val}&'.format(key=key, val=val[0])
        return self.list_cache_key
