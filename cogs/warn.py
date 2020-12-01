import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def warn(self,ctx,member : discord.Member, *, reason = None):
        await ctx.message.delete()
        embedVar = discord.Embed(title="Warned", description=f"{member.mention} was warned for {reason}.", color=0x35a64f)
        await ctx.send(embed=embedVar)
        await member.send(F"You have been warned for {reason}")
        
    @commands.command()
    @has_permissions(administrator=True)
    async def pardon(self,ctx,member : discord.Member):
        await ctx.message.delete()
        embedVar = discord.Embed(title="Pardoned", description=f"{member.mention} was pardoned.", color=0x35a64f)
        await ctx.send(embed=embedVar)
        await member.send("You have been pardoned")

def setup(client):
    client.add_cog(Moderation(client))