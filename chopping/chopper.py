# -*- coding: latin-1 -*-
from __future__ import print_function
'''
to use this you need either libav or ffmpeg binaries installed. 
'''
from pydub import AudioSegment
import eyed3
import os
# from tracks_times.current import inpath, outpath, art_alb_dict, tracks_times

class chopper:

	def __init__(self, files, directory):
		self.files = files #this should be list of dictionaries with a 'songlist' key whose value is another dictionary consisting of song titles for keys and whose values are dictionaries with 't0' and 't1' keys with values of times as strings in hh:mm:ss format
		self.dir = directory

	def run(self):
		#step through each file that should be in the directory
		for file in self.files:
			#make a directory composed of the artist and title also set input path
			inpath = os.path.join(self.dir, "{} - {}.mp3".format(file['artist'], file['title']))
			outpath = os.path.join(self.dir, "{} - {}".format(file['artist'], file['title']))
			os.mkdir(outpath)
			#convert to milliseconds
			#do this in two steps since it looks kinda messy in the lc
			times = [[value['t0'], value['t1'], key] for key,value in file['songlist'].items()]
			times = [(sum([float(x)*60**(t[0].count(':')-i) for i, x in enumerate(t[0].split(':'))])*1000, 
				sum([float(x)*60**(t[1].count(':')-i) for i, x in enumerate(t[1].split(':'))])*1000, t[2]) for t in times]
			#also need to sort it
			times = sorted(times, key=lambda x: x[0])
			#this just prints the times out, just a qc check
			print("\n\n{}".format("="*80))
			print("{:^80}".format("Converted times:"))
			print("{}\n\n".format("="*80))
			for x, y, title in times:
				print("{:>35}: {:>10}".format(x,y))
			print("="*80)
			print("\n\nCurrent file to chop: {}".format(inpath))
			print(" Current output path: {}".format(outpath))
			cont = raw_input("\nContinue? [Y/N]")

			if cont.lower() == "y":
				print("{:<60}".format("Acquiring audio track..."), end="")
				song = AudioSegment.from_mp3(inpath)
				print("DONE!")
				for i in range(len(times)):
					if os.path.isfile(os.path.join(outpath,'{0}.mp3'.format(times[i][2]))):
						print("Track {} of {} already exists: {}...".format(i+1, len(times), times[i][2]))
					else:
						print("Chopping track {} of {}: {} ...".format(i+1, len(times), times[i][2]))
						fl = song[times[i][0]:times[i][1]].export(os.path.join(outpath,'{0}.mp3'.format(times[i][2])),format='mp3')
						audiofile = eyed3.load(os.path.join(outpath,'{0}.mp3'.format(times[i][2])))
						audiofile.initTag()
						audiofile.tag.artist = u"{}".format(file['artist'])
						audiofile.tag.album = u"{}".format(file['album'])
						audiofile.tag.title = u"{0}".format(times[i][2])
						audiofile.tag.track_num = i + 1
						audiofile.tag.save()

				fl.close
				del fl
				print("Chop and label complete!")
			else:
				print("\nAborted!\n\n")