from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


language = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🇺🇸 English", callback_data="en"),
			InlineKeyboardButton("🇷🇺 Русский", callback_data="ru"),
			InlineKeyboardButton("🇹🇷 Turkish", callback_data="tr")
		],
		[
			InlineKeyboardButton("🇹🇯 Tajik", callback_data="tg")
		]
	],
)