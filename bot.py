import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import asyncio
import time


intents = discord.Intents.default()
intents.members = True  
intents.presences = True

client = commands.Bot(command_prefix=("./"), help_command=None, intents=intents)
load_dotenv()

greetings = [
    "Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
    "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
    "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"
]

predictions = [
    "Yeah, sure.", "What about no?", "Yes, totally.", "Are you kidding me? Of course, no!", "Of course!",
    "I guess, no.", "Probably yes." , "Nah. Not at all.", "Obviously, yes!"
]

death_scenarios = [
    "A snake bit you.", "You met a vampire and he sucked all your blood.", \
    "You drank a glass of juice, but there was poison inside.", \
    "You were thrown out into space by a giant gorilla.", "You ate too many mushrooms.", \
    "A heavy hammer fell onto your head.", "A zombie strangled you to death.", \
    "A maniac cut your throat while you were sleeping.", "You became too old.", \
    "You decided that you had to eat 20 bags of chips.", \
    "You wanted to take a vacation in Chernobyl.", \
    "Voldemort came to you and said \'Avada Kedavra!\'", \
    "You were trying to install Arch Linux, but failed."
]


subreddits = [
    "linuxmemes", \
    "dankmemes", \
    "memes", \
    "cleanmemes", \
    "wholesomememes", \
    "progammerhumor" \
]


distro_list = [
    "Arch BTW", \
    "Ubuntu", \
    "Gentoo", \
    "Debian", \
    "Endeavour OS", \
    "Zorin OS", \
    "Pop_OS!", \
    "Fedora", \
    "Cent OS", \
    "Manjaro", \
    "OpenSUSE", \
    "Kali", \
    "Artix", \
    "Knoppix", \
    "Alpine", \
    "Hyperbola", \
    "Parabola", \
    "Qubes OS", \
    "Void Linux", \
    "Elementary OS", \
    "Slackware", \
    "RHEL", \
    "gNewSense", \
    "MX Linux", \
    "Parrot", \
]
bsd_distros = [
    "FreeBSD", \
    "OpenBSD", \
    "DragonflyBSD", \
    "GhostBSD", \
    "NetBSD", \
    "PC-BSD" \
]

sort_mode = [
    "top", \
    "hot", \
    "controversial", \
    "new" \
]

ubuntu_versions = [
    "Ubuntu 4.10 (Warty Warthog)", \
    "Ubuntu 5.04 (Hoary Hedgehog)", \
	"Ubuntu 5.10 (Breezy Badger)", \
    "Ubuntu 6.06 LTS (Dapper Drake)", \
	"Ubuntu 6.10 (Edgy Eft)", \
	"Ubuntu 7.04 (Feisty Fawn)", \
	"Ubuntu 7.10 (Gutsy Gibbon)", \
	"Ubuntu 8.04 LTS (Hardy Heron)", \
	"Ubuntu 8.10 (Intrepid Ibex)", \
	"Ubuntu 9.04 (Jaunty Jackalope)", \
	"Ubuntu 9.10 (Karmic Koala)",  \
	"Ubuntu 10.04 LTS (Lucid Lynx)",  \
	"Ubuntu 10.10 (Maverick Meerkat)",  \
	"Ubuntu 11.04 (Natty Narwhal)",  \
	"Ubuntu 11.10 (Oneiric Ocelot)",  \
	"Ubuntu 12.04 LTS (Precise Pangolin)",  \
	"Ubuntu 12.10 (Quantal Quetzal)",  \
	"Ubuntu 13.04 (Raring Ringtail)",  \
	"Ubuntu 13.10 (Saucy Salamander)",  \
	"Ubuntu 14.04 LTS (Trusty Tahr)",  \
	"Ubuntu 14.10 (Utopic Unicorn)",  \
	"Ubuntu 15.04 (Vivid Vervet)",  \
	"Ubuntu 15.10 (Wily Werewolf)",  \
	"Ubuntu 16.04 LTS (Xenial Xerus)",  \
	"Ubuntu 16.10 (Yakkety Yak)",  \
	"Ubuntu 17.04 (Zesty Zapus)",  \
	"Ubuntu 17.10 (Artful Aardvark)",  \
	"Ubuntu 18.04 LTS (Bionic Beaver)",  \
	"Ubuntu 18.10 (Cosmic Cuttlefish)",  \
	"Ubuntu 19.04 (Disco Dingo)",  \
	"Ubuntu 19.10 (Eoan Ermine)",  \
	"Ubuntu 20.04 LTS (Focal Fossa)",  \
	"Ubuntu 20.10 (Groovy Gorilla)",  \
    "Ubuntu 21.04 (Hirsute H...)"
]

vowels = ["a","e","i","o","u","y"]

consonants = [
    "b","c","d","f","g","h","j","k","l","m", \
    "n","p","q","r","s","t","v","w","x","z"
]

@client.event
async def on_connect():
    print("Connecting to Discord.....")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type \'./help\' for the commands. On {len(client.guilds)} servers"))
    print("Gardenbot has connected to Discord")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Client-side ping took {round(client.latency * 1000)}ms')

@client.command()
async def about(ctx):
    await ctx.send(f'Gardenbot is a Discord by me is me forked from PurpleBot (<https://github.com/PurpleSci/PurpleBot>).')

@client.command()
async def license(ctx):
    await ctx.send(f'Gardenbot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot. This is not the full license, it is just summarized. Please read the full license here: https://raw.githubusercontent.com/meisme-dev/Gardenbot/master/LICENSE')

@client.command()
async def github(ctx):
    await ctx.send(f'Gardenbot\'s source code is avalaible on GitHub: <https://github.com/meisme-dev/Gardenbot>')

@client.command()
async def invite(ctx):
    await ctx.send(f'If you want to add Gardeonbot to your server, use this link: <https://discord.com/api/oauth2/authorize?client_id=769606923091181569&permissions=8&scope=bot>')

@client.command()
async def distro(ctx):
    await ctx.send(random.choice(distro_list))
    
@client.command(pass_context = True)
async def dm(ctx,*,arg):
    await ctx.message.author.send(arg)

@client.command(pass_context = True)
async def reminder(ctx,specifiedtime,*,arg):
        specifiedtimeseconds = int(specifiedtime) * 60
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Reminder set to {arg}, sending in {int(specifiedtime)} minutes!")
        await asyncio.sleep(specifiedtimeseconds)
        await ctx.message.author.send(arg)

@client.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@client.command()
async def randnum(ctx):
    await ctx.send(random.randint(0, 10000))

@client.command()
async def respond(ctx):
    await ctx.send(random.choice(predictions))

@client.command()
async def die(ctx):
    await ctx.send(random.choice(death_scenarios))

@client.command()
async def pogchamp(ctx):
    await ctx.send('''
░░░░░▒░░▄██▄░▒░░░░░░
░░░▄██████████▄▒▒░░░
░▒▄████████████▓▓▒░░
▓███▓▓█████▀▀████▒░░
▄███████▀▀▒░░░░▀█▒░░
████████▄░░░░░░░▀▄░░
▀██████▀░░▄▀▀▄░░▄█▒░
░█████▀░░░░▄▄░░▒▄▀░░
░█▒▒██░░░░▀▄█░░▒▄█░░
░█░▓▒█▄░░░░░░░░░▒▓░░
░▀▄░░▀▀░▒░░░░░▄▄░▒░░
░░█▒▒▒▒▒▒▒▒▒░░░░▒░░░
░░░▓▒▒▒▒▒░▒▒▄██▀░░░░
░░░░▓▒▒▒░▒▒░▓▀▀▒░░░░
░░░░░▓▓▒▒░▒░░▓▓░░░░░
░░░░░░░▒▒▒▒▒▒▒░░░░░░
''')

@client.command()
async def ubuntu(ctx):
    await ctx.send(random.choice(ubuntu_versions))

@client.command()
async def groovy(ctx):
    await ctx.send(f'https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_500,h_776/https://assets.ubuntu.com/v1/fe951eda-20.10_Groovy+Gorilla_RPi_Sketch.svg')

@client.command()
async def pi(ctx):
    await ctx.send(f'Here is π calculated to the first 1000000 digits: http://newton.ex.ac.uk/research/qsystems/collabs/pi/pi6.txt')

@client.command()
async def ptable(ctx):
    await ctx.send(f'Ptable is an interactive online version of the Periodic Table of Elements: https://ptable.com/')

@client.command()
async def bsd(ctx):
    await ctx.send(random.choice(bsd_distros))

@client.command(pass_context=True)
async def meme(ctx): 
    async with ctx.typing():
        asyncio.sleep(3)
    memesubreddits = random.choice(subreddits)
    sortedmode = random.choice(sort_mode)
    async with aiohttp.ClientSession() as cs:
        async with cs.get(F'https://www.reddit.com/r/{memesubreddits}/new.json?sort={sortedmode}') as r:
            res = await r.json()
            randomint = random.randint(0, 25)
            if not (res['data']['children'][randomint]['data']['over_18']):
                if not (res['data']['children'][randomint]['data']['is_video']):
                    embedLink = res['data']['children'] [randomint]['data']['permalink']
                    embedTitle = res['data']['children'] [randomint]['data']['title']
                    embedFooterUp = res['data']['children'] [randomint]['data']['ups']
                    embedFooterDown = res['data']['children'] [randomint]['data']['downs']
                    embedFooterComments = res['data']['children'] [randomint]['data']['num_comments']
                    embed = discord.Embed(title=f"From r/{memesubreddits}", description=F"[{embedTitle}](https://reddit.com{embedLink})", color=random.randint(0, 0xffffff))
                    embed.set_image(url=res['data']['children'] [randomint]['data']['url'])
                    embed.set_footer(text=F"👍{embedFooterUp}  👎{embedFooterDown}  💬{embedFooterComments}")
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("👍")
                    await message.add_reaction("👎")
                else:
                    await meme(ctx)
            else:
                print("Blocked NSFW")
                await meme(ctx)

@meme.error
async def meme_error(ctx,error):
    if isinstance(error, commands.CommandInvokeError):
        async with ctx.typing():
            asyncio.sleep(3)
        memesubreddits = random.choice(subreddits)
        sortedmode = random.choice(sort_mode)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(F'https://www.reddit.com/r/{memesubreddits}/new.json?sort={sortedmode}') as r:
                res = await r.json()
                randomint = random.randint(0, 25)
                if not (res['data']['children'][randomint]['data']['over_18']):
                    if not (res['data']['children'][randomint]['data']['is_video']):
                        embedLink = res['data']['children'] [randomint]['data']['permalink']
                        embedTitle = res['data']['children'] [randomint]['data']['title']
                        embedFooterUp = res['data']['children'] [randomint]['data']['ups']
                        embedFooterDown = res['data']['children'] [randomint]['data']['downs']
                        embedFooterComments = res['data']['children'] [randomint]['data']['num_comments']
                        embed = discord.Embed(title=f"From r/{memesubreddits}", description=F"[{embedTitle}](https://reddit.com{embedLink})", color=random.randint(0, 0xffffff))
                        embed.set_image(url=res['data']['children'] [randomint]['data']['url'])
                        embed.set_footer(text=F"👍{embedFooterUp}  👎{embedFooterDown}  💬{embedFooterComments}")
                        message = await ctx.send(embed=embed)
                        await message.add_reaction("👍")
                        await message.add_reaction("👎")



@client.command(pass_context = True)
async def uinfo(ctx,member: discord.Member):
    if member.guild_permissions.administrator:
        admin = "Yes"
    else:
        admin = "No"
    if member.bot:
        bot = "Yes"
    else:
        bot = "No"
    if member.status == discord.Status.online:
        status = "Online"
    elif member.status == discord.Status.offline:
        status = "Offline"
    else:
        status = "Do not disturb"
    roles = member.roles
    roles.reverse() 
    top_role = roles[0]
    created = member.created_at
    joined = member.joined_at
    embed=discord.Embed(title=f"{member}")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.add_field(name="Account created", value=f"{created.strftime('%Y-%m-%d')}", inline=True)
    embed.add_field(name="Nickname", value=f"{member.mention}", inline=True)
    embed.add_field(name="ID", value=f"{member.id}", inline=True)
    embed.add_field(name="Joined server at", value=f'{joined.strftime("%Y-%m-%d")}', inline=True)
    embed.add_field(name="Admin",value=f'{admin}', inline=True)
    embed.add_field(name="Bot",value=f'{bot}', inline=True)
    embed.add_field(name=f'Roles', value=f'{len(roles)}', inline=True)
    embed.add_field(name=f'Top role', value=f'{top_role.mention}', inline=True)
    embed.add_field(name=f'Status', value=status, inline=True)
    await ctx.send(embed=embed)

@uinfo.error
async def userinfo_error(ctx,error):
    if ctx.message.author.guild_permissions.administrator:
        admin = "Yes"
    else:
        admin = "No"
    if ctx.message.author.bot:
        bot = "Yes"
    else:
        bot = "No"
    if ctx.message.author.status == discord.Status.online:
        status = "Online"
    elif ctx.message.author.status == discord.Status.offline:
        status = "Offline"
    else:
        status = "Do not disturb"
    roles = ctx.message.author.roles
    roles.reverse() 
    top_role = roles[0]
    created = ctx.message.author.created_at
    joined = ctx.message.author.joined_at
    embed=discord.Embed(title=f"{ctx.message.author}")
    embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
    embed.add_field(name="Account created", value=f"{created.strftime('%Y-%m-%d')}", inline=True)
    embed.add_field(name="Nickname", value=f"{ctx.message.author.mention}", inline=True)
    embed.add_field(name="ID", value=f"{ctx.message.author.id}", inline=True)
    embed.add_field(name="Joined server at", value=f'{joined.strftime("%Y-%m-%d")}', inline=True)
    embed.add_field(name="Admin",value=f'{admin}', inline=True)
    embed.add_field(name="Bot",value=f'{bot}', inline=True)
    embed.add_field(name=f'Roles', value=f'{len(roles)}', inline=True)
    embed.add_field(name=f'Top role', value=f'{top_role.mention}', inline=True)
    embed.add_field(name=f'Status', value=f'{status}', inline=True)
    await ctx.send(embed=embed)

@client.command()
async def rubbish(ctx):
    sentence = ""
    for i in range(random.randrange(3,7)):
        word = str()
        for j in range(random.randrange(1,5)):
            word = word + random.choice(consonants) + random.choice(vowels)
        sentence = sentence + word + " "
    await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))

@client.command()
async def echo(ctx,*,arg):
    await ctx.channel.purge(limit=1)
    if(arg != "@everyone"):
        if (arg != "@here"):
            await ctx.send(f"{arg}")
        else: 
            await ctx.send("You are not permitted to ping @ here. Continuing will result in a punishement.")
    else:
        await ctx.send("You are not permitted to ping @ everyone. Continuing will result in a punishement.")

@client.command()
async def google(ctx,*,arg):
    Urlified = arg.replace(" ", "%20")
    embed = discord.Embed(title=f"Search Results", description=F"[{arg}](https://google.com/search?q={Urlified})", color=random.randint(0, 0xffffff))
    await ctx.send(embed=embed)

@client.command()
async def reddit(ctx,arg):
    async with aiohttp.ClientSession() as cs:
        sortedmode = random.choice(sort_mode)
        async with cs.get(F'https://www.reddit.com/r/{arg}/new.json?sort={sortedmode}') as r:
            res = await r.json()
            randomint = random.randint(0, 25)
            if not (res['data']['children'][randomint]['data']['over_18']):
                if not (res['data']['children'][randomint]['data']['is_video']):
                    embedLink = res['data']['children'] [randomint]['data']['permalink']
                    embedTitle = res['data']['children'] [randomint]['data']['title']
                    embedFooterUp = res['data']['children'] [randomint]['data']['ups']
                    embedFooterDown = res['data']['children'] [randomint]['data']['downs']
                    embedFooterComments = res['data']['children'] [randomint]['data']['num_comments']
                    embed = discord.Embed(title=f"From r/{arg}", description=F"[{embedTitle}](https://reddit.com{embedLink})")
                    embed.set_image(url=res['data']['children'] [randomint]['data']['url'])
                    embed.set_footer(text=F"👍{embedFooterUp}  👎{embedFooterDown}  💬{embedFooterComments}")
                    message = await ctx.send(embed=embed)
                    await message.add_reaction("👍")
                    await message.add_reaction("👎")

                else:
                   await reddit(ctx,arg) 
            else:
                await reddit(ctx,arg)
                print("Blocked NSFW")


@client.command()
async def help(ctx,arg):
    author = ctx.message.author
    await author.create_dm()
    if arg == "moderation":
        embedVar = discord.Embed(title="Moderation Commands", description="Shows a list of commands for moderators \n \u200B", color=0x3388FF)
        embedVar.add_field(name="`Kick`", value="Kicks a member. \nUsage: ./kick <@member> \n \u200B", inline=True)
        embedVar.add_field(name="`Mute`", value="Mutes a member. \nUsage: ./mute <@member> \n \u200B", inline=True)
        embedVar.add_field(name="`Ban`", value="Bans a member. \nUsage: ./ban <@member>\n \u200B", inline=True)
    if arg == "fun":
        embedVar = discord.Embed(title="Fun Commands", description="Shows a list of commands for fun stuff \n \u200B", color=0x3388FF)
        embedVar.add_field(name="`Hello`", value="Greets you! \nUsage: ./hello \n \u200B", inline=True)
        embedVar.add_field(name="`Distro`", value="Sends a random distro. \nUsage: ./distro \n \u200B", inline=True)
        embedVar.add_field(name="`BSD`", value="Sends a BSD distro. \nUsage: ./bsd \n \u200B", inline=True)
        embedVar.add_field(name="`Echo`", value="Repeats the specified message. \nUsage: ./echo message\n \u200B", inline=True)
        embedVar.add_field(name="`Randnum`", value="Sends a random number between 0 and 10000. \nUsage: ./randnum\n \u200B", inline=True)
        embedVar.add_field(name="`Respond`", value="Sends a random response, similar to \"8ball\". \nUsage: ./respond\n \u200B", inline=True)
        embedVar.add_field(name="`Die`", value="Sends a random death scenario. \nUsage: ./die\n \u200B", inline=True)
        embedVar.add_field(name="`Meme`", value="Sends a random meme from popular subreddits. \nUsage: ./meme\n \u200B", inline=True)
        embedVar.add_field(name="`Ubuntu`", value="Sends a random Ubuntu version. \nUsage: ./ubuntu\n \u200B", inline=True)
        embedVar.add_field(name="`Rubbish`", value="Generates random pronounciable nonsense. \nUsage: ./rubbish\n \u200B", inline=True)
        embedVar.add_field(name="`DM`", value="DMs you with a message. \nUsage: ./dm <message>\n \u200B", inline=True)
        embedVar.add_field(name="`Reddit`", value="Fetches a post from the specified Subreddit. \nUsage: ./reddit <subreddit>\n \u200B", inline=True)
    if arg == "utility":
        embedVar = discord.Embed(title="Utility Commands", description="Shows a list of commands for utility \n \u200B", color=0x3388FF)
        embedVar.add_field(name="`Help`", value="Displays the help message. \nUsage: ./help [category]\n \u200B", inline=True)
        embedVar.add_field(name="`Ping`", value="Sends the bot latency in ms. \nUsage: ./ping \n \u200B", inline=True)
        embedVar.add_field(name="`About`", value="Displays information about the bot. \nUsage: ./about \n \u200B", inline=True)
        embedVar.add_field(name="`License`", value="Displays the bot license. \nUsage: ./license \n \u200B", inline=True)
        embedVar.add_field(name="`GitHub`", value="Sends the source code link. \nUsage: ./github \n \u200B", inline=True)
        embedVar.add_field(name="`Invite`", value="Sends the bot invite link. \nUsage: ./invite \n \u200B", inline=True)
        embedVar.add_field(name="`Pi`", value="Displays a link to 1 000 000 digits of pi. \nUsage: ./pi \n \u200B", inline=True)
        embedVar.add_field(name="`Ptable`", value="Displays a link to an interactive Periodic Table. \nUsage: ./ptable\n \u200B", inline=True)        
        embedVar.add_field(name="`Reminder`", value="Sets a reminder. \nUsage: ./reminder <minutes> <message>\n \u200B", inline=True)


    await ctx.send(embed=embedVar)



@help.error
async def help_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedVar = discord.Embed(title="Help", description="Shows a list of commands \n \u200B", color=0x3388FF)
        embedVar.add_field(name="Utility", value="`Shows a list of utility commands! \nUsage: ./help utility` \n \u200B", inline=False)
        embedVar.add_field(name="Fun", value="`Shows a list of commands for fun stuff! \nUsage: ./help fun` \n \u200B", inline=False)
        embedVar.add_field(name="Moderation", value="`Shows a list of commands for moderators! \nUsage: ./help moderation`", inline=False)
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
