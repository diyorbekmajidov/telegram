import telegram

TOKEN = '5468504239:AAFnCFuZH99q0HYYF0iux_DGPrZoyFLwk9A'
bot = telegram.Bot(token=TOKEN)
user = bot.getMe()

def get_message():
    update = bot.getUpdates()
    reslut = update[-1]
    chat_id = reslut.message.chat.id 
    text = reslut.message.text
    photo = reslut.message.photo[0]
    update_id = reslut.update_id
    return chat_id, text, update_id, photo



last_update_id = -1
while True:
    chat_id, text ,update_id, photo = get_message()
    if last_update_id != update_id:
        if text != None :
            bot.sendMessage(chat_id,text)
        elif photo !=None:
            bot.send_photo(chat_id,photo)
        last_update_id = update_id        

