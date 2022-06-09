from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


language = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🇺🇸 English", callback_data="en"),
			InlineKeyboardButton("🇷🇺 Русский", callback_data="ru"),
			InlineKeyboardButton("🇹🇷 Turkish", callback_data="tr")
		],
		[
			InlineKeyboardButton("🇹🇯 Tajik", callback_data="tg"),
			InlineKeyboardButton("🇦🇪 Arabic", callback_data="ar"),
			InlineKeyboardButton("🇫🇷 French", callback_data="fr")
		],
		[
			InlineKeyboardButton("🇰🇷 Korean", callback_data="ko"),
			InlineKeyboardButton("🇯🇵 Japanese", callback_data="ja"),
			InlineKeyboardButton("🇩🇪 German", callback_data="de")
		],
		[
			InlineKeyboardButton("🇬🇷 Greek", callback_data="el"),
			InlineKeyboardButton("🇮🇹 Italian", callback_data="it"),
			InlineKeyboardButton("🇪🇸 Spanish", callback_data="es")
		]
	],
)