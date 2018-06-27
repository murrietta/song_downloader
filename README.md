# YouTube Convenience Downloader

An app that downloads videos from YouTube using pytube, creates mp3s from mp4s using mplayer or lame, adds ID3 tags using eyed3, and (optionally) cuts songs at specified timestamps using PyDub

plan:
+ modify `current_list` module's `urls` object to a dictionary that will accept extra information thus allowing full specification of tasks at one entry point.
+ will create a `master.py` file that coordinates all required programs and will be run at the `app` directory level

DISCLAIMER: I take no responsibility for the way you choose to use this software. I have built this simply for personal educational purposes.

### Instructions for Use:
Currently only working in python 2.7.
+ You'll need to have some other stuff installed:
	+ For converting from mp4 to mp3 install lame, and mplayer:
		+ `sudo apt-get install lame`
		+ `sudo apt-get install mplayer`
	+ For chopping install `pydub` which requires either the libav or ffmpeg binaries
		+ `sudo apt-get install ffmpeg`
		+ `pip install pydub`
	+ For adding id3 tags install `eyed3`
		+ `pip install eyed3`

+ In the `downloading` folder, modify the `current_list.py` file as needed.
	+ It should be self explanatory based on the objects in there: the `urls` object is a list of dictionaries that pertain to specific videos. Add to or remove from this object as needed. Be sure to modify each specific value for the appropriate key (url, artist, title, album, etc.).
+ Run it at the top level folder:
	+ In the folder containing `master.py` simpy run `python master.py`
