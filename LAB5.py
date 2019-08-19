#! python3
from os import path, walk
from fnmatch import fnmatch
from mutagen.easyid3 import EasyID3
from sys import argv
import re

def showMusic():

    globPath = argv[-1]

    directory, glob = path.split(globPath)

    for (top, dirs, files) in walk(directory):
        for file in files:
            if fnmatch(file, glob):

                # "Normalizing the path just for safety"
                # This makes sure all of the path separators are correct for the OS etc..
                mp3FilePath = path.normpath(path.join(top, file))

                try:
                    media = EasyID3(mp3FilePath)
                    data = {  tagName:tagValue[0] for tagName,tagValue in media.items()}

                    args = [f.lstrip("-").split("=") for f in argv if f.startswith("--")]

                    tag, value = [(x,y) for x,y in args][0]

                    for tag,val in args:

                        # match expression with arguments
                        if re.match("^(The)*\s*\w.+", val):


                            if data["artist"] == val:

                                tmplt = "Found: {artist} {album} {title}"
                                print(tmplt.format(**data))

                            if data["title"] == val:

                                tmplt = "Found: {artist} {album} {title}"
                                print(tmplt.format(**data))

                            if data["album"] == val:

                                tmplt = "Found: {artist} {album} {title}"
                                print(tmplt.format(**data))
                            
                except Exception as e:
                    print("Could not read: " + file + " " + str(e))
                    print("Usage: LAB5.py [--artist=\"artistname\"] [--song=\"songname\"] [--album=\"albumname\"] fileGlob")


showMusic()
