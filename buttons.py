from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


language = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("๐บ๐ธ English", callback_data="en"),
			InlineKeyboardButton("๐ท๐บ ะ ัััะบะธะน", callback_data="ru"),
			InlineKeyboardButton("๐น๐ท Turkish", callback_data="tr")
		],
		[
			InlineKeyboardButton("๐น๐ฏ Tajik", callback_data="tg"),
			InlineKeyboardButton("๐ฆ๐ช Arabic", callback_data="ar"),
			InlineKeyboardButton("๐ซ๐ท French", callback_data="fr")
		],
		[
			InlineKeyboardButton("๐ฐ๐ท Korean", callback_data="ko"),
			InlineKeyboardButton("๐ฏ๐ต Japanese", callback_data="ja"),
			InlineKeyboardButton("๐ฉ๐ช German", callback_data="de")
		],
		[
			InlineKeyboardButton("๐ฌ๐ท Greek", callback_data="el"),
			InlineKeyboardButton("๐ฎ๐น Italian", callback_data="it"),
			InlineKeyboardButton("๐ช๐ธ Spanish", callback_data="es")
		]
	],
)