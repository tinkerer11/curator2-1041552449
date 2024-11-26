from telebot import TeleBot

bot = TeleBot('5587269560:AAH1YtonXP4qfOOYtX879_QcLVHRLOTSw7c')


# Обработка команды start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, это мой первый бот на python')


# Обработка команды help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'тут будут подсказки по боту')


# Обработка команды search
@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, 'ссылка на [поисковик Яндекс](https://ya.ru/)', parse_mode='Markdown')


# Обработка команды products
@bot.message_handler(commands=['products'])
def products(message):
    bot.send_message(message.chat.id, '*список товаров*\nТовар1\nТовар2', parse_mode='Markdown')


# Обработка команды question
@bot.message_handler(commands=['question'])
def question(message):
    bot.send_message(message.chat.id, '_Напишите ваш вопрос:_', parse_mode='Markdown')


bot.infinity_polling()