# -*- coding: utf-8 -*-
import os, sys
from telegram import File
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from keys import telegram_token
import logging

updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Calismaya Basladim")

def getpdf(bot, update):
    pdf_file = bot.getFile(update.message.document["file_id"])
    rfname = update.message.document["file_name"]
    if rfname[-4:] == ".pdf":
        pdf_file_name = str(update.message.document["file_id"]) + ".pdf"
        pdf_file.download(pdf_file_name)
        document = pdf_file_name
        txt_file_name = document + ".txt"
        os.system("pdf2txt.py -o " + txt_file_name + " " + document)
        mined_out = open(txt_file_name, "rb")
        lines = mined_out.readlines()
        cleanchar = ["\x0c"]
        text = ""
        for i in lines:
            print i
            if i.find("  ") >= 0:
                while not i.find("  ") >= 0:
                    i = i.replace("  ", " ")
            if len(str(i)) >= 3 and i.endswith("\r\n"):
                i = i[:-2]
            if i.endswith("-"):
                i = i[:-1]
            for ccitem in cleanchar:
                if i.find(ccitem) >= 0:
                    i = i.replace(ccitem, "\r\n")
            text = text + i
        save_file = open(txt_file_name, "w")
        save_file.write(text)
        save_file.close()
        bot.sendDocument(chat_id = update.message.chat_id, document = open(txt_file_name, "r"))
        text = ""

    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Şimdilik pdf alabiliyorum, zaten benim varlık amacım pdf...")

start_handler = CommandHandler('start', start)
getpdf_handler = MessageHandler(Filters.document, getpdf)
#voice_handler = MessageHandler(Filters.voice, voice)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getpdf_handler)
#dispatcher.add_handler(voice_handler)

updater.start_polling()
