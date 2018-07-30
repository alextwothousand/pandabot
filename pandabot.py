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

    if message.content == "$hello":

	    if message.author.id == "YOUR_CLIENT_ID_HERE": # NAME#TAG Client ID
	        msg = "my creator, my father, my overlord!"
	        
	    else:
	        msg = message.author.name

	    await bot.send_message(message.channel, f"Hello there {msg}!")

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
	rand = random.randint(1, 4)
	if rand == 1:
		string = "dynamic TOY system !"

	elif rand == 2:
		string = "backpack system DYNAMIC"

	elif rand == 3:
		string = "dynamic HALAL machine"

	elif rand == 4:
		string = "dynamic MINEcraft KEY ! Generator"

	await bot.say(string)

@bot.command()
async def eightball():
	rand = random.randint(1, 6)
	if rand == 1:
		string = "certain"

	elif rand == 2:
		string = "likely"

	elif rand == 3:
		string = "somewhat possible"

	elif rand == 4:
		string = "unlikely"

	elif rand == 5:
		string = "highly unlikely"

	elif rand == 6:
		string = "uncertain"

	await bot.say(f"The 8ball says that your outcome is '{string}'.")

@bot.command()
async def oofdab():
	await bot.say(":Oof_dab:")

@bot.event 
async def on_ready():
    print(f"> {bot.user.name} loading...")
    print("> Token loading...")
    print("> Script loaded in successfully.")
    print(f"> Bot name: {bot.user.name}")
    print(f"> Bot ID: {bot.user.id}")

bot.run(token) 
