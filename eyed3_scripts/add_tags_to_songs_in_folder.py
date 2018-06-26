import eyed3
import os
from albums.current import *
#import pth and albuminfo variables

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

files = [x for x in os.listdir(pth) if x.endswith('.mp3') == True]

#check for track numbers
nums = True
for i,x in enumerate(files):
	if is_number(x.split(" ",1)[0].strip(".")) == False:
		nums = False
		if i > 0:
			print "\n\n{}".format("="*60)
			print "{:^50}".format("TRACK LISTING WARNING")
			print "\nNot all files had an inherent track listing at the start of the file names.\n\nIf a specific listing is desired make sure all files start with a track number.\n\nListing will default to ascending index based on alphabetical file listing."
			print "\n\n{}".format("="*60)
		break
if nums == True:
	print "\n\n{}".format("="*60)
	print "{:^50}".format("TRACK LISTING NOTE")
	print "\nFiles appear to have a track listing specified that will be used."
	print "\n\n{}".format("="*60)
	
print "\n\nNOTE: This script assumes the file format of '<Artist Name> - <Track Name>'"
print "\n\nCurrent Album Name: {}\n\nAdd tags for the following?".format(albuminfo['name'])
print "\n"
#print "{:>50}".format("Filename")
#print "{:^60}\n".format("="*60)
for file in files:
	print "{:>50}".format(file)

cont = raw_input("\nContinue? [Y/N]")
if cont.upper() == "Y":
	for i,fl in enumerate(files):
		print "Creating tag info for {:<60}".format(fl),
		audiofile = eyed3.load(os.path.join(pth,fl))
		audiofile.initTag()
		audiofile.tag.album = albuminfo['name']
		if nums == True:
			#then use the number at the front of the file name, will need to remove it to use the rest of this code
			trk_num = int(fl.split(" ",1)[0].strip("."))
			audiofile.track_num = trk_num
			fl = fl.split(" ",1)[1].strip()
		else:
			audiofile.track_num = i + 1
		audiofile.tag.artist = unicode(fl.split(" - ")[0])
		audiofile.tag.title = unicode(fl.split(" - ")[1].strip('.mp3'))
		audiofile.tag.save()
		print "{:>20}".format("Done!")
else:
	print "\nCanceled!\n"