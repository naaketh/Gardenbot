import discord
import os
import random
from discord.ext.commands import Cog, command, has_permissions
from time import sleep
from datetime import datetime

class Moderation(Cog):

    def _init_(self, bot):
        self.bot = bot

    @command()
    @has_permissions(administrator=True)
    async def ban(self,ctx,member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'The user {member.mention} has been banned.')
        
    @command()
    @has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
            await ctx.send(f'The user {member} has been unbanned.')

def setup(bot):
    bot.add_cog(Moderation(bot))
