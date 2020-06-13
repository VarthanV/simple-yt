class Comment(object):
    def __init__(self,comment_dict:dict):
        self.comment_dict  = comment_dict
        self.parse_comment()
    def parse_comment(self):
        self.main_data =self.comment_dict.get('snippet')
        self.comment_data = self.main_data.get('topLevelComment').get('snippet')
    @property
    def comment_text(self)->str:
        """ The Comment made by the user """
        return self.comment_data.get('textDisplay')  
    @property
    def author_name(self)->str:
        """ The name of the author who made the comment """
        return self.comment_data.get('authorDisplayName')
    @property
    def author_image_url(self)->str:
        """ The Profile Image of the Author  """
        return self.comment_data.get('authorProfileImageUrl')
    @property
    def like_count(self) -> int:
        """ The Likes that the Comment got"""
        return int(self.comment_data.get('likeCount'))    

            
    
