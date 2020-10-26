import discord
import os
from discord.ext.commands import Cog, command, has_permissions
from time import sleep

class DistroDownloader(Cog):

    def _init_(self, bot):
        self.bot = bot

    @command()
    async def distrodownload(self, ctx):
        pass
        # Meisme will setup this (distro list etc..)

def setup(bot):
    bot.add_cog(DistroDownloader(bot))