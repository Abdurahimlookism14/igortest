from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

token = dotenv_values(".env")["AAGwIyow0et_Q6WpxjXMRQi5cBccKtBsS8s"]
bot = Bot(token=token)
dp = Dispatcher()

