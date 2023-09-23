import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def send_message_chatgpt(msg: str = None, start: bool = False) -> str:
	"""
	Взаимодействие пользователя с ChatGPT.

	:param msg: Сообщение пользователя
	:param start: Проверка первое ли это обращение
	:return: completion.choices[0].message.content
	"""
	# Если обращение первое, то задаем ChatGPT как помощника покупки билетов
	if start:
		msg = 'Ты помощник для покупки билетов.'

	# Подключение к ChatGPT
	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": 'assistant', "content": msg}
		]
	)

	# Проверка на ошибку запроса
	if not completion:
		return 'Ошибка запроса к ChatGPT. Попробуйте снова со стартовой команды /start.'

	# Вывод сообщения
	return completion.choices[0].message.content
