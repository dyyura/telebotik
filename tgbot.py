import telebot  #Давайте импортируем библиотеку
import config  #и создадим наш файлик конфиг который будет принимать значение Токена 
# который нам предоставит БОТ ФАЗЕР отец всех ботов

bot = telebot.TeleBot(config.TOKEN) # здесь я использую встроенную функцию которую предоставляет библиотека pytelegrambotapi
# и передаю свой токен для активации своего бота


@bot.message_handler(commands=['start']) #Так как telebot уже имеет свой встроеную функцию мы приминяем декоратор для добавления неких значений
def welcome(message): #называю функцию и передаю аргумент
  sti = open("static/sticker.webp", "rb") #я хочу чтобы при старте бот отправил сперва мне гифку
  bot.send_sticker(message.chat.id, sti) # и вызываю библиотеку бот с функцией  
bot.polling(none_stop=True)
