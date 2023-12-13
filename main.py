import telebot, requests
import config

bot_token = config.token
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-визитка Никита. Я могу рассказать о себе или о ком-то еще. Просто спроси меня!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Я могу предоставить информацию о себе или о ком-то еще. Просто спроси меня о чем-то конкретном! Также у меня есть команда /calc. После нее ты можешь писать выражение, и я посчитаю его. Еще у меня есть функция /advert, которая расскажет тебе об одном интересном проекте!")

@bot.message_handler(commands=['calc'])
def handle_calc(message):
    try:
        expression = message.text.split(' ', 1)[1]
        result = eval(expression)
        bot.send_message(message.chat.id, f"Результат: {result}")
    except (SyntaxError, NameError, ZeroDivisionError):
        bot.send_message(message.chat.id, "Ошибка в выражении. Пожалуйста, введите корректное математическое выражение.")
    except IndexError:
        bot.send_message(message.chat.id, "Пожалуйста, введите математическое выражение после команды /calc.")

def send_advert(chat_id):
    advert_message = "Учи программирование с Яндекс Практикумом! Получи профессию мечты и стань IT-специалистом."
    bot.send_message(chat_id, advert_message)

@bot.message_handler(commands=['advert'])
def handle_advert(message):
    send_advert(message.chat.id)

@bot.message_handler(func=lambda message: True)
def text(message):
    if "информация" in message.text.lower():
        bot.send_message(message.chat.id, "Меня зовут Бот-визитка Никита. Мой возраст неизвестен. Мои хобби - отвечать на вопросы пользователей и узнавать новое!")
    elif "имя" in message.text.lower():
        bot.send_message(message.chat.id, "Меня зовут Бот-визитка Никита.")
    elif "никита" in message.text.lower():
        bot.send_message(message.chat.id, "Это программист, который написал меня. Он учиться в лицее и любит программировать и играть в футбол, вообщем парень молодец :)")
    else:
        bot.send_message(message.chat.id, "Прости, я не понимаю тебя. Попробуй спросить что-то другое или воспользуйся командой /help.")

if __name__ == '__main__':
    bot.polling()