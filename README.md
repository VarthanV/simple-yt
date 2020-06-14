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

```
import simpleyt
client = simpleyt.YotubeAPI('<API KEY>')
```

## Get Video

Details of a video can be obtained by using the   ``` get_video``` method.