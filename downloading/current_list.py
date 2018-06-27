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
	{"url" : 'https://www.youtube.com/watch?v=_sznCpMlUnI',
	 "artist" : "Gipsy Kings",
	 "title" : "Greatest Hits",
	 "album" : "Greatest Hits",
	 "autotag" : True,
	 "songlist" : {
	 	"Djobi Djoba" : {"t0" : "0:01", "t1" : "3:26"},
	 	"Baila Me" : {"t0" : "3:26", "t1" : "7:13"},
	 	"Bamboleo" : {"t0" : "7:13", "t1" : "10:39"},
	 	"Pida Me La" : {"t0" : "10:39", "t1" : "13:58"},
	 	"Bem, Bem, Maria" : {"t0" : "13:58", "t1" : "17:04"},
	 	"Volare" : {"t0" : "17:04", "t1" : "20:45"},
	 	"Moorea" : {"t0" : "20:45", "t1" : "24:49"},
	 	"A Mi Manera" : {"t0" : "24:49", "t1" : "28:23"},
	 	"Un Amor" : {"t0" : "28:23", "t1" : "32:13"},
	 	"Galaxia" : {"t0" : "32:13", "t1" : "34:50"},
	 	"Escucha Me" : {"t0" : "34:50", "t1" : "39:29"},
	 	"Tu Quieres Volver" : {"t0" : "39:29", "t1" : "42:44"},
	 	"Soy" : {"t0" : "42:44", "t1" : "45:57"},
	 	"La Quiero" : {"t0" : "45:57", "t1" : "49:43"},
	 	"Allegria" : {"t0" : "49:43", "t1" : "52:33"},
	 	"Vamos a Bailar" : {"t0" : "52:33", "t1" : "57:30"},
	 	"La Dona" : {"t0" : "57:30", "t1" : "1:02:06"},
	 	"Medley" : {"t0" : "1:02:06", "t1" : "1:07:06"}
	 	}
	}
	]

autostrip = True #main imports this, if True then performs mp4 to mp3 conversion
