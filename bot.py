import os
from django import setup
# Задайте переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devfiles.settings")

# Вызовите функцию setup() для настройки Django
setup()


from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from django.core.files.base import ContentFile
from files.models import TelegramFile
from django.http import HttpResponse


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне /getfile <file_id>, чтобы получить файл по его ID.')

def get_file(update: Update, context: CallbackContext) -> None:
    try:
        file_id = context.args[0]
        telegram_file = TelegramFile.objects.get(number=file_id)

        # Отправляем файл пользователю
        file_url = telegram_file.disk_link
        
        update.message.reply_text(f'Ваш файл: {file_url}')

    except TelegramFile.DoesNotExist:
        update.message.reply_text('Файл с указанным ID не найден.')

    except IndexError:
        update.message.reply_text('Пожалуйста, укажите ID файла после команды /getfile.')

def main() -> None:
    # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
    updater = Updater(token='6838826201:AAHDRL6GNTA417dt68IF2_blewjUN2lUkcw',use_context=True, )
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("getfile", get_file))

    # Запускаем бота
    updater.start_polling(timeout=600)
    updater.idle()

if __name__ == '__main__':
    main()
