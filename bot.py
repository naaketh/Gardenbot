# MIT License

# Copyright (c) 2020 me is me

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#Define dependencies of the bot and import them
import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import asyncio 
import mysql.connector
import requests
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand
from discord_slash.model import SlashContext


#Set the intents for the uinfo command
intents = discord.Intents.all()
intents.members = True  
intents.presences = True

#Load the bot
client = commands.Bot(command_prefix=("/"), help_command=None, intents=discord.Intents.all())
load_dotenv()
slash = SlashCommand(client)


api_key=os.getenv('API_KEY')

#Define the lists for commands to use 
greetings = [
    "Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!", "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!", "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"
]

predictions = [
    "Yeah, sure.", "What about no?", "Yes, totally.", "Are you kidding me? Of course, no!", "Of course!", "I guess, no.", "Probably yes." , "Nah. Not at all.", "Obviously, yes!", "Ha! yeah... no.", "Maybe..."
]

subreddits = [
    "dankmemes", "memes", "cleanmemes", "wholesomememes"
]

distro_list = [
    "Arch BTW", "Ubuntu", "Gentoo", "Debian", "Endeavour OS", "Zorin OS", "Pop_OS!", "Fedora", "Cent OS", "Manjaro", "OpenSUSE", "Kali", "Artix", "Knoppix", "Alpine", "Hyperbola", "Parabola", "Qubes OS", "Void Linux", "Elementary OS", "Slackware", "RHEL", "gNewSense", "MX Linux", "Parrot", "Bodhi Linux" 
]
bsd_distros = [
    "FreeBSD", "OpenBSD", "DragonflyBSD", "GhostBSD", "NetBSD", "PC-BSD" 
]

sort_mode = [
    "top", "hot", "controversial", "new" 
]

vowels = [
    "a", "e", "i", "o", "u", "y"
]

consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"
]


#Print the bot status to the console output.
@client.event
async def on_connect():
    print("Connecting to Discord.....")




@client.event
async def on_ready():
    print("Gardenbot has connected to Discord")       
    for guild in client.guilds:
        print(guild.name)

    #Get the number of members from the guilds the bot is in, to later display in the status.
    ActiveServers = client.guilds
    sum = 0
    for s in ActiveServers:
        sum += len(s.members)

    #Start a while loop to change the bot status every five seconds.
    while True:
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("/help for more info."))
            await asyncio.sleep(5)
            #"len(client.guilds)" gets the number of servers the bot is in.
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers."))
            await asyncio.sleep(5)
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("https://discord.gg/TFg9GTc"))
            await asyncio.sleep(5)
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Linux"))
            await asyncio.sleep(5)
            #Display the sum of members in every server the bot is in, which we defined earlier.
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{sum} members."))
            await asyncio.sleep(5)

#Start defining the commands

# @client.listen('on_message')
# async def on_message(message):


@client.command()
async def ping(ctx):
    PingEmbed = discord.Embed(title="Ping", description=f"Pong! Client-side ping took {round(client.latency * 1000)}ms.", color=0x35a64f)
    PingEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=PingEmbed)

@client.command()
async def about(ctx):
    AboutEmbed = discord.Embed(title="About", description="Gardenbot is a Discord bot by <@536303380088356904>. It was started as a bot for a Linux community, which you can find [here](https://discord.gg/TFg9GTc)!", color=0x35a64f)
    await ctx.send(embed=AboutEmbed)

@client.command()
async def license(ctx):
    LicenseEmbed = discord.Embed(title="License", description="Gardenbot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot.", color=0x35a64f)
    LicenseEmbed.add_field(name="\u200b", value="**DISCLAIMER**: this is not the full license, and this is not legal advice. Please read the full license [here](https://raw.githubusercontent.com/meisme-dev/Gardenbot/master/LICENSE).")
    LicenseEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=LicenseEmbed)

@slash.slash(name="blep", guild_ids=[765557872682729472])
async def _test(ctx: SlashContext, arg):
    await ctx.send(content="e")


@client.command()
async def github(ctx):
    GithubEmbed = discord.Embed(title="Source code", description="Gardenbot\'s source code is available [here](https://github.com/meisme-dev/Gardenbot).", color=0x35a64f)
    GithubEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=GithubEmbed)

@client.command()
async def invite(ctx):
    InviteEmbed = discord.Embed(title="Invite", description="If you want to add Gardenbot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=769606923091181569&permissions=8&scope=bot).", color=0x35a64f)
    await ctx.send(embed=InviteEmbed)

@client.command()
async def distro(ctx):
    DistroEmbed = discord.Embed(title="Distro", description=f"{random.choice(distro_list)}", color=0x35a64f)
    DistroEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=DistroEmbed)

@client.command(pass_context = True)
async def dm(ctx,*,arg):
    await ctx.message.author.send(arg)

@client.command(aliases=['suggestion','request'])
async def suggest(ctx,*,arg):
    SuggestEmbed = discord.Embed(title="Suggestion", description=f"{arg}", color=0x35a64f)
    SuggestEmbed.set_footer(text=f"Requested by {ctx.message.author}  ●  At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    channel = client.get_channel(783385724158083102)
    msg = await channel.send(embed=SuggestEmbed)
    await msg.add_reaction("✔️")
    await msg.add_reaction("❌")
    await ctx.message.add_reaction("✅")


@client.command()
async def poll(ctx,*,arg):
    PollEmbed = discord.Embed(title="Poll", description=f"{arg}", color=0x35a64f)
    PollEmbed.set_footer(text=f"{ctx.message.created_at.strftime(f'Requested by {ctx.message.author}  ●  At %Y/%m/%d - %I:%M %p GMT')}")
    msg = await ctx.send(embed=PollEmbed)
    await ctx.message.delete()
    await msg.add_reaction("✔️")
    await msg.add_reaction("❌")
    await ctx.message.add_reaction("✅")

@client.command(pass_context = True)
async def reminder(ctx,specifiedtime,*,arg):
    if specifiedtime.endswith("s"):
        multiplier = 1
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            timedisplay = "seconds"
        else:
            timedisplay = "second"
    elif specifiedtime.endswith("m"):
        multiplier = 60
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            timedisplay = "minutes"
        else:
            timedisplay = "minutes"
    elif specifiedtime.endswith("h"):
        multiplier = 3600
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            timedisplay = "hours"
        else:
            timedisplay = "hour"
    elif specifiedtime.endswith("d"):
        multiplier = 86400
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            timedisplay = "days"
        else:
            timedisplay = "day"
    elif specifiedtime.isnumeric():
        specifiedtime = int(specifiedtime)
        multiplier = 60
        if specifiedtime != 1:
            timedisplay = "minutes"
        else:
            timedisplay = "minute"
    else:
       ReminderEmbed = discord.Embed(title="Error!", description="Please enter a valid ending. Example: 1s, 1m, 1h, 1d, or 1.", color=0xff0000)
       ReminderEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
       await ctx.send(embed=ReminderEmbed) 
       await ctx.message.delete()

    specifiedtimeseconds = int(specifiedtime) * int(multiplier)
    await ctx.message.delete()
    ReminderEmbed = discord.Embed(title="Reminder", description=f"Reminder \"{arg}\" will be sending in {specifiedtime} {timedisplay}.", color=0x35a64f)
    ReminderEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=ReminderEmbed)
    await asyncio.sleep(specifiedtimeseconds)
    await ctx.message.author.send(arg)

@client.command()
async def hello(ctx):
    HelloEmbed = discord.Embed(title="Hello", description=f"{random.choice(greetings)}", color=0x35a64f)
    HelloEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=HelloEmbed)

@client.command()
async def randnum(ctx):
    RandnumEmbed = discord.Embed(title="Random number", description=f"{random.randint(0, 10000)}", color=0x35a64f)
    RandnumEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=RandnumEmbed)

@client.command()
async def respond(ctx):
    RespondEmbed = discord.Embed(title="Prediction", description=f"{random.choice(predictions)}", color=0x35a64f)
    RespondEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=RespondEmbed)

@client.command()
async def interject(ctx):
    InterjectEmbed = discord.Embed(title="Interjection", description="I\'d just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX. Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called “Linux”, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project. There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine’s resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called “Linux” distributions are really distributions of GNU/Linux.", color=0x35a64f)
    InterjectEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=InterjectEmbed)

@client.command()
async def bsd(ctx):
    BsdEmbed = discord.Embed(title="BSD distro", description=f"{random.choice(bsd_distros)}", color=0x35a64f)
    BsdEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=BsdEmbed)

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
                    MemeEmbed = discord.Embed(title=f"From r/{memesubreddits}", description=F"[{embedTitle}](https://reddit.com{embedLink})", color=random.randint(0, 0xffffff))
                    MemeEmbed.set_image(url=res['data']['children'] [randomint]['data']['url'])
                    MemeEmbed.set_footer(text=F"👍{embedFooterUp}  👎{embedFooterDown}  💬{embedFooterComments} - At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
                    message = await ctx.send(embed=MemeEmbed)
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
                        MemeEmbed = discord.Embed(title=f"From r/{memesubreddits}", description=F"[{embedTitle}](https://reddit.com{embedLink})", color=random.randint(0, 0xffffff))
                        MemeEmbed.set_image(url=res['data']['children'] [randomint]['data']['url'])
                        MemeEmbed.set_footer(text=F"👍{embedFooterUp}  👎{embedFooterDown}  💬{embedFooterComments} - At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
                        message = await ctx.send(embed=MemeEmbed)
                        await message.add_reaction("👍")
                        await message.add_reaction("👎")



@client.command()
async def cowsay(ctx,*,arg):
    CowEmbed = discord.Embed(title="Cowsay", description=f"```< {arg} >\n" + 
        "       \   ^__^ \n" +
        "        \  (oo)\_______\n" +
        "           (__)\       )\/\n" +
         "              ||----w |\n" +
         "              ||     ||  ```", color=0x35a64f)
    CowEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")    
    await ctx.send(embed=CowEmbed)



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
    UinfoEmbed = discord.Embed(title=f"{member}")
    UinfoEmbed.set_thumbnail(url=f"{member.avatar_url}")
    UinfoEmbed.add_field(name="Account created", value=f"{created.strftime('%Y/%m/%d')}", inline=True)
    UinfoEmbed.add_field(name="Nickname", value=f"{member.mention}", inline=True)
    UinfoEmbed.add_field(name="ID", value=f"{member.id}", inline=True)
    UinfoEmbed.add_field(name="Joined server at", value=f'{joined.strftime("%Y/%m/%d")}', inline=True)
    UinfoEmbed.add_field(name="Admin",value=f'{admin}', inline=True)
    UinfoEmbed.add_field(name="Bot",value=f'{bot}', inline=True)
    UinfoEmbed.add_field(name='Roles', value=f'{len(roles)}', inline=True)
    UinfoEmbed.add_field(name='Top role', value=f'{top_role.mention}', inline=True)
    UinfoEmbed.add_field(name='Status', value=status, inline=True)
    UinfoEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=UinfoEmbed)

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
    UinfoEmbed = discord.Embed(title=f"{ctx.message.author}")
    UinfoEmbed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
    UinfoEmbed.add_field(name="Account created", value=f"{created.strftime('%Y/%m/%d')}", inline=True)
    UinfoEmbed.add_field(name="Nickname", value=f"{ctx.message.author.mention}", inline=True)
    UinfoEmbed.add_field(name="ID", value=f"{ctx.message.author.id}", inline=True)
    UinfoEmbed.add_field(name="Joined server at", value=f'{joined.strftime("%Y/%m/%d")}', inline=True)
    UinfoEmbed.add_field(name="Admin",value=f'{admin}', inline=True)
    UinfoEmbed.add_field(name="Bot",value=f'{bot}', inline=True)
    UinfoEmbed.add_field(name='Roles', value=f'{len(roles)}', inline=True)
    UinfoEmbed.add_field(name='Top role', value=f'{top_role.mention}', inline=True)
    UinfoEmbed.add_field(name='Status', value=f'{status}', inline=True)
    UinfoEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=UinfoEmbed)

@client.command()
async def rubbish(ctx):
    sentence = ""
    for i in range(random.randrange(2,9)):
        word = str()
        for j in range(random.randrange(1,5)):
            word = word + random.choice(consonants) + random.choice(vowels)
        sentence = sentence + word + " "
    numgen = sentence.capitalize().rstrip() + random.choice(["!","?",".","..."])
    RubbishEmbed = discord.Embed(title="Rubbish", description=f"{numgen}", color=0x35a64f)
    RubbishEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=RubbishEmbed)

@client.command()
async def echo(ctx,*,arg):
    await ctx.message.delete()
    if not("@here" in arg):
        if not("@everyone" in arg):
            await ctx.send(f"{arg}")
        else:
            embedVar = discord.Embed(title="Error!", description="You are not permitted to ping `@everyone` using the echo command.", color=0xFF0000)
            embedVar.set_footer(text=f"Requested by {ctx.message.author } ●  At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
            await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(title="Error!", description="You are not permitted to ping `@here` using the echo command.", color=0xFF0000)
        embedVar.set_footer(text=f"Requested by {ctx.message.author } ●  At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
        await ctx.send(embed=embedVar)

@client.command()
async def google(ctx,*,arg):
    UrlFormatted = arg.replace(" ", "%20")
    GoogleEmbed = discord.Embed(title="Search Results", description=f"[{arg}](https://google.com/search?q={UrlFormatted})", color=random.randint(0, 0xffffff))
    GoogleEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=GoogleEmbed)

@client.command()
async def reddit(ctx,arg):
    async with aiohttp.ClientSession() as cs:
        sortedmode = random.choice(sort_mode)
        async with cs.get(f'https://www.reddit.com/r/{arg}/new.json?sort={sortedmode}') as r:
            res = await r.json()
            postNum = res['data']['dist']
            randomint = random.randint(0, int(postNum))
            print(randomint)
            print(str(res['data']['children'][randomint]['data']['over_18']))
            if (str(res['data']['children'][randomint]['data']['over_18']) == "False"):
                if not (res['data']['children'][randomint]['data']['is_video']):
                    embedLink = res['data']['children'] [randomint]['data']['permalink']
                    embedTitle = res['data']['children'] [randomint]['data']['title']
                    embedFooterUp = res['data']['children'] [randomint]['data']['ups']
                    embedFooterDown = res['data']['children'] [randomint]['data']['downs']
                    embedFooterComments = res['data']['children'] [randomint]['data']['num_comments']
                    RedditEmbed = discord.Embed(title=f"From r/{arg}", description=F"[{embedTitle}](https://reddit.com{embedLink})")
                    RedditEmbed.set_image(url=res['data']['children'] [randomint]['data']['url'])
                    RedditEmbed.set_footer(text=f"👍{embedFooterUp}  👎{embedFooterDown}  💬{embedFooterComments} - At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
                    message = await ctx.send(embed=RedditEmbed)
                    await message.add_reaction("👍")
                    await message.add_reaction("👎")

                else:
                   await reddit(ctx,arg) 
            else:
                print("Blocked NSFW")

@client.command()
async def package(ctx,arg):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{arg}/new.json?sort={sortedmode}') as r:
            res = await r.json()

@client.command()
async def embed(ctx,*,arg):
     embed = discord.Embed(title="", description=f"{arg}", color=0x35a64f)
     await ctx.message.delete()
     await ctx.send(embed=embed)

@client.command()
async def fun(ctx):
        HelpEmbed = discord.Embed(title="Fun Commands", description="A list of commands for fun stuff to do while you are bored \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="Hello", value="Greets you! \nUsage: `/hello` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Distro", value="Sends a random distro. \nUsage: `/distro` \n \u200B", inline=True)
        HelpEmbed.add_field(name="BSD", value="Sends a BSD distro. \nUsage: `/bsd` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Echo", value="Repeats the specified message. \nUsage: `/echo <message>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Randnum", value="Sends a random number between 0 and 10000. \nUsage: `/randnum`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Respond", value="Sends a random response, similar to \"8ball\". \nUsage: `/respond`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Meme", value="Sends a random meme from popular subreddits. \nUsage: `/meme`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Embed", value="Embeds the specified message. \nUsage: `/embed <message>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Rubbish", value="Generates random pronounciable nonsense. \nUsage: `/rubbish`\n \u200B", inline=True)
        HelpEmbed.add_field(name="DM", value="DMs you with a message. \nUsage: `/dm <message>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Reddit", value="Fetches a post from the specified Subreddit. \nUsage: `/reddit <subreddit>`\n \u200B", inline=True)
        HelpEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
        await ctx.send(embed=HelpEmbed)

@has_permissions(manage_channels=True)
@client.command()
async def slowmode(ctx, specifiedtime):
    if specifiedtime.endswith("s"):
        multiplier = 1
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            slowmode = "seconds"
        else:
            slowmode = "second"
    elif specifiedtime.endswith("m"):
        multiplier = 60
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            slowmode = "minutes"
        else:
            slowmode = "minute"
    elif specifiedtime.endswith("h"):
        multiplier = 3600
        specifiedtime = specifiedtime[:-1]
        specifiedtime = int(specifiedtime)
        if specifiedtime != 1:
            slowmode = "hours"
        else:
            slowmode = "hour"
    elif specifiedtime.isnumeric():
        specifiedtime = int(specifiedtime)
        multiplier = 60
        if specifiedtime != 1:
            slowmode = "seconds"
        else:
            slowmode = "second"
    else:
       SlowmodeEmbed = discord.Embed(title="Error!", description="Please enter a valid ending. Example: 1s, 1m, 1h, 1d, or 1.", color=0xff0000)
    specifiedtimeseconds = int(specifiedtime) * int(multiplier)
    await ctx.channel.edit(slowmode_delay=specifiedtimeseconds)
    await ctx.message.delete()
    SlowmodeEmbed = discord.Embed(title="Slowmode", description=f"Slowmode set to {specifiedtime} {slowmode}.", color=0x35a64f)
    SlowmodeEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=SlowmodeEmbed)



@client.command()
async def utility(ctx):
        HelpEmbed = discord.Embed(title="Utility Commands", description="A list of utility commands to fit any needs \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="Help", value="Displays the help message. \nUsage: `/help [category]`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Ping", value="Sends the bot latency in ms. \nUsage: `/ping` \n \u200B", inline=True)
        HelpEmbed.add_field(name="About", value="Displays information about the bot. \nUsage: `/about` \n \u200B", inline=True)
        HelpEmbed.add_field(name="License", value="Displays the bot license. \nUsage: `/license` \n \u200B", inline=True)
        HelpEmbed.add_field(name="GitHub", value="Sends the source code link. \nUsage: `/github` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Invite", value="Sends the bot invite link. \nUsage: `/invite` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Reminder", value="Sets a reminder. \nUsage: `/reminder <minutes> <message>`\n \u200B", inline=True)
        HelpEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
        await ctx.send(embed=HelpEmbed)


@client.command()
async def moderation(ctx):
        HelpEmbed = discord.Embed(title="Moderation Commands", description="A list of commands for moderators. No memes in #general >:C \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="Kick", value="Kicks a member. \nUsage: `/kick <@member>` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Mute", value="Mutes a member. \nUsage: `/mute <@member>` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Ban", value="Bans a member. \nUsage: `/ban <@member>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Warn", value="Warns a member. \nUsage: `/warn <@member>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Purge", value="Purges a specific number of messages. \nUsage: `/purge <number>`\n \u200B", inline=True)
        HelpEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
        await ctx.send(embed=HelpEmbed)

@client.command()
async def help(ctx,arg):
    author = ctx.message.author
    await author.create_dm()
    if arg == "moderation":
        HelpEmbed = discord.Embed(title="Moderation Commands", description="A list of commands for moderators. No memes in #general >:C \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="Kick", value="Kicks a member. \nUsage: `/kick <@member>` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Mute", value="Mutes a member. \nUsage: `/mute <@member>` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Ban", value="Bans a member. \nUsage: `/ban <@member>`\n \u200B", inline=True)
    if arg == "fun":
        HelpEmbed = discord.Embed(itle="Fun Commands", description="A list of commands for fun stuff to do while you are bored \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="Hello", value="Greets you! \nUsage: `/hello` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Distro", value="Sends a random distro. \nUsage: `/distro` \n \u200B", inline=True)
        HelpEmbed.add_field(name="BSD", value="Sends a BSD distro. \nUsage: `/bsd` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Echo", value="Repeats the specified message. \nUsage: `/echo <message>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Randnum", value="Sends a random number between 0 and 10000. \nUsage: `/randnum`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Respond", value="Sends a random response, similar to \"8ball\". \nUsage: `/respond`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Meme", value="Sends a random meme from popular subreddits. \nUsage: `/meme`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Embed", value="Embeds the specified message. \nUsage: `/embed <message>` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Rubbish", value="Generates random pronounciable nonsense. \nUsage: `/rubbish`\n \u200B", inline=True)
        HelpEmbed.add_field(name="DM", value="DMs you with a message. \nUsage: `/dm <message>`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Reddit", value="Fetches a post from the specified Subreddit. \nUsage: `/reddit <subreddit>`\n \u200B", inline=True)
    if arg == "utility":
        HelpEmbed = discord.Embed(itle="Utility Commands", description="A list of utility commands to fit any needs \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="Help", value="Displays the help message. \nUsage: `/help [category]`\n \u200B", inline=True)
        HelpEmbed.add_field(name="Ping", value="Sends the bot latency in ms. \nUsage: `/ping` \n \u200B", inline=True)
        HelpEmbed.add_field(name="About", value="Displays information about the bot. \nUsage: `/about` \n \u200B", inline=True)
        HelpEmbed.add_field(name="License", value="Displays the bot license. \nUsage: `/license` \n \u200B", inline=True)
        HelpEmbed.add_field(name="GitHub", value="Sends the source code link. \nUsage: `/github` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Invite", value="Sends the bot invite link. \nUsage: `/invite` \n \u200B", inline=True)
        HelpEmbed.add_field(name="Reminder", value="Sets a reminder. \nUsage: `/reminder <minutes> <message>`\n \u200B", inline=True)

    HelpEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
    await ctx.send(embed=HelpEmbed)



@help.error
async def help_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        HelpEmbed = discord.Embed(title="Help", description="Shows a list of commands \n \u200B", color=0x35a64f)
        HelpEmbed.add_field(name="`Utility`", value="Shows a list of utility commands! \nUsage: /help utility \n \u200B", inline=False)
        HelpEmbed.add_field(name="`Fun`", value="Shows a list of commands for fun stuff! \nUsage: /help fun \n \u200B", inline=False)
        HelpEmbed.add_field(name="`Moderation`", value="Shows a list of commands for moderators! \nUsage: /help moderation", inline=False)
        HelpEmbed.set_footer(text=f"At {ctx.message.created_at.strftime('%Y/%m/%d - %I:%M %p GMT')}")
        await ctx.send(embed=HelpEmbed)

@client.event
async def on_disconnect():
    print("GardenBot disconnected.")


# Let's make the Discord.py module understand that there is a folder for additional commands (cogs).

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'extensions.{extension}')

for filename in os.listdir('./extensions'):
    if filename.endswith('.py'):
        client.load_extension(f'extensions.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
