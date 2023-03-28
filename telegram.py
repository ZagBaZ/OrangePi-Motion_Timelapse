import datetime

import telebot

bot = telebot.TeleBot('<Token BotTelegram>')


@bot.message_handler(commands=['today'])
def today(message):
    try:
        today = datetime.datetime.today().strftime('%d-%m')
        video = open(f'/home/orangepi/dev/motion_timelapse/timelapse/Timelapse-{today}.mpg4', 'rb')
        bot.send_video(message.chat.id,  video)
    except FileNotFoundError:
        bot.send_message(message.chat.id, f'Таймлапса за {today} нету!')


@bot.message_handler(commands=['yesterday'])
def yesterday(message):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%d-%m')
    try:
        video = open(f'/home/orangepi/dev/motion_timelapse/timelapse/Timelapse-{yesterday}.mpg',  'rb')
        bot.send_video(message.chat.id,  video)
    except FileNotFoundError:
        bot.send_message(message.chat.id, f'Таймлапса за {yesterday} нету!')


@bot.message_handler(commands=['date'])
def date(message):
    bot.send_message(message.chat.id, f'Введитте дату в формате dd-mm:')
    bot.register_next_step_handler(message,  date_video)


def date_video(message):
    if message.text[2] == '-' and len(message.text) == 5:
        try:
            video = open(f'/home/orangepi/dev/motion_timelapse/timelapse/Timelapse-{message.text}.mpg',  'rb')
            bot.send_video(message.chat.id,  video)
        except FileNotFoundError:
            bot.send_message(message.chat.id, f'Таймлапса за {message.text} нету!')
    else:
        bot.send_message(message.chat.id, f'Некорректный ввод')


@bot.message_handler(content_types=['text'])
def on(message):
    users_name = message.chat.first_name
    bot.send_message(message.chat.id, f"Привет {users_name}!"
                                      f"\n/today"
                                      f"\n/yesterday"
                                      f"\n/date")


bot.polling(none_stop=True, interval=0)
