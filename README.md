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

Details of a video can be obtained by using the   ``` get_video``` method.

```python
# A Sample video id has been passed 

video =client.get('uN-TvWzeEvA')
```

An instance of  ``` YotubeVideo``` class will be returned which helps to obtain the details of the video in a easy manner by using the attributes.

```python
>>> video.title
'Rip Ohio /r/softwaregore #48 [REDDIT REVIEW]'

>>> v.category_id
 '24'

>>> v.channel_name
'PewDiePie'
>>> v.description
'ohio will be taken over by computers. subscribe for more reddit reviews epicly\n\n100 CLUB MERCH OUT NOW! https://represent.com/store/pewdiepie (Thank you) (▰˘◡˘▰)\nMinecraft Series Playlist:\nhttps://www.youtube.com/watch?v=VGt-BZ-SxGI&list=PLYH8WvNV1YEnLCzUDWueIZQXDNhqLKywk\nALL MINECRAFT EPISODES Playlist:\nhttps://www.youtube.com/watch?v=mhgS6TNkX9Q&list=PLYH8WvNV1YEn9PkI2stxJWMs8GRit66Rz\n\n\n:::::::My Stores:::::::: \nTSUKI:\nhttps://tsuki.market/\nMerch:\nhttps://represent.com/store/pewdiepie\n\n:::::::I drink GFUEL (affiliate link)::::::::\nhttps://gfuel.ly/31Kargr\n\n:::::::I stream on DLive (ad)::::::::\n\nhttps://go.dlive.tv/pewdiepie\n\n:::::::My Setup (affiliate links):::::::: \nChair: https://clutchchairz.com/pewdiepie/\nElgato Green Screen:\nhttp://e.lga.to/PewDiePie\n\n:::::::Check out this game I helped make (affiliate)::::::::\nhttps://store.steampowered.com/app/703840/Animal_Super_Squad/\n\n__ Outro: Animation:\nhttps://www.youtube.com/user/jae55555\n Song: https://www.youtube.com/channel/UC3e8EMTOn4g6ZSKggHTnNng'

>>> v.like_count
465961

```
