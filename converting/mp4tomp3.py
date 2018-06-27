'''
this isn't my work, I got this from someone else, I'll have to find his website...
in any case, you can't just run this from cmd or powershell in windows you will need
windows 10 (or whatever version started to allow bash on ubuntu on windows) and also
have set up bash on ubuntu on windows. From there you need to install lame and mplayer
as described in the original author's instructions below

2018-06-25: modified this to be run by a master script that downloads, converts to mp3, "cuts" any songs or sections from larger file, and adds id3 tags. put it in a class so that the original command line use is still possible
'''


# MP4 TO MP3 CONVERSION SCRIPT
# script to convert mp4 video files to mp3 audio
# useful for turning video from sites such as www.ted.com into audio files useable
# on any old mp3 player.
#
# usage: python mp4tomp3.py [input directory [output directory]]
# input directory (optional)  - set directory containing mp4 files to convert (defaults to current folder)
# output directory (optional) - set directory to export mp3 files to (defaults to input)
#
# NOTE: you will need python 2, mplayer and lame for this script to work
# sudo apt-get install lame
# sudo apt-get install mplayer
# sudo apt-get install python2.7


from subprocess import call     # for calling mplayer and lamedirectories
import os                       # help with file handling

class mp4converter:

    def __init__(self, indir, outdir):
        self.indir = indir
        self.outdir = outdir

    def check_file_exists(self, directory, filename, extension):
        path = directory + "/" + filename + extension
        return os.path.isfile(path)

    def run(self):
        try:
            # check specified folders exist
            if not os.path.exists(self.indir):
                exit("Error: Input directory \'" + self.indir + "\' does not exist. (try prepending './')")
            if not os.path.exists(self.outdir):
                exit("Error: Output directory \'" + self.outdir + "\' does not exist.")
            if not os.access(self.outdir, os.W_OK):
                exit("Error: Output directory \'" + self.outdir + "\' is not writeable.")

            print "[%s/*.mp4] --> [%s/*.mp3]" % (self.indir, self.outdir)
            files = [] # files for exporting
                
            # get a list of all convertible files in the input directory
            filelist = [ f for f in os.listdir(self.indir) if f.endswith(".mp4") ]
            for path in filelist:
                basename = os.path.basename(path) 
                filename = os.path.splitext(basename)[0]
                files.append(filename)
            # remove files that have already been outputted from the list
            files[:] = [f for f in files if not self.check_file_exists(self.outdir, f, ".mp3")]
        except OSError as e:
            exit(e)
        
        if len(files) == 0:
            exit("Could not find any files to convert that have not already been converted.")

        # convert all unconverted files
        for filename in files:
            print "-- converting %s.mp4 to %s.mp3 --" % (self.indir + "/" + filename, self.outdir + "/" + filename)
            call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", self.indir + "/" + filename + ".mp4"])
            call(["lame", "-h", "-b", "192", "audiodump.wav", self.outdir + "/" + filename + ".mp3"])
            os.remove("audiodump.wav")


if __name__ == "__main__":
    from sys import argv            # allows user to specify input and output 

    # set the default directories and try to get input directories
    args = [".", "."]
    for i in range(1, min(len(argv), 3)):
        args[i - 1] = argv[i]

    # if only input directory is set, make the output directory the same
    if len(argv) == 2:
        args[1] = args[0]

    mcon = mp4converter(args[0], args[1])
    mcon.run()