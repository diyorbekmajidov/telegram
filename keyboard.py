import main

last_update_id=-1
while True:
    chat_id, text ,update_id = main.get_message()
    if last_update_id != update_id:
        bot.sendMessage(chat_id, text, reply_markup=telegram.ReplyKeyboardMarkup(keyboard=[[telegram.KeyboardButton("button 1")],
        [telegram.KeyboardButton('button 2')]]))
        last_update_id = update_id