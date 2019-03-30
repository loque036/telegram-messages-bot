This is a Telegram bot coded in python that sends you a message every 1.5 seconds.


Installation:

Clone this repo to your pc
```
git clone https://github.com/loque036/telegram_messages_bot/
```
Install requirements
```
pip3 install requirements.txt
```
edit bot.py with nano
```
sudo nano bot.py
```
Replace ```Bot_API_Key``` with your bot's api key. You can get it from https://t.me/BotFather (don't delete the quotes)

Replace ```Your_ID``` with your Telegram ID. You can get it with a bot like Marie or Rose and replying to yourself with /info (again, don't delete the quotes)

Save changes

To run just type 
```
python3 bot.py
```

If you want to change the frequency messages are sent just replace the 1.5 here
```
time.sleep(1.5)
```
with the number of seconds between messages
