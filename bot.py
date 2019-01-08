import os
import sys
import time
import telebot
import json
import ast
from os import environ
from ast import literal_eval

print("")
print("Sending messages")
print("")

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

counter = 0
while True:
    try:
        counter = counter+1
        bot.send_message("396438461", "{c}".format(c=counter))
        sys.stdout.write("\r" + str(counter))
    except telebot.apihelper.ApiException as e:
        print(e.args[0].split('\n')[-1])
        print(literal_eval(literal_eval(e.args[0].split('\n')[-1])[0])["parameters"]["retry_after"])
        raise
        sys.stdout.write("\r" + str(counter))
    finally:
        time.sleep(1.5)
        counter = counter
