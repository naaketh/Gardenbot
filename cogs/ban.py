import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def ban(self,ctx,member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        embedVar = discord.Embed(title=f"Ban", description=f"{member.mention} was banned for {reason}.", color=0x35a64f)
        await ctx.message.delete()
        await ctx.send(embed=embedVar)
        
    @commands.command()
    @has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
            embedVar = discord.Embed(title=f"Warned", description=f"{member.mention} was unbanned.", color=0x35a64f)
            await ctx.message.delete()
            await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Moderation(client))