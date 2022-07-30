from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '5585930920:AAGxkFL0CKPprJOSsaq1Y_1DY0s6tn4i3e8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("test",
reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test",
web_app=WebAppInfo(url="https://ismoilov10.000webhostapp.com/"))))

@dp.message_handler(commands="durger")
async def durger(message: types.Message):
    await message.answer("durger", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Durger king", web_app=WebAppInfo(url="https://ismoilov299.000webhostapp.com"))))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)