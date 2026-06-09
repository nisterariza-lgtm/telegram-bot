import telebot
import os
from flask import Flask
import threading

TOKEN = "8125684295:AAFWExjKLNGTN1JC2DSu6lTqsZDvRusPGOE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo', 'video', 'document'])
def delete_media(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass

app = Flask('')
@app.route('/')
def home(): 
    return "Bot Aktif"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

threading.Thread(target=run).start()
bot.infinity_polling()
