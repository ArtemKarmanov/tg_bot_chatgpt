from telebot.types import Message

from loader import bot

from api.chatgpt_ai import send_message_chatgpt


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    """
    Стартовое обращение к ChatGPT.

    :param message: Сообщение
    :return: None
    """

    chatgpt_message = send_message_chatgpt(start=True)
    bot.send_message(message.chat.id, chatgpt_message)


@bot.message_handler()
def communication_ai(message: Message) -> None:
    """
    Основное общение с ChatGPT.

    :param message: Сообщение
    :return: None
    """
    chatgpt_message = send_message_chatgpt(msg=message.text)
    bot.send_message(message.chat.id, chatgpt_message)
