import telebot

bot = telebot.TeleBot('6421741235:AAHihV1mgxQHrDARezvAnYegapK4W-yJ_Z8')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'На какую сумму пообедали?')

@bot.message_handler(commands=['twenty'])
def twenty_percent(message):
    summ = check + check * 0.2
    bot.send_message(message.chat.id, f'Если чаевые составляют 20%, то вы в итоге должны отдать: {int(summ)}')

@bot.message_handler(commands=['fifteen'])
def fifteen_percent(message):
    summ = check + check * 0.15
    bot.send_message(message.chat.id, f'Если чаевые составляют 15%, то вы в итоге должны отдать: {int(summ)}')

@bot.message_handler(content_types='text')
def response(message):
    global check
    check = int(message.text)
    bot.send_message(message.chat.id, 'Какой процент будет составлять чаевые? (/twenty, /fifteen)')


bot.infinity_polling()
