import requests
from simpleyt.exception import SimpleYTException
from pprint import pprint
from simpleyt.youtube_channel import YouTubeChannel
from simpleyt.youtube_video import YoutubeVideo
from simpleyt.video_comment import VideoComment
import json
from simpleyt.playlist import Playlist
# AIzaSyA9Tz9bICdRgR3CLwxR__wDVAeSFiVz15M

# Id: 7M9hc_PC_Vg
#Channel : UC-lHJZR3Gqxm24_Vd_AJ5Yw
class YoutubeAPI:
    def __init__(self, api_key):
        """
        Please do obtain a API key from here https://console.cloud.google.com/apis/dashboard
        :param:api_key: The API key that you got from the Console
        """
        self.api_key = api_key
        if not self.verify_key():
            raise ValueError(
                "Invalid Api Key , Please do obtain a valid key from here  https://console.cloud.google.com/apis/dashboard")

    def verify_key(self):
        url = "https://www.googleapis.com/youtube/v3/videos?id=7M9hc_PC_Vg&key={}&part=contentDetails&part=statistics".format(
            self.api_key)
        res = requests.get(url)
        try:
            res.raise_for_status()
            return True
        except:
            """
            It will be meaningless to throw the error provided
            by requests
            """
            return False

    def make_request(self, url):
        """
        A common method to make Http Requests
        """
        res = requests.get(url)
        try:
            return res.json()
        except Exception as e:
            raise SimpleYTException("An Exception Occured", e)

    def get_video(self, video_id):
        """
        When a video id is given it returns the Details of the video like
        Thumbnail,Title,Likes,Count,description,Category etc.. as a "YouTube"
        video class which has the properties for the same
        :param:video_id: The Id of the video

        """
        _vid_url = 'https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=contentDetails&part=statistics&part=snippet'.format(
            video_id, self.api_key)
        response_json = self.make_request(_vid_url)
        yt_class = YoutubeVideo(response_json)
        return yt_class

    def get_channel(self, channel_id):
        """ Returns the Detail of a Channel
        :param:channel_id: The ID of the Channel 
        
         """
        _url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&part=snippet&part=statistics&part=topicDetails&part=brandingSettings&id={}&key={}&maxResults=50".format(
            channel_id, self.api_key)
        response_json = self.make_request(_url)
        yt_class =YouTubeChannel(response_json)
        return yt_class
    def get_comments(self,video_id, max_results=50,**kwargs):
        """  
        Fetches Comments of a Video 
        :param: The ID of the Video 
        
        """
        _url  ='https://www.googleapis.com/youtube/v3/commentThreads?key={}&textFormat=plainText&part=snippet&videoId={}&maxResults={}'.format(self.api_key,video_id,max_results)
        for key,value in kwargs.items():
            """  For passing next page token and other stuffs"""
            _url+='&{}={}'.format(key , value)
        response_json = self.make_request(_url)
        comment_obj =VideoComment(response_json)
        return comment_obj

    def get_playlists(self,channel_id,max_results=50,**kwargs):
        """
        Returns the List of Playlists a particular channel has
        :param: The Id of the Channel 
        """
        self.playlists =[]
        _url='https://www.googleapis.com/youtube/v3/playlists?key={}&textFormat=plainText&part=snippet&channelId={}&maxResults={}'.format(self.api_key,channel_id,max_results)
        for key,value in kwargs.items():
           """  For passing next page token and other stuffs"""
           _url+='&{}={}'.format(key , value)
        response_json = self.make_request(_url)
        comment_list = response_json.get('items')
        self.next_page_token = response_json.get('nextPageToken')
        for comment in comment_list:
            obj =Playlist(comment)
            self.playlists.append(obj)
        return self.playlists 


    def get_videos_from_playlist(self,playlist_id,max_results =1000,**kwargs):
        """
        Gets the List of ID's of Videos from the given 
        playlist

        The video Id's will be returned to get more details about the video 
        get_vide can be used
        """
        _url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&maxResults=50&key={}".format(playlist_id,self.api_key)
        for key,value in kwargs.items():
           """  For passing next page token and other stuffs"""
           _url+='&{}={}'.format(key , value)
        video_ids = []
        response_json = self.make_request(_url)
        response_json = response_json.get('items')
        self.response = response_json
        for item in response_json:
            video_ids.append(item.get('snippet').get('resourceId').get('videoId'))
        return video_ids    

    def search(self,term='',max_results=10,**kwargs):
        """ 
        Search a video
        
        """
        pass    

        


