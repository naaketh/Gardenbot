import discord
import os
import random
from discord.ext.commands import has_permissions, Cog
from time import sleep
from datetime import datetime

class Misc(Cog):

    def _init_(self, bot):
        self.bot = bot

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

    scary_things = ["😈", "💀", "👻", "🎃", "🧛‍♂️", "🦇", "🧟"]

    distro_list = [
        "Arch Linux", \
        "Ubuntu", \
        "Gentoo", \
        "Mageia", \
        "Debian", \
        "Endeavour OS", \
        "Zorin OS", \
        "Pop_OS!", \
        "Fedora", \
        "Cent OS", \
        "Manjaro", \
        "OpenSUSE", \
        "Kali", \
        "Blackarch", \
        "LFS", \
        "Artix", \
        "Arco",
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
        "Ubuntu 21.04 (Hirsute H...)",
    ]

    vowels = ["a","e","i","o","u","y"]

    consonants = [
        "b","c","d","f","g","h","j","k","l","m", \
        "n","p","q","r","s","t","v","w","x","z"
    ]

    @command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! Client-side ping took {round(bot.latency * 1000)}ms')

    @command()
    async def about(self, ctx):
        await ctx.send(f'Gardenbot is a Discord by me is me forked from PurpleBot (https://github.com/PurpleSci/PurpleBot).')

    @command()
    async def license(self, ctx):
        await ctx.send(f'Gardenbot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot. This is not the full license, it is just summarized. Please read the full license here: https://raw.githubusercontent.com/meisme-dev/Gardenbot/master/LICENSE')

    @command()
    async def github(self, ctx):
        await ctx.send(f'Gardenbot\'s source code is avalaible on GitHub: https://github.com/meisme-dev/Gardenbot')

    @command()
    async def invite(self, ctx):
        await ctx.send(f'If you want to add Gardeonbot to your server, use this link: https://discord.com/api/oauth2/authorize?client_id=769606923091181569&permissions=8&scope=bot')

    @command()
    async def distro(self, ctx):
        await ctx.send(random.choice(distro_list))

    @command()
    async def hello(self, ctx):
        await ctx.send(random.choice(greetings))

    @command()
    async def randnum(self, ctx):
        await ctx.send(random.randint(0, 10000))

    @command()
    async def predict(self, ctx):
        await ctx.send(random.choice(predictions))

    @command()
    async def die(self, ctx):
        await ctx.send(random.choice(death_scenarios))

    @command()
    async def boo(self, ctx):
        await ctx.send(random.choice(scary_things))

    @command()
    async def pogchamp(self, ctx):
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

    @command()
    async def ubuntu(self, ctx):
        await ctx.send(random.choice(ubuntu_versions))

    @command()
    async def groovy(self, ctx):
        await ctx.send(f'https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_500,h_776/https://assets.ubuntu.com/v1/fe951eda-20.10_Groovy+Gorilla_RPi_Sketch.svg')

    @command()
    async def pi(self, ctx):
        await ctx.send(f'Here is π calculated to the first 1000000 digits: http://newton.ex.ac.uk/research/qsystems/collabs/pi/pi6.txt')

    @command()
    async def ptable(self, ctx):
        await ctx.send(f'Ptable is an interactive online version of the Periodic Table of Elements: https://ptable.com/')

    @command()
    async def rubbish(self, ctx):
        sentence = ""
        for i in range(random.randrange(3,7)):
            word = str()
            for j in range(random.randrange(1,5)):
                word = word + random.choice(consonants) + random.choice(vowels)
            sentence = sentence + word + " "
        await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))

    @command()
    async def echo(ctx,*,arg):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{arg}")

def setup(bot):
    bot.add_cog(Misc(bot))
