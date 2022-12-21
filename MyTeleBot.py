import telebot

token = ''

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    if 'Mary' in massage.text:
        text="Ба! Знакомые все лица!"
    else:
        text=massage.text
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)