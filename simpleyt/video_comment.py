from simpleyt.comment import Comment
class VideoComment(object):
    def __init__(self,comments_obj:dict):
        self.comments_obj =comments_obj
        self.parse_comments()
    def parse_comments(self):
        self,main_data = ""
    @property
    def next_page_token(self) -> str :
        """  Next Page token """
        return self.comments_obj.get('nextPageToken')    
