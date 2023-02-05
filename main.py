import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    await client.tree.sync()
    print('ready!', random.uniform(0, 100))

@client.tree.command(name="rand1-2", description="1 to 2")
async def hello(ctx: discord.Interaction):
    rand = random.uniform(0, 10)
    await ctx.response.send_message(int(rand))

@client.tree.command(name="rand1-10", description="1 to 10")
async def hello(ctx: discord.Interaction):
    rand = random.uniform(0, 10)
    await ctx.response.send_message(int(rand))

@client.tree.command(name="rand1-50", description="1 to 50")
async def hello(ctx: discord.Interaction):
    rand = random.uniform(0, 10)
    await ctx.response.send_message(int(rand))

@client.tree.command(name="rand1-100", description="1 to 100")
async def hello(ctx: discord.Interaction):
    rand = random.uniform(0, 100)
    await ctx.response.send_message(int(rand))

client.run(TOKEN)
