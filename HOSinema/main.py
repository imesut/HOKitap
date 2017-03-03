#! /usr/bin/env python

import os

print "\nUsage is ./main.py"
print "It is uses static filename"
print "Be sure your pseudo mp3 file is named as filename.mp3"

if raw_input("If it is right, press enter, if not please rename then press enter"):
    pass

filename = "filename.mp3"
number = 37

os.system("mv " + filename + " " + str(number) + ".mp3")

filename = str(number) + ".mp3"

fullmedialistfile = open(filename+".txt", "w")
fullmedialistfile.write(filename)
fullmedialistfile.close()

fullmedialist = filename + ".txt"
config = "amdb_config.config"
output = "full_media.amdb"


os.system("./amDbBuilder.py -i " + fullmedialist + " -c " +config+ " -o " + output)

os.system("mv " + filename + " hayalortagim/static/media/sinemalar/" + filename)
os.system("mv " + output + " hayalortagim/static/media/sinemalar/" + output)
os.system("rm -f " + fullmedialist)
