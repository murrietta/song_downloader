#explanation of the dictionaries:
#url is the url of the youtube video
#artist is the name of the artist, this will be used in the artist field for the ID3 tag, will also be combined with `title` to make a temporary file name
#title is the name of the video, this is just used to make a temporary file name
#album is the name of the album, this will be used in the album field of the ID3 tag
#autotag is a boolean variable that specifies to the main program if this file should be given ID3 tags after strip
#songlist is a list of the songs inherent in the file. if file contains only one song then only one key-value pair needs to be specified. the keys are song titles that will be used in the ID3 tag of the individual song. the t0 and t1 keys of the child dictionary are endpoints specified in hh:mm:ss or mm:ss or m:ss format. the endpoints are used in the pydub chopping process. if there is only one song listed no chopping occurs.

#autostrip specifies to the master to auto

urls = [
	# {"url" : 'https://www.youtube.com/watch?v=MCs_1EFmjkg',
	#  "artist" : "Com Truise",
	#  "title" : "Galactic Melt",
	#  "album" : "Galactic Melt",
	#  "autotag" : False,
	#  "songlist" : {
	#  	"song01_title" : {"t0" : "0:00", "t1" : "1:25"},
	#  	"song02_title" : {"t0" : "1:25", "t1" : "3:25"},
	#  	"song03_title" : {"t0" : "3:25", "t1" : "5:25"} 
	#  	}
	# },
	# {"url" : 'https://www.youtube.com/watch?v=oAG_k4VUeTs',
	#  "artist" : "Outkast",
	#  "title" : "ATliens",
	#  "album" : "ATliens",
	#  "autotag" : False,
	#  "songlist" : {
	#  	"song01_title" : {"t0" : "0:00", "t1" : "1:25"},
	#  	"song02_title" : {"t0" : "1:25", "t1" : "3:25"},
	#  	"song03_title" : {"t0" : "3:25", "t1" : "5:25"} 
	#  	}
	# },
	{"url" : 'https://www.youtube.com/watch?v=wtHAKEZzrl8',
	 "artist" : "Tool",
	 "title" : "The Patient",
	 "album" : "Lateralus",
	 "autotag" : True,
	 "songlist" : {
	 	"The Patient" : {"t0" : "0:00", "t1" : "7:14"} 
	 	}
	}
	]

autostrip = True #main imports this, if True then performs mp4 to mp3 conversion
