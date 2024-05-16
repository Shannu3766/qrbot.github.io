from aiogram import Bot, Dispatcher,executor, types
import pyqrcode
bot = Bot(token="Your telegram bot token ID")
dp=Dispatcher(bot)

@dp.message_handler(commands=["start","help"])
async def welcome(message :types.Message):
    await message.reply("hello world this is an qr code genrator!!!")
@dp.message_handler(commands=["logo"])
async def logo(message :types.Message):
    await message.answer_photo('https://th.bing.com/th/id/OIP.paYw8yErf53kXm0-upPe7AHaLF?w=186&h=278&c=7&r=0&o=5&dpr=1.3&pid=1.7')
    
@dp.message_handler()
async def df(message:types.Message):
    #await message.answer(message.text)
    text=pyqrcode.create(message.text)
    text.png('code.png',scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png','rb'))

executor.start_polling(dp)
