import ptbot
from pytimeparse import parse
from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def reply(text):
    number_second = parse(text)
    id_message = bot.send_message(CHAT_ID, 'Таймер запущен на {} секунд'.format(number_second))
    bot.create_timer(number_second, notify)
    bot.create_countdown(number_second, notify_progress, id_message=id_message, total_progress=number_second)


def notify():
    bot.send_message(CHAT_ID, 'Время вышло!')


def notify_progress(secs_left, id_message, total_progress):
    bot.update_message(CHAT_ID, id_message, render_progressbar(total_progress, secs_left,
                                                               'Осталось секунд(ы) {}\n'.format(secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


bot = ptbot.Bot(TOKEN)
bot.send_message(CHAT_ID, 'На сколько запустить таймер?')
bot.reply_on_message(reply)


bot.run_bot()
