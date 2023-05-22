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
WELCOME_CHANNEL = os.getenv('DISCORD_WELCOME_CHANNEL')
GENERAL_ROLE = os.getenv('DISCORD_GENERAL_ROLE')
MUTE_ROLE = os.getenv('DISCORD_MUTE_ROLE')


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


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name} yo'
    )

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(int(WELC_CHANNEL))
    print(f"{member} join us")
    await welcome_channel.send(f"Hello, {member.mention}, welcome")
    role_name = "Club member"  # Your role's name, in my case it's 'Club member'
    role = discord.utils.get(member.guild.roles, name=role_name)
    await member.add_roles(role)
    print(f"add role {member}")

@bot.event
async def on_member_remove(member):
    print(f'{member} left us')
    leave_channel = bot.get_channel(int(WELC_CHANNEL))
    await leave_channel.send(f'{member.mention} bb!')

@bot.command()
async def all_role(ctx):
    guild = ctx.guild
    role = guild.get_role(int(GENERAL_ROLE))
    for m in guild.members:
        await m.add_roles(role)
        await asyncio.sleep(2)

@bot.command()
async def avatar(ctx, member: discord.Member  = None):
    if member == None:#if you don't mention the participant then the avatar of the author of the post is displayed
        member = ctx.author
    embed = discord.Embed(color = 0x8B0000, title = f"Member's avatar - {member.name}", description = f"[Click to download the avatar]({member.avatar})")
    embed.set_image(url = member.avatar)
    await ctx.send(embed = embed)
    
    
@bot.command()
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member):
    muteRole = ctx.guild.get_role(int(MUTE_ROLE))
    for i in member.roles:
        try:
            await member.remove_roles(i)
        except:
            print(f"Can't remove the role {i}")
    await member.add_roles(muteRole)
    await ctx.channel.purge(limit=1)
    await ctx.send(str(member) + ' has been muted!')



bot.run(TOKEN)
