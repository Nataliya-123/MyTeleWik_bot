import telebot
TOKEN = "5743979069:AAFjszU7jzLlCvCvakvu8dKJPYSxbskIq4Q"
bot=telebot.TeleBot('5743979069:AAFjszU7jzLlCvCvakvu8dKJPYSxbskIq4Q')



@bot.message_handler(commands=['start'])
def help(message: telebot.types.Message):
    text = 'Привет!'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def start(message):
    message.text=message.text.lower()

    if message.text == 'привет':

        bot.send_message(message.from_user.id, "Как тебя зовут");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши Привет');


def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Отлично! Меня зовут Наташа. И я тестирую свой бот. Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'Отлично! Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
 #   while age == 3: #проверяем что возраст изменился
    try:
        age = int(message.text) #проверяем, что возраст введен корректно
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    else:
        bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

    bot.register_next_step_handler(message, say_by)

def say_by(message):
    message.text=message.text.lower()
    if message.text == "да":
        bot.send_message(message.from_user.id, "Ну, все с тобой ясно. Пока")
    elif message.text == "нет":
        bot.send_message(message.from_user.id, "Зачем тогда обманывать?")
    else:
        bot.send_message(message.from_user.id, "Ответь Да или Нет?")
    bot.register_next_step_handler(message, say_by_agane)

def say_by_agane(message):
    message.text = message.text.lower()
    if message.text == "пока":
        bot.send_message(message.from_user.id, "Иди уже домой")
    if message.text == "да":
        bot.send_message(message.from_user.id, "Ну, все с тобой ясно. Пока")
    if message.text == "нет":
        bot.send_message(message.from_user.id, "Зачем тогда обманывать?")
    else:
        bot.send_message(message.from_user.id, " Закончим разговор (✷‿✷)  ")
bot.polling(none_stop=True)