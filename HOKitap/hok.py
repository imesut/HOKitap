# -*- coding: utf-8 -*-
import os

log_file = open("log.txt", "a")

def space(adres):
    return adres.replace(" ", "\ ")

def ho_kitap(klasor, basla):
    alt_klasorler = os.listdir(klasor)
    for i in alt_klasorler:
        if not i.find(".")>=0: #hided files
            alt_klasor = klasor + i #full path
            isim = i #to book name
            ses_sayac = 1
            for file in os.listdir(alt_klasor): #go into sound files

                if not file.startswith("."): #hided files
                    file = alt_klasor + "/" + file #full path
                    file = space(file) #full path re-touch for spaces
                    if file == alt_klasor + "/" + str(basla) + ".mp3": #If book has book name sound
                        break #this file shouldn't evaluated, because it cause a chain to delete files

                    #changing voice files
                    cmd = "mv " + file + " " + space(alt_klasor) + "/" + str(basla) + "_" + "0"*(3-len(str(ses_sayac))) + str(ses_sayac) + ".mp3"
                    os.system(cmd) #execution
                    ses_sayac += 1 #increase number on voice files

            #Create book name voice record by screen reader
            os.system("say -v Yelda -o " + space(alt_klasor) + "/" + str(basla) + ".aiff " + "'" + isim + "'")

            #Convert to mp3
            os.system("ffmpeg -i " + space(alt_klasor) + "/" + str(basla) + ".aiff " + space(alt_klasor) + "/" + str(basla) +".mp3")
            #Delete aiff file
            os.system("rm " + space(alt_klasor) + "/" + str(basla) + ".aiff")

            #Create wav Files from mp3 files
            for file in os.listdir(alt_klasor):
                if str(alt_klasor + "/" + file).endswith(".mp3"):
                    cmd = "ffmpeg -i " + space(alt_klasor) + "/" + file +" -acodec pcm_u8 -ar 10000 " + space(alt_klasor) + "/" + file[:-3]+"wav"
                    os.system(cmd)

            #Change folder name
            cmd = "mv " + space(alt_klasor) + " " + str(basla)
            os.system(cmd) #Exceution

            log_file.write("Klasör no: " + str(basla) + " Parça sayısı: " + str(ses_sayac) + " Kitap ismi: " + isim)
            log_file.write("\n")

            basla += 1 #increase number on folder

#for example
ho_kitap("/Users/mesut/HOKitap/", 4090)