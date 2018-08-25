import discord
from discord.ext import commands

import asyncio
import random

botprefix = "$" # change this to change the bot's prefix. you will also have to modify '$hello' under on_message

bot = commands.Bot(command_prefix = botprefix)
token = "YOUR_BOT_TOKEN_HERE"

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if "`" in message.content:
    	return
    
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def hello(ctx):
    if ctx.message.author.id == "A_NOOBS_TOKEN_ID":
            await bot.say("No.")
            return

    if ctx.message.author.id == "YOUR_TOKEN_ID":
        msg = " my father"

    elif ctx.message.author.id == "YOUR_FRIENDS_TOKEN_ID":
        msg = " stupid faggot scripting minion"

    elif ctx.message.author.id == "YOUR_OTHER_FRIENDS_TOKEN_ID":
        msg = " milkiest man on the planet"

    else:
        msg = ""
    
    await bot.say(f"Hello there{msg}, {ctx.message.author.mention}!")

@bot.command()
async def prefix():
    await bot.say(f"My prefix is `{botprefix}`.")

@bot.command()
async def cookie():
    await bot.say("Here's a free cookie! :cookie:")

@bot.command()
async def panda():
    await bot.say("Here's a free portrait of myself! :panda_face:")

@bot.command()
async def dynamic():
	string = random.choice(
            ["dynamic TOY system !",
             "backpack system DYNAMIC",
             "dynamic HALAL machine",
             "dynamic MINEcraft KEY ! Generator!"])

	await bot.say(string)

@bot.command()
async def eightball(*, arg):
    string = random.choice(
        ["certain",
         "likely",
         "somewhat possible",
         "unlikely",
         "highly unlikely",
         "uncertain",
         "impossible"])

    await bot.say(f"The 8ball says that your outcome of {arg} is '{string}'.")

@bot.command(pass_context=True)
async def guildname(ctx):
    await bot.say(f"This is the '{ctx.message.server.name}' guild.")

@bot.event 
async def on_ready():
    print(f"> {bot.user.name} loading...")
    print("> Token loading...")
    print("> Script loaded in successfully.")
    print(f"> Bot name: {bot.user.name}")
    print(f"> Bot ID: {bot.user.id}")

bot.run(token) 
