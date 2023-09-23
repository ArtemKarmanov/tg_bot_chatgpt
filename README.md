# Телеграм-бот «ChatGPT для покупки билетов»
## Содержание
* [Краткое описание](#description)
* [Установка и настройка](#install)
  * [Перед тем, как начать](#install-python)
  * [Клонирование репозитория](#install-git)
  * [Установка библиотек](#install-utils)
  * [Создание бота в телеграм (BotFather)](#install-botfather)
  * [Ключ от AI ChatGPT](#install-api)
  * [Файл .env](#install-env)
  * [Запуск бота](#install-start)
* [Команды](#commands)
  * [Команда /start](#command-start)
* [Используемые библиотеки](#utils)

<a name="description"></a>
## Краткое описание
Телеграм-бот «ChatGPT для покупки билетов» позволяет использовать нейросеть ChatGPT 3.5 для любой помощи в покупке каких-либо билетов.

Телеграм-бот составлен на основе библиотеки [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI "Переход к библмотеке pyTelegramBotAPI").

Для разработки и функционирования использовался AI ChatGPT 3.5 turbo.

<a name="install"></a>
## Установка и настройка
Эти инструкции помогут развернуть проект на локальном компьютере для использования.

<a name="install-python"></a>
### Перед тем, как начать
* Проверьте, что у вас установлен `Python` и есть виртуальное пространство

<a name="install-git"></a>
### Клонирование репозитория
* Перейдите в папку проекта и выполните команду `git clone`, чтобы скопировать файлы репозитория
```
https://github.com/PanicNyan/tg_bot_chatgpt.git
```

<a name="install-utils"></a>
### Установка библиотек
* Перейдите в папке проекта к файлу `requirements.txt` и введите команду в консоль для установки всех библиотек
```
pip install -r requirements.txt
```

<a name="install-botfather"></a>
### Создание бота в телеграм (BotFather)
* Найдите бота BotFather в телеграм и создайте нового бота командой `/newbot`
* Следуя инструкции, укажите название и username бота. Скопируйте отправленный вам токен бота.

<a name="install-api"></a>
### Ключ от AI ChatGPT
* Получите ключ с AI ChatGPT 3.5 turbo и скопируйте его для использования в боте.

<a name="install-env"></a>
### Файл .env
* Скопируйте файл `.env.template` или его содержимое и сохраните под именем нового файла `.env`
* Укажите все полученные данные в файле `.env` в ковычках
  * Токен созданного бота в BotFather в переменной **BOT_TOKEN**
  * Ключ от AI в переменной **OPENAI_API_KEY**

```
BOT_TOKEN = "Токен для бота, полученный от @BotFather"
OPENAI_API_KEY = "Ключ от API ChatGPT 3.5 turbo"
```
<a name="install-start"></a>
### Запуск бота
* Запустите файл main.py в папке проекта

<a name="commands"></a>
## Команды

<a name="command-start"></a>
### Команда /start
По команде /start сразу происходит стартовое взаимодействие с ChatGPT и отправляется инструкция для работы нейросети как помощника в поиске билетов.\
Следующие сообщения пользователя происходят в режиме диалога.

<a name="command-help"></a>


<a name="utils"></a>
## Используемые библиотеки
aiohttp==3.8.5\
aiosignal==1.3.1\
async-timeout==4.0.3\
attrs==23.1.0\
certifi==2023.7.22\
charset-normalizer==3.2.0\
frozenlist==1.4.0\
idna==3.4\
multidict==6.0.4\
openai==0.28.0\
pyTelegramBotAPI==4.13.0\
python-dotenv==1.0.0\
requests==2.31.0\
tqdm==4.66.1\
urllib3==2.0.5\
yarl==1.9.2\
