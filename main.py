from discord.ext import commands
import json

token = json.load(open('token.json'))
bot = commands.Bot(command_prefix="-")

bot.run(token)
