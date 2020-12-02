# MIT License

# Copyright (c) 2020 me is me

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#Define dependencies of the bot and import them
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
import discord


#Define the class and initialize the bot
class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client


#Define the commands
    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self,ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)
        embedVar = discord.Embed(title="Purged", description=f"Deleted {amount} messages", color=0x35a64f)
        sent = await ctx.send(embed=embedVar)
        sleep(1)
        await sent.delete()


#Connect the cog to the main bot
def setup(client):
    client.add_cog(Moderation(client))