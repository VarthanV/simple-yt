class YoutubeVideo(object):
    def __init__(self, video_obj):
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
