import COVID19Py
import telebot

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('5200714348:AAEeGU7K0jeJqWTEFUJap6N5xVNv7wFKOsA')

latest = covid19.getLatest()
location = covid19.getLocationByCountryCode('US')
print(latest)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'<b>Привет {message.from_user.first_name}!</b>\nВведите страну'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


