from googletrans import Translator
import logging
from aiogram.types import Message, CallbackQuery
from config import TOKEN 
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
logging.basicConfig(level=logging.INFO)
tr=Translator()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>SALOM! \nMen tarjima botman! Iltimos so'z kiriting: </b>",parse_mode="HTML")

@dp.message_handler()
async def echo(message: types.Message):
	global word
	word = message.text
	await message.answer("Tilni tanlang...👇", reply_markup=language)

@dp.callback_query_handler(text="en")
async def english(call: CallbackQuery):
	display=tr.translate(word,dest="en")
	await call.message.answer(display.text)


@dp.callback_query_handler(text="ru")
async def russian(call: CallbackQuery):
	display=tr.translate(word,dest="ru")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="tr")
async def turkish(call: CallbackQuery):
	display=tr.translate(word,dest="tr")
	await call.message.answer(display.text)

@dp.callback_query_handler(text="tg")
async def tajik(call: CallbackQuery):
	display=tr.translate(word,dest="tg")
	await call.message.answer(display.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




# #Birinchi ko'rinish
# tarjima = Translator()
# display = tarjima.translate("salom",dest="ru")
# print(display)

# #Ikkinchi ko'rinish
# tarjima = Translator()
# word = input("So'zni kiriting: ")
# display = tarjima.translate(word,dest="ru")
# print(display.text)

# #Uchinchi ko'rinish
# tarjima = Translator()
# word = input("So'zni kiriting: ")
# language = input("Tarjima qilmoqchi bo'lgan tilni kiriting: ")
# display = tarjima.translate(word,dest=language)
# print(display.text)