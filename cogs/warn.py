import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def warn(self,ctx,member : discord.Member, *, reason = None):
        await ctx.channel.purge(limit=1)
        await ctx.send(F"{member.mention} has been warned for {reason}")
        await member.send(F"You have been warned for {reason}")
        
    @commands.command()
    @has_permissions(administrator=True)
    async def pardon(self,ctx,member : discord.Member):
        await ctx.channel.purge(limit=1)
        await member.send("You have been pardoned")

def setup(client):
    client.add_cog(Moderation(client))
