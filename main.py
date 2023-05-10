# This example requires the 'message_content' intent.

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WELC_CHANNEL = os.getenv('WELCOME_CHANNEL')


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')


# @bot.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'{member.name} yo'
#     )

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(int(WELC_CHANNEL))
    print(f"{member} join us")
    await welcome_channel.send(f"Hello, {member.mention}, welcome")
    role_name = "Member"  # Your role's name, in my case it's 'Member'
    role = discord.utils.get(member.guild.roles, name=role_name)
    await member.add_roles(role)
    print(f"add role {member}")

@bot.event
async def on_member_remove(member):
    print(f'{member} left us')
    leave_channel = bot.get_channel(int(WELC_CHANNEL))
    await leave_channel.send(f'{member.mention} bb!')


bot.run(TOKEN)
