
class Playlist(object):
    def __init__(self,playlist_obj:dict):
        self.playlist_obj=playlist_obj
        self.parse_json()

    def parse_json(self):
        self.main_data = self.playlist_obj.get('snippet')    
    @property
    def response(self):
        """ 
        Returns  the JSON response 
        """
        return self.playlist_obj  
    @property
    def playlist_id(self):
        """
        Returns the Id of the playlist
        """

        return  self.playlist_obj.get("id")

    @property
    def title(self):
        """
        Returns the Title of the Playlist 
        
        """ 
        return self.main_data.get('title')
    @property
    def description(self):
        """
        Returns the Description of the playlist
        
        """    
        return self.main_data.get('description')
    @property
    def  thumbnail_dict(self):
        """
        Returns the Thumbnail Dict 
        
        """   
        return self.main_data.get('thumbnails')  
    @property
    def default_thumbnail_url(self) -> str:
        """
        Returns the Default Thumbnail URL
        
        """
        return self.main_data.get('thumbnails').get('default').get('url')  