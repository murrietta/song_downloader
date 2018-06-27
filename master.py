from __future__ import print_function
#download any songs, also imports urls from current_list.py
from downloading import download_songs
import argparse, os

#since this is a command line implementation, allow user to specify directory to download videos to
parser = argparse.ArgumentParser(description = "downloads multiple videos from youtube and has functionality to convert them to mp3s, cut them at specified times, and add ID3 tags.")
parser.add_argument("-dir", type = str , default = os.path.join(os.getcwd(), "mp4s"), help = "Default directory is the 'mp4s' folder in the top level directory of this application.")

args = parser.parse_args()
dl = download_songs.downloader(args.dir)

#finally, run the downloading script
dl.run()

#now autostrip the files if that is specified
if download_songs.autostrip:
	print("Autostrip is specified, running mp4tomp3.py...")
	from converting import mp4tomp3

	mcon = mp4tomp3.mp4converter("./mp4s", "./mp4s")
	mcon.run()

	#the next two tasks depend on conversion from mp4 to mp3
	#that is chopping and labeling/tagging

	#here is the chopping
	#labeling is included since we're already handling each file
	print("Proceeding with audio file chopping and labeling...")
	from chopping import chopper
	chpr = chopper.chopper(download_songs.urls, dl.dir)
	chpr.run()