import discord
from discord.ext import commands
import json

with open('setting.json','r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   join_channel = bot.get_channel(int(jdata['新進人員']))
   await join_channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
   leave_channel = bot.get_channel(int(jdata['離開人員']))
   await leave_channel.send(f'{member} leave!')       

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

bot.run(jdata['BOT_TOKEN'])    