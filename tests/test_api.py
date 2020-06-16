import os
import simpleyt
from simpleyt import YoutubeVideo
from simpleyt.youtube_channel import YouTubeChannel
from simpleyt.playlist import Playlist
from dotenv import load_dotenv
import pytest
load_dotenv()
""" Intialization """
key = os.environ.get('API_TOKEN')
client = simpleyt.YoutubeAPI(key)
channel_id = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'
video_id = '7M9hc_PC_Vg'
def test_api_fails():
    with pytest.raises(Exception) as e :
        failed_client = simpleyt.YoutubeAPI('fkfjf')

def test_video_method():
    """  Test for the get_video method"""
    video = client.get_video(video_id)
    assert isinstance(video, YoutubeVideo)
    assert video.title == 'Oxygen - Video Song | Kavan | Hiphop Tamizha | K V Anand | Vijay Sethupathi, Madonna Sebastian'
    assert video.dimension == '2d'
    assert isinstance(video.dislike_count, int)
    assert isinstance(video.duration_in_seconds ,float)
    assert isinstance(video.has_captions ,str)
    assert isinstance(video.is_licensed_content,bool)
    assert isinstance(video.category_id,str)
    assert video.is_licensed_content == True
    assert isinstance(video.response,dict)
    assert isinstance(video.video_obj,dict)
    assert isinstance(video.duration,str)

def test_channel_method():
    """  Testing of the get_channel method  """
    channel  = client.get_channel(channel_id)
    assert isinstance(channel,YouTubeChannel)
    assert channel.name == 'PewDiePie'
    assert channel.description == 'I make videos.'
    assert channel.country == 'US'
    assert isinstance(channel.subscribers_count,str)
    assert isinstance(channel.topics,list)
    assert channel.banner_image_url == 'https://yt3.ggpht.com/wuqXYCeCdttO0TcwBJR2yy0uJP2hPwTPdrDQpjD00t0Xd_81t6dYeLdVMR24ArD4kuIpWO4hWg=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj'
    assert isinstance(channel.video_count,int)
    assert isinstance(channel.view_count,int)

def test_comment_method():
    """ Testing of get_comment method """
    comment_data  =client.get_comments(video_id)
    comments_list = comment_data.comments
    assert isinstance(comments_list,list)
    comment = comments_list[0]
    assert isinstance(comment.comment_text,str)
    assert isinstance(comment.author_name,str)

def test_get_playlists_method():
    """ Testing of get_playlist method """
    playlist = client.get_playlists(channel_id)
    assert isinstance(playlist,list)
    assert isinstance(playlist[0],Playlist)

def test_search_method():    
    """ Test for search method """
    s =client.search('Cat videos ') 
    assert isinstance(s,list)
    result = s[0]
    assert isinstance(result,YoutubeVideo)
    assert isinstance(result.title , str  )
    assert isinstance(result.like_count,int)

@pytest.mark.fail_test    
def test_video_parsing_fails():
    with pytest.raises(Exception) as e:
       vid = YoutubeVideo([])

@pytest.mark.fail_test      
def test_video_method_fails():
     with pytest.raises(Exception) as e: 
         video =client.get_video('33i93939393')       
@pytest.mark.fail_test
def test_playlist_method_fails():
    with pytest.raises(Exception) as e  :
        video = client.get_playlists('ejfejfnbej')
