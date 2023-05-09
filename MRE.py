from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from uuid import uuid4
from loguru import logger
import MREDB
bot = AsyncTeleBot("token")
to_test = MREDB.MreMeal()

HELP_MESSAGE = """
Commands:

⚪ /help – Show help
⚪ /start – Start bot & show help
"""


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, HELP_MESSAGE)


@bot.message_handler(commands=['deposit'])
async def deposit(message: Message):
    keyboard = [
        [
            InlineKeyboardButton("💲1", callback_data="deposit-1"),
            InlineKeyboardButton("💲25", callback_data="deposit-25"),
            InlineKeyboardButton("💲35", callback_data="deposit-35"),

        ],
        [
            InlineKeyboardButton("$50", callback_data="deposit-50"),
            InlineKeyboardButton("$75", callback_data="deposit-75"),
            InlineKeyboardButton("$100", callback_data="deposit-100"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.send_message(message.chat.id, "How much would you like to deposit?", reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("deposit"))
async def deposit_callback(call: CallbackQuery):
    amount_usd = int(call.data.split("-")[1])
    order_id = str(uuid4())
    print(f"order_id: {order_id}")
    resp = await to_test.fetch()
    await bot.answer_callback_query(callback_query_id=call.id, text="Processing payment")

asyncio.run(bot.polling())
