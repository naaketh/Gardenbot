import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

# Optional- Load data from config.json instead of dotenv EXCEPT TOKEN

client = commands.Bot(command_prefix="./", help_command=None)
load_dotenv()

@client.event
async def on_connect():
    print("Connecting to Discord.....")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type \'./help\' for the commands. On {len(client.guilds)} servers"))
    print("Gardenbot has connected to Discord")

@client.command()
async def help(ctx,arg):
    author = ctx.message.author
    await author.create_dm()
    if arg == "moderation":
        embedVar = discord.Embed(title="Moderation Commands", description="Shows a list of commands for moderators \n \u200B", color=0x3388FF)
        embedVar.add_field(name="Kick", value="```Kicks a member. Usage: ./kick @member``` \n \u200B", inline=True)
        embedVar.add_field(name="Mute", value="```Mutes a member. Usage: ./mute @member``` \n \u200B", inline=True)
        embedVar.add_field(name="Ban", value="```Bans a member. Usage: ./ban @member``` \n \u200B", inline=True)
   
    await ctx.send(embed=embedVar)

@help.error
async def help_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedVar = discord.Embed(title="Help", description="Shows a list of commands \n \u200B", color=0x3388FF)
        embedVar.add_field(name="Utility", value="```help \nping about \nlicense github \ninvite pi \nptable``` \n \u200B", inline=True)
        embedVar.add_field(name="Fun", value="```hello distro \nrandnum predict \ndie boo \npogchamp ubuntu \ngroovy rubbish``` \n \u200B", inline=True)
        embedVar.add_field(name="Moderation", value="```ban \nmute \nkick \npurge  \nMore coming soon!```", inline=True)
        await ctx.send(embed=embedVar)

@client.event
async def on_disconnect():
    print("GardenBot disconnected.")


# Let's make the Discord.py module understand that there is a folder for additional commands (cogs).

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
