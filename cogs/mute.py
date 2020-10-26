import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
from datetime import datetime

class Moderation(commands.Cog):

    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def mute(self,ctx,member : discord.Member, *, reason = None):
        role = discord.utils.get(ctx.guild.roles, name="MutedUsers")
        perms = discord.PermissionOverwrite()
        perms.send_messages = False
        perms.read_messages = True
        if discord.utils.get(ctx.guild.roles, name="MutedUsers"):
            await member.add_roles(role)
        else:
            role = await ctx.guild.create_role(name='MutedUsers', permissions=discord.Permissions(0))
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, overwrite=perms)
        await member.add_roles(role)
        await ctx.send(f'The user {member.mention} has been muted.')
        
    @commands.command()
    @has_permissions(administrator=True)
    async def unmute(self,ctx,member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="MutedUsers")
        await member.remove_roles(role)
        await ctx.send(f"The user {member.mention} has been unmuted.")

def setup(bot):
    bot.add_cog(Moderation(bot))
