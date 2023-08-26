from aiogram import Bot, Dispatcher, types, executor
from config import token 
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO) 

direction_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Объекты'),
    types.KeyboardButton('Контакты') 
] 

direction_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*direction_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer() 

@dp.message_handler(text='О нас') 
async def backend(message:types.Message):
    await message.answer("https://vg-stroy.com/about/") 
  
@dp.message_handler(text='Объекты')
async def backend(message:types.Message):
    await message.answer("Наши объекты") 
    await message.answer_photo("https://vg-stroy.com/completed_objects/")

@dp.message_handler(text='Контакты')
async def backend(message:types.Message):
    await message.answer("https://vg-stroy.com/contacts/") 
executor.start_polling(dp)