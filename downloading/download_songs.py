from __future__ import print_function
'''
expedites the download process, just put this file in a 
folder with a subfolder in it named "song_dl_lists". That
folder will need to contain two files: __init__.py and 
hotlist.py, the latter must contain a variable named
"urls" that is a list of either tuples or lists with 3
entries each where the first is the youtube URL to the
video to d/l, the second is the artist name, and the 
third is the video name.

Note that there is a default directory specified in this
file for where to dump the 
'''

from pytube import YouTube as youtube
from current_list import urls, autostrip
import os

#this used to be the default dir but we are going to now run this from a folder above
# defaultdir = "".join([x for x in reversed("".join([x for x in reversed(os.getcwd())]).split("/", 1)[1])]) + "/mp4s"

def_dir = os.path.join(os.getcwd(), "mp4s")

class downloader:
	
	def __init__(self, target_dir = def_dir):
		self.dir = target_dir

	def run(self):
		if os.path.isdir(self.dir) != False:
			print("\n\nDirectory: {}".format(self.dir))
			print("\n\nDownload the following from youtube?")
			print("\n")
			print("{:>30}   {:<50}".format("Artist","Title"))
			print("{:^60}\n".format("="*60))
			for url in urls:
				print("{:>30}   {:<50}".format(url['artist'], url['title']))

			cont = raw_input("\nContinue? [Y/N]")

			if cont.upper() == "Y":
				for url in urls:
					fname = "{} - {}".format(url['artist'],url['title'])
					print("Downloading {}...".format(fname), end='')
					yt = youtube(url['url'])
					yt.get_videos()
					yt.set_filename(fname)
					try:
						yt.get('mp4', yt.filter('mp4')[-1].resolution).download(self.dir)
						print("{:>14}".format("DONE!"))
					except:
						print("\nmp4 format not available for {}.".format(yt.filename))
			else:
				print("\nCanceled!\n")
		else:
			print("\n\nPath not found, check the -dir argument\nDir provided: {}\n".format(self.dir))

if __name__ == "__main__":
	#do the standard command line use
	import argparse

	parser = argparse.ArgumentParser(description = "downloads multiple videos from youtube, I typically use this for songs, hence the name.")
	parser.add_argument("-dir", type = str , default = os.path.join(os.getcwd(), "mp4s"), help = "If you are not me then the default may not exist on your computer")

	args = parser.parse_args()

	dl = downloader(args.dir)
	dl.run()