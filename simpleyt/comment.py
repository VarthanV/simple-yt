class Comment(object):
    def __init__(self,comment_dict:dict):
        self.comment_dict  = comment_dict
        self.parse_comment()
    def parse_comment(self):
        self.main_data = self.comment_dict.get('snippet').get('snippet')
    @property
    def comment_text(self):
        return self.main_data.get('textDisplay')       
