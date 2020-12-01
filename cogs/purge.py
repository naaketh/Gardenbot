from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
import discord

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self,ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)
        embedVar = discord.Embed(title=f"Warned", description=f"Deleted `{amount}` messages`", color=0x35a64f)
        sent = await ctx.send(embed=embedVar)
        sleep(1)
        await sent.delete()

def setup(client):
    client.add_cog(Moderation(client))