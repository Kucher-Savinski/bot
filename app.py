from config import keys, token
from extensions import ConvertException, CryptoConverter, GetAPI
import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате:\n<имя_валюты>\
        <в какую валюту перевести>\n<колличество переводимой валюты>\
        \nУвидеть список доступных валют: /currencies'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def exchange(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertException('Неправильное количество параметров')
        base, quote, amount = values
        CryptoConverter.convert(base,quote,amount)
        result = GetAPI.get_price(base,quote,amount)
        bot.send_message(message.chat.id, base + ' в ' + quote + ' || ' + str(amount) + ' = ' + result)
    except Exception:
        bot.reply_to(message, 'Не удалось обработать запрос')



if __name__ == '__main__':
    bot.polling()
