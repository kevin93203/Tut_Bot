import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   join_channel = bot.get_channel(625620743454982144)
   await join_channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
   leave_channel = bot.get_channel(625620781350518805)
   await leave_channel.send(f'{member} leave!')       

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

bot.run('NjI1NTQ1NTQ4MTg2OTEwNzMw.XYiBBw.SZnszqkZtt8lN1Z5RDl2QHJhk2A')    