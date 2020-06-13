from simpleyt.comment import Comment
class VideoComment(object):
    def __init__(self,comments_obj:dict):
        self._comments_obj =comments_obj
        self._comments_list = []
        self.parse_comments()
        
    def parse_comments(self):
        self.main_data =self._comments_obj.get('items')

        for item in self.main_data:
            self._comments_list.append(Comment(item))
            

    @property
    def next_page_token(self) -> str :
        """  Next Page token """
        return self._comments_obj.get('nextPageToken')    
    @property
    def response(self) ->dict:
        return self._comments_obj
    @property
    def comments(self)  ->list:
        return self._comments_list