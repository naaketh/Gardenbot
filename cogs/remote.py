import discord
import os
import random
from discord.ext.commands import Cog, command, has_permissions
from time import sleep

class Remote(Cog):

    def _init_(self, bot):
        self.bot = bot

    # Data/Handlers go here

    # Main function goes here

    @command()
    async def ssh(self):
        pass

    # For BASH

    @command()
    async def bash(self):
        pass

def setup(bot):
    bot.add_cog(Remote(bot))
