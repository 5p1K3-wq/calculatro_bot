# Calculator bot
Telegram bot for countdown time with progress bar.

## Getting started
### Manual instruction
1. **Clone the repository** 
`
git clone https://github.com/5p1K3-wq/calculatror_bot.git
`
2.  **Open directory**
`cd calculator_bot/`
3.  **We start the setup script**
`python3 setup.py`
4.  **Specify the values for the following variables:**
    *   `TOKEN` - API key telegram bot
    *   `CHAT_ID` - ID of your chat with bot. You can find it out using [Bot-reference](https://telegram.me/userinfobot)
5.  **Run a script `python3 main.py` that will run telegram-bot**

![](https://dvmn.org/media/filer_public/af/4e/af4e30a5-7c7a-4bbe-8472-0aeb8d4cc1f1/timer-in-telegram.gif)

## Built With
[python-dotenv 0.13.0](https://pypi.org/project/python-dotenv/) - It allows you to load environment variables from the 
.env file in the root directory

[python-telegram-bot 12.7](https://pypi.org/project/python-telegram-bot/) - This library provides a pure Python interface 
for the Telegram Bot API. It’s compatible with Python versions 3.5+ and PyPy.

[pytimeparse 1.1.8](https://pypi.org/project/pytimeparse/) - A small Python library to parse various kinds of time 
expressions.
