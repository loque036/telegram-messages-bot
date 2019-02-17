# This Python file uses the following encoding: utf-8
import os
import sys
import time
import telepot

print("")
print("Sending messages")
print("")

# Bot API Key
bot = telepot.Bot("Bot_API_Key",)

# Number your counter starts with
counter = 0
while True:
    counter = counter+1
    bot.sendMessage("Your_ID", "{c}".format(c=counter))
    time.sleep(1.5)
    sys.stdout.write("\r" + str(counter))
