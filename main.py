import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем токен
API_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Проверяем, что токен был загружен
if not API_TOKEN:
    print("Ошибка: TELEGRAM_TOKEN не найден в файле .env")
    exit()

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Клавиатура с кнопками
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("/ritual - Получить ритуал дня"))
menu_keyboard.add(KeyboardButton("/eco_tips - Экологический совет"))
menu_keyboard.add(KeyboardButton("/inspire - Мотивационная цитата"))
menu_keyboard.add(KeyboardButton("/reminder - Установить напоминание"))

# Команда /start
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    logging.debug(f"Received /start from {msg.from_user.id}")
    await msg.reply("Привет! Я помогу тебе с ежедневными практиками Эко Терапии. Вот что я могу:", reply_markup=menu_keyboard)

# Команда для получения ритуала
@dp.message_handler(commands=['ritual'])
async def ritual(msg: types.Message):
    logging.debug(f"Received /ritual from {msg.from_user.id}")
    await msg.reply(f"Ваш ритуал на сегодня: Прогулка в парке без телефона — сосредоточьтесь на звуках и запахах вокруг.", reply_markup=menu_keyboard)

# Команда для получения экологического совета
@dp.message_handler(commands=['eco_tips'])
async def eco(msg: types.Message):
    logging.debug(f"Received /eco_tips from {msg.from_user.id}")
    await msg.reply(f"Ваш экологичный совет: Используйте многоразовые сумки и контейнеры вместо пластиковых.", reply_markup=menu_keyboard)

# Команда для получения мотивационной цитаты
@dp.message_handler(commands=['inspire'])
async def inspire(msg: types.Message):
    logging.debug(f"Received /inspire from {msg.from_user.id}")
    await msg.reply(f"Вдохновляющая цитата на сегодня: «Мы не унаследовали Землю от наших предков, мы одолжили её у наших потомков.»", reply_markup=menu_keyboard)

# Команда для установки напоминания
@dp.message_handler(commands=['reminder'])
async def reminder(msg: types.Message):
    logging.debug(f"Received /reminder from {msg.from_user.id}")
    await msg.reply("Как часто вы хотите получать напоминания? Введите число в часах.", reply_markup=menu_keyboard)

# Запуск бота
if __name__ == '__main__':
    logging.debug("Starting bot...")
    executor.start_polling(dp, skip_updates=True)
