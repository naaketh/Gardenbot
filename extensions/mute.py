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
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


#Define the class and initialize the bot
class Moderation(commands.Cog):

    def _init_(self, client):
        self.client = client


#Define the commands
    @commands.command()
    @has_permissions(manage_roles=True)
    async def mute(self,ctx,member : discord.Member, *, reason = None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        perms = discord.PermissionOverwrite()
        perms.send_messages = False
        perms.read_messages = True
        if discord.utils.get(ctx.guild.roles, name="Muted"):
            await member.add_roles(role)
        else:
            role = await ctx.guild.create_role(name='Muted', permissions=discord.Permissions(0))
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, overwrite=perms)
        await member.add_roles(role)
        embedVar = discord.Embed(title="Muted", description=f"{member.mention} was muted for {reason}.", color=0x35a64f)
        await ctx.message.delete()
        await ctx.send(embed=embedVar)
        
    @commands.command()
    @has_permissions(administrator=True)
    async def unmute(self,ctx,member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        embedVar = discord.Embed(title=
        "Unmuted", description=f"{member.mention} was unmuted.", color=0x35a64f)
        await ctx.message.delete()
        await ctx.send(embed=embedVar)


#Connect the cog to the main bot
def setup(client):
    client.add_cog(Moderation(client))