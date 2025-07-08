from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging, json

API_TOKEN = '8080180295:AAHH8FdPQUqxWMNIkGsiJvbwMhmRVDKTM4w'
CHANNEL_USERNAME = '@kinotime1218'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

def load_codes():
    with open("codes.json", "r") as f:
        return json.load(f)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, message.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            await message.reply("✅ Obuna bo‘ldingiz!\n🎬 Kodni kiriting:")
        else:
            keyboard = types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton("📢 Obuna bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
            )
            await message.reply("❗ Avval kanalga obuna bo‘ling.", reply_markup=keyboard)
    except:
        keyboard = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("📢 Obuna bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        )
        await message.reply("❗ Obuna holati tekshirib bo‘lmadi. Avval kanalga obuna bo‘ling.", reply_markup=keyboard)

@dp.message_handler()
async def check_code(message: types.Message):
    codes = load_codes()
    code = message.text.strip()
    if code in codes:
        await message.reply(f"✅ Kod to‘g‘ri!\n🎬 Kino: {codes[code]}")
    else:
        await message.reply("❌ Noto‘g‘ri kod! Qaytadan urinib ko‘ring.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
