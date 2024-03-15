import os
import random


#importing riotApi functions
import sys
sys.path.insert(0,'./commands')
import riot


import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)




@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



#bot command that replies pong to the command
#example input: !ping
#output: pong
@bot.command(name='ping', help='RESPONDS WITH PONG')
async def ping_me(ctx):
    response = 'pong'
    await ctx.send(response)



#bot command that rolls dice. Uses converters.
#example input: !roll 1 6
#will output a random number between 1 and 6
@bot.command(name='roll', help='Simulates dice')
async def roll(ctx, diceNumber:int, sideNumber:int):
    dice = [
        str(random.choice(range(1,sideNumber + 1)))
        for _ in range (diceNumber)
    ]
    await ctx.send(', '.join(dice))



#command that creates a text channel, must have role Virgin to create
#example input: !create-channel VirginChannel
#output: new channel created
@bot.command(name='create-channel')
@commands.has_role('Virgin')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.command(name='showLevel')
async def showLevel(ctx, riotId:str, region:str = "EUW"):
   level = riot.showOffLevel(riotId, region)
   if level > 500:
       await ctx.send(f'Behold! An account level **{level}**! TOUCH SOME GRASS')
   else: await ctx.send(f' Account is level **{level}**')

@bot.command(name='showId')
async def showId(ctx, riotId:str, region:str = "EUW"):
    id = riot.showID(riotId, region)
    await ctx.send(f'Your id is: {id}.\n Dont show it to anyone pls')


@bot.command(name='lastMatch')
async def showMatch(ctx, riotId:str, region:str = "EUW"):
    await ctx.send(riot.getMatch(riotId, region))

@bot.command(name='hiddenStats')
async def hidden(ctx, riotId:str, region:str = "EUW"):
    await ctx.send(riot.hiddenStats(riotId, region))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)

