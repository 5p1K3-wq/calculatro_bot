import ptbot

TOKEN = '1241115564:AAGtv97ps9Yxma3lfAcNpPF5qi5SQSzTsMA'
CHAT_ID = '134640247'

bot = ptbot.Bot(TOKEN)
bot.send_message(CHAT_ID, "Бот запущен")