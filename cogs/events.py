import discord
import os
from discord.ext.commands import Cog, command, has_permissions
from time import sleep

class Events(Cog):

    def _init_(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        if "i love ubuntu" in message.content:
            await channel.send("What did you say? You love what?!")
        if "i want everything out of the box in linux" in message.content:
            await channel.send("I don't think Linux is for you....")
        if "i love arch" in message.content:
            await channel.send("Repeat those holy words!")
        if "i love vanilla distros" in message.content:
            await channel.send("Repeat those holy words!")

    @Cog.listener()
    async def on_guild_join(self, user):
        pass
        # I will do this next time lol

def setup(bot):
    bot.add_cog(Events(bot))