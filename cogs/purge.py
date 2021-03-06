from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep

class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self,ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)
        sent = await ctx.send(F"Deleted `{amount}` messages")
        sleep(1)
        await sent.delete()

def setup(client):
    client.add_cog(Moderation(client))