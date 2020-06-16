import os
import simpleyt
from simpleyt import YoutubeVideo
from dotenv import load_dotenv
load_dotenv()
""" Intialization """
key = os.environ.get('API_TOKEN')
client = simpleyt.YoutubeAPI(key)


def test_video_method():
    """  Test for the get video method"""
    video = client.get_video('7M9hc_PC_Vg')
    assert isinstance(video, YoutubeVideo)
    assert video.title == 'Oxygen - Video Song | Kavan | Hiphop Tamizha | K V Anand | Vijay Sethupathi, Madonna Sebastian'
    assert video.dimension == '2d'
    assert isinstance(video.dislike_count, int)
    assert isinstance(video.duration_in_seconds ,float)
    assert isinstance(video.has_captions ,str)
    assert isinstance(video.is_licensed_content,bool)
    assert isinstance(video.category_id,str)
    assert video.is_licensed_content == True
    