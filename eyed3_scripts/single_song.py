import eyed3
'''
in this case I simply downloaded the video from youtube and converted to mp3 using mp4tomp3.py. Something must be fundamentally different between files obtained fresh from conversion and files that are obtained from chopping, the chopped files don't seem to need you to use audofile.initTag() otherwise audiofile.tag will be None
'''

audiofile = eyed3.load("/home/m/Music/new_mp4s/The Mamas & the Papas - California Dreamin'.mp3")

audiofile.initTag()
audiofile.tag.album	= u'If You Can Believe Your Eyes And Ears'
audiofile.tag.artist = u'The Mamas & the Papas'
audiofile.tag.title = u"California Dreamin'"
audiofile.tag.track_num = 1
audiofile.tag.save()
