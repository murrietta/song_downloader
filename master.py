from __future__ import print_function
#download any songs, also imports urls from current_list.py
from downloading import download_songs
import argparse, os

#since this is a command line implementation, allow user to specify directory to download videos to
parser = argparse.ArgumentParser(description = "downloads multiple videos from youtube, I typically use this for songs, hence the name.")
parser.add_argument("-dir", type = str , default = os.path.join(os.getcwd(), "mp4s"), help = "If you are not me then the default may not exist on your computer")

args = parser.parse_args()
dl = download_songs.downloader(args.dir)

#finally, run the downloading script
# dl.run()

#now autostrip the files if that is specified
if download_songs.autostrip:
	print("Autostrip is specified, running mp4tomp3.py...")
	import mp4tomp3

	mcon = mp4tomp3.mp4converter("./mp4s", "./mp4s")
	mcon.main()

	#to put id3 tags we need to have stripped to mp4 so
	#we proceed here with id3 tagging
