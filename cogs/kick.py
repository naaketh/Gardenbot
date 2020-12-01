import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        embedVar = discord.Embed(title="Kicked", description=f"{member.mention} has been kicked for {reason}", color=0x35a64f)
        await ctx.send(embed=embedVar)
        await ctx.message.delete()

def setup(client):
    client.add_cog(Moderation(client))