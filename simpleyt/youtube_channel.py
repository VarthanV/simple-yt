
class YouTubeChannel(object):
    def __init__(self, channel_obj):
        self.channel_obj = channel_obj
        self._parse_obj()

    def _parse_obj(self):
        self.main_items = self.channel_obj.get('items')[0]
        self._snippet = self.main_items.get('snippet')
        self.content = self.main_items.get("contentDetails")
        self.statistics = self.main_items.get('statistics')

    @property
    def response(self) -> dict:
        """ Returns the Actual Response from the request """
        return self.channel_obj

    @property
    def name(self) -> str:
        """ The name of the Channel """
        return self._snippet.get('title')

    @property
    def description(self) -> str:
        """  The description of the Channel"""
        return self._snippet.get('description')

    @property
    def published_at(self) -> str:
        """ The published details of the Channel """
        return self._snippet.get('publishedAt')

    @property
    def thumbnail_dict(self) -> dict:
        """ The Thumbnail Dict of the Channel  """
        return self._snippet.get('thumbnails')

    @property
    def default_thumbnail(self) -> str:
        """ The URL of the default thumbnail of the Channel"""
        _url = self._snippet.get('thumbnails').get('default').get('url')
        return _url

    @property
    def country(self) -> str:
        """ Returns the Country of the Channel """
        return self._snippet.get('country')
    @property
    def view_count(self) -> int :
        """ View Count of the Channel """

        return int(self.statistics.get('viewCount'))    

    @property
    def subscribers_count(self) -> str:
        """ Subscribers Count of the Channel """
        return self.statistics.get('subscriberCount') 
    @property
    def video_count(self) ->int:
        """ Count of the Videos Posted by the Channel"""
        return int(self.statistics.get('videoCount'))     
    @property
    def topics(self) ->list :
        """ List of the Topics Covered by the Channel """
        return self.main_items.get('topicDetails').get('topicCategories')
    @property
    def banner_dict(self) -> dict:
        """ Returns a dict that contains the Banner details of the Channel"""
        return self.main_items.get('brandingSettings').get('image')
    @property
    def banner_image_url(self) -> str:
       """ Returns the URL of the Default Banner Image"""
       try : 
         return self.main_items.get('brandingSettings').get('image').get('bannerImageUrl')        
       except : 
           return None