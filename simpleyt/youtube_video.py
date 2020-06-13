import isodate


class YoutubeVideo(object):
    def __init__(self, video_obj: dict):
        """
        The video obj is the  json that is obtained from the response
        """
        self.video_obj = video_obj
        self._parse_json()

    def _parse_json(self):
        """
        Internal method which parses the Json and returns the
        associated properties of the video
        """
        try:
            self.main_item = self.video_obj.get('items')[0]
            self.video_data = self.main_item.get('snippet')
            self.content = self.main_item.get('contentDetails')
            self.statistics = self.main_item.get('statistics')
        except Exception as e:
            print(e)

    def _clean_string(self, string):
        string = string.strip()
        return string

    @property
    def response(self):
        """ Returns the Actual JSON """
        return self.video_data

    @property
    def category_id(self):
        """ Returns the Category of the video """
        return self.video_data.get('categoryId')

    @property
    def published_at(self):
        """ When it is published   """
        return self.video_data.get('publishedAt')

    @property
    def channel_id(self):
        """ The id of the channel """
        return self.video_data.get('channelId')

    @property
    def title(self):
        """ The title of the Video """
        return self._clean_string(self.video_data.get('title'))

    @property
    def description(self):
        """ The description of the Video """
        return self._clean_string(self.video_data.get('description'))

    @property
    def channel_name(self):
        """  The name of the Channel """

        return self._clean_string(self.video_data.get('channelTitle'))

    @property
    def tags(self):
        """  The list of tags of the video """

        return self.video_data.get('tags')

    @property
    def definition(self):
        """ Then definition of the Video,Whether it is hd,sd ..etc"""
        return self.content.get('definition')

    @property
    def content_rating(self):
        """ The dict of the rating of the Content """
        return self.content.get('contentRating')

    @property
    def is_licensed_content(self) -> bool:
        """ Checks whether the content is licensed or not, Returns a boolean"""
        return self.content.get('licensedContent')

    @property
    def dimension(self):
        """  The Dimension of the video """
        return self.content.get('dimension')

    @property
    def view_count(self) -> int:
        """  The number of views for the video"""
        return int(self.statistics.get('viewCount'))

    @property
    def like_count(self) -> int:
        """ The Like count of the Video  """
        return int(self.statistics.get('likeCount'))

    @property
    def dislike_count(self) -> int:
        """  The Dislike count of the Video"""
        return int(self.statistics.get('dislikeCount'))

    @property
    def favorite_count(self) -> int:
        """  The Favorite count of the Video """
        return int(self.statistics.get('favoriteCount'))

    @property
    def thumbnail_dict(self) -> dict:
        """  The dict containing Thumbnail"""
        return self.video_data.get('thumbnails')

    @property
    def default_thumbnail_url(self) -> str:
        """ The URL of the Thumbnail of the Default Resolution"""
        url_ = self.video_data.get('thumbnails').get('default').get('url')
        return url_

    @property
    def has_captions(self) -> bool:
        """ Whether the Video has Captions or not """
        return self.content.get('caption')

    @property
    def duration(self) -> str:
        """ The duration of the video in ISO Format"""
        return self.content.get('duration')

    @property
    def duration_in_seconds(self) -> float:
        """ The duration of the video in seconds  """
        duration = isodate.parse_duration(self.content.get('duration'))
        total_seconds = duration.total_seconds()
        return total_seconds
