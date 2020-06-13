class YouTubeChannel(object):
    def __init__(self, channel_obj):
        self.channel_obj = channel_obj
        self._parse_obj()

    def _parse_obj(self):
        self.main_items = self.channel_obj.get('items')[0]
        self.snippet = self.main_items.get('snippet')
        self.content = self.main_items.get("contentDetails")
        self.statistics = self.main_items.get('statistics')

    @property
    def response(self) -> dict:
        """ Returns the Actual Response from the request """
        return self.channel_obj

    @property
    def name(self) -> str:
        """ The name of the Channel """
        return self.snippet.get('title')

    @property
    def description(self) -> str:
        """  The description of the Channel"""
        return self.snippet.get('description')

    @property
    def published_at(self) -> str:
        """ The published details of the Channel """
        return self.snippet.get('publishedAt')

    @property
    def thumbnail_dict(self) -> dict:
        """ The Thumbnail Dict of the Channel  """
        return self.snippet.get('thumbnails')

    @property
    def default_thumbnail(self) -> str:
        """ The URL of the default thumbnail of the Channel"""
        _url = self.snippet.get('thumbnails').get('default').get('url')
        return _url

    @property
    def country(self) -> str:
        """ Returns the Country of the Channel """
        return self.snippet.get('country')
