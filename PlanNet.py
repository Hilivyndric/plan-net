from aiogram import Bot, Dispatcher, executor, types
from app import keyboards as kb
from app import database as db
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)
PAYMENT_TOKEN = 'fddefwr'

async def on_startup(_):
    await db.db_start()
    print('Бот запустился')



# Вводные сообщения + кнопка вводная
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        'Шаблон “PlanNet” для Notion про <b>новый подход к дисциплине через осознанность.</b> \n \nБудь продуктивным, не виня себя. и радуясь своим успехам',
        parse_mode='html', reply_markup=kb.StartUsing)
    OpenningVideo = open('../birds.mp4', 'rb')
    await message.answer_video(OpenningVideo, reply_markup=kb.main)
    await db.cmb_start_db(message.from_user.id)
@dp.message_handler(text=kb.TemplateBTN)
async def templateBTN(message: types.Message):
    await message.answer(
        'Шаблон “PlanNet” для Notion про <b>новый подход к дисциплине через осознанность.</b> \n \nБудь продуктивным, не виня себя. и радуясь своим успехам',
        parse_mode='html', reply_markup=kb.StartUsing)
    OpenningVideo = open('../birds.mp4', 'rb')
    await message.answer_video(OpenningVideo)



# Кнопка HowToInsrBTN
@dp.message_handler(text=kb.HowToInsrBTN)
async def HowToInsrBTN(message: types.Message):
    await message.answer(
        'Все очень просто! \nПриобрести шаблон: /shop', parse_mode='html')
    InstrustionGIF = open("../open.gif", 'rb')
    await message.answer_animation(InstrustionGIF)

# Кнопка магазина
@dp.message_handler(text=kb.ShopBTN)
async def HowToInsrBTN(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Шаблон "PlanNet" для Notion', 'Перейти к оплате шаблона', 'invoice',
                           PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Шаблон "PlanNet" для Notion', 1500 * 100)])
@dp.message_handler(commands=['shop'])
async def HowToInsrBTN(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Шаблон "PlanNet" для Notion', 'Перейти к оплате шаблона', 'invoice',
                           PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Шаблон "PlanNet" для Notion', 1500 * 100)])



# колбеки (инлайн приветственное сообщение)
@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'Lets start':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Все очень просто! \nПриобрести шаблон: /shop')


# Обычные сообщения
@dp.message_handler()
async def unknown(message: types.Message):
    await message.reply('Не могу понять, что вы пишите :(')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
