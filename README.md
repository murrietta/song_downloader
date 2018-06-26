# YouTube Convenience Downloader

An app that downloads videos from YouTube using pytube, creates mp3s from mp4s using mplayer or lame, adds ID3 tags using eyed3, and (optionally) cuts songs at specified timestamps using PyDub

plan:
+ modify `current_list` module's `urls` object to a dictionary that will accept extra information thus allowing full specification of tasks at one entry point.
+ will create a `master.py` file that coordinates all required programs and will be run at the `app` directory level.

The directory structure will be as follows:
	app
	|
	|-labeling
	|
	|-mp4s
	|
	|-song_dl_lists


