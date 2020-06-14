## simpleyt

simpleyt is a unofficial Python Package for the Youtube API. It focuses on **simplicity** as the name says to fetch details of the video,playlist,channel etc in a easy manner

## Installation

```
pip install simpleyt
```

## Usage

## Quickstart

Simply import the simple yt module and intialize
with an API Key

If API key is invalid an exception will be thrown do refer this to obtain key[documentation](https://bit.ly/2UJD8rT) for details.

```python
import simpleyt
client = simpleyt.YotubeAPI('<API KEY>')
```

## Get Video

Details of a video can be obtained by using the `get_video` method.

```python
# A Sample video id has been passed

video =client.get('uN-TvWzeEvA')
```

An instance of `YotubeVideo` class will be returned which helps to obtain the details of the video in a easy manner by using the attributes.

```python
>>> video.title
'Rip Ohio /r/softwaregore #48 [REDDIT REVIEW]'

>>> video.category_id
 '24'

>>> video.channel_name
'PewDiePie'
>>> video.description
'ohio will be taken over by computers. subscribe for more reddit reviews epicly\n\n100 CLUB MERCH OUT NOW! https://represent.com/store/pewdiepie (Thank you) (▰˘◡˘▰)\nMinecraft Series Playlist:\nhttps://www.youtube.com/watch?v=VGt-BZ-SxGI&list=PLYH8WvNV1YEnLCzUDWueIZQXDNhqLKywk\nALL MINECRAFT EPISODES Playlist:\nhttps://www.youtube.com/watch?v=mhgS6TNkX9Q&list=PLYH8WvNV1YEn9PkI2stxJWMs8GRit66Rz\n\n\n:::::::My Stores:::::::: \nTSUKI:\nhttps://tsuki.market/\nMerch:\nhttps://represent.com/store/pewdiepie\n\n:::::::I drink GFUEL (affiliate link)::::::::\nhttps://gfuel.ly/31Kargr\n\n:::::::I stream on DLive (ad)::::::::\n\nhttps://go.dlive.tv/pewdiepie\n\n:::::::My Setup (affiliate links):::::::: \nChair: https://clutchchairz.com/pewdiepie/\nElgato Green Screen:\nhttp://e.lga.to/PewDiePie\n\n:::::::Check out this game I helped make (affiliate)::::::::\nhttps://store.steampowered.com/app/703840/Animal_Super_Squad/\n\n__ Outro: Animation:\nhttps://www.youtube.com/user/jae55555\n Song: https://www.youtube.com/channel/UC3e8EMTOn4g6ZSKggHTnNng'

>>> video.like_count
465961
>>> video.duration_in_seconds
1177.0

#The actual response returned by the  API

>>> v.response

{'publishedAt': '2019-10-06T18:33:47Z',
 'channelId': 'UC-lHJZR3Gqxm24_Vd_AJ5Yw',
 'title': 'Rip Ohio /r/softwaregore #48 [REDDIT REVIEW]',
 'description': 'ohio will be taken over by computers. subscribe for more reddit reviews epicly\n\n100 CLUB MERCH OUT NOW! https://represent.com/store/pewdiepie (Thank you) (▰˘◡˘▰)\nMinecraft Series Playlist:\nhttps://www.youtube.com/watch?v=VGt-BZ-SxGI&list=PLYH8WvNV1YEnLCzUDWueIZQXDNhqLKywk\nALL MINECRAFT EPISODES Playlist:\nhttps://www.youtube.com/watch?v=mhgS6TNkX9Q&list=PLYH8WvNV1YEn9PkI2stxJWMs8GRit66Rz\n\n\n:::::::My Stores:::::::: \nTSUKI:\nhttps://tsuki.market/\nMerch:\nhttps://represent.com/store/pewdiepie\n\n:::::::I drink GFUEL (affiliate link)::::::::\nhttps://gfuel.ly/31Kargr\n\n:::::::I stream on DLive (ad)::::::::\n\nhttps://go.dlive.tv/pewdiepie\n\n:::::::My Setup (affiliate links):::::::: \nChair: https://clutchchairz.com/pewdiepie/\nElgato Green Screen:\nhttp://e.lga.to/PewDiePie\n\n:::::::Check out this game I helped make (affiliate)::::::::\nhttps://store.steampowered.com/app/703840/Animal_Super_Squad/\n\n__ Outro: Animation:\nhttps://www.youtube.com/user/jae55555\n Song: https://www.youtube.com/channel/UC3e8EMTOn4g6ZSKggHTnNng',
 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/uN-TvWzeEvA/default.jpg',
   'width': 120,
   'height': 90},
  'medium': {'url': 'https://i.ytimg.com/vi/uN-TvWzeEvA/mqdefault.jpg',
   'width': 320,
   'height': 180},
  'high': {'url': 'https://i.ytimg.com/vi/uN-TvWzeEvA/hqdefault.jpg',
   'width': 480,
   'height': 360},
  'standard': {'url': 'https://i.ytimg.com/vi/uN-TvWzeEvA/sddefault.jpg',
   'width': 640,
   'height': 480},
  'maxres': {'url': 'https://i.ytimg.com/vi/uN-TvWzeEvA/maxresdefault.jpg',
   'width': 1280,
   'height': 720}},
 'channelTitle': 'PewDiePie',
 'tags': ['SATIRE',
  'pewdiepie',
  'pewdie',
  'pdp',
  'reddit review',
  'pewdiepie reddit review',
  'pewdiepie reddit',
  'reddit',
  'minecraft',
  'pewdiepie minecraft',
  'reddit software',
  'software',
  'software engineering',
  'technology',
  'tech review',
  'pc',
  'computers',
  'ohio',
  'comedy',
  'parody'],
 'categoryId': '24',
 'liveBroadcastContent': 'none',
 'defaultLanguage': 'en-US',
 'localized': {'title': 'Rip Ohio /r/softwaregore #48 [REDDIT REVIEW]',
  'description': 'ohio will be taken over by computers. subscribe for more reddit reviews epicly\n\n100 CLUB MERCH OUT NOW! https://represent.com/store/pewdiepie (Thank you) (▰˘◡˘▰)\nMinecraft Series Playlist:\nhttps://www.youtube.com/watch?v=VGt-BZ-SxGI&list=PLYH8WvNV1YEnLCzUDWueIZQXDNhqLKywk\nALL MINECRAFT EPISODES Playlist:\nhttps://www.youtube.com/watch?v=mhgS6TNkX9Q&list=PLYH8WvNV1YEn9PkI2stxJWMs8GRit66Rz\n\n\n:::::::My Stores:::::::: \nTSUKI:\nhttps://tsuki.market/\nMerch:\nhttps://represent.com/store/pewdiepie\n\n:::::::I drink GFUEL (affiliate link)::::::::\nhttps://gfuel.ly/31Kargr\n\n:::::::I stream on DLive (ad)::::::::\n\nhttps://go.dlive.tv/pewdiepie\n\n:::::::My Setup (affiliate links):::::::: \nChair: https://clutchchairz.com/pewdiepie/\nElgato Green Screen:\nhttp://e.lga.to/PewDiePie\n\n:::::::Check out this game I helped make (affiliate)::::::::\nhttps://store.steampowered.com/app/703840/Animal_Super_Squad/\n\n__ Outro: Animation:\nhttps://www.youtube.com/user/jae55555\n Song: https://www.youtube.com/channel/UC3e8EMTOn4g6ZSKggHTnNng'},
 'defaultAudioLanguage': 'en-GB'}


```

## Get Channel Details

```python
>>> channel = v.get_channel('UC-lHJZR3Gqxm24_Vd_AJ5Yw')

>>> channel.name
'PewDiePie'
>>> channel.description
'I make videos.'
>>> channel.country
'US'
>>> channel.subscribers_count
105000000
>>> channel.topics

['https://en.wikipedia.org/wiki/Film',
 'https://en.wikipedia.org/wiki/Video_game_culture',
 'https://en.wikipedia.org/wiki/Entertainment',
 'https://en.wikipedia.org/wiki/Action_game',
 'https://en.wikipedia.org/wiki/Role-playing_video_game']

>>> channel.banner_image_url

'https://yt3.ggpht.com/wuqXYCeCdttO0TcwBJR2yy0uJP2hPwTPdrDQpjD00t0Xd_81t6dYeLdVMR24ArD4kuIpWO4hWg=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj'

```

## Get comments of a video

The `get_comment` method returns a List of `Comment` object

```python
comment_data = client.get_comments('JHhO5JKofgc')

comments_list = client.comments
comment = comments_list[0]
>>> comment.comment_text
'as a filipino, i am quite irritated at the fact that they belittle Rose j'
>>> comment.author_image_url
'https://yt3.ggpht.com/a/AATXAJxlURGc1iRQESvxlyUZPTM_pt1WviokL2k2dQ=s48-c-k-c0xffffffff-no-rj-mo'

>>> comment.author_name
'boninieee'

```

## Get playlists

This method returns the `Playlist` object.

```python

 playlists =c.get_playlists('UC-lHJZR3Gqxm24_Vd_AJ5Yw')

 >>> for item in playlists:
   ...:     print(item.playlist_id)
   ...:
PLYH8WvNV1YElE78ql2vvcOURM1tve_njn
PLYH8WvNV1YEkRR6peiTWZfIRUglGJBQV5
PLYH8WvNV1YElSlBP0ohchkYTByQ-xD92v
PLYH8WvNV1YEnb1QbNk1_liUa_UXH_SIVl
PLYH8WvNV1YEldU75ZIVbAl6OB6brtGKY6
PLYH8WvNV1YEnaAanyt5FPgwjZY0Lnu8Pb
PLYH8WvNV1YEnLCzUDWueIZQXDNhqLKywk
PLYH8WvNV1YEn9PkI2stxJWMs8GRit66Rz
PLYH8WvNV1YElPqvWxK_uzWhcMXY_DvlPu
PLYH8WvNV1YEniTaIMd95jFlqBpxR0SWJE
....
```
##  Search for videos


```python

 s =client.search('Cat videos ') 

```
This method returns the list of ``` YotubeVideo``` objects

## Contributing

If you have worked on some changes and need new changes make a pull request  [Pull Request](https://github.com/VarthanV/simple-yt/pulls)

## Issues

Submit a new Issue here [Issue](https://github.com/VarthanV/simple-yt/issues)
