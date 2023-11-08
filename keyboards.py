from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

TemplateBTN = 'Шаблон "PlanNet"️'
HowToInsrBTN = 'Как установить'
ShopBTN = 'Магазин'
main = ReplyKeyboardMarkup(resize_keyboard=True).add(TemplateBTN).add(HowToInsrBTN, ShopBTN)

StartUsing = InlineKeyboardMarkup(row_width=1)
StartUsing.add(InlineKeyboardButton(text='Начать пользоваться', callback_data='Lets start'))
