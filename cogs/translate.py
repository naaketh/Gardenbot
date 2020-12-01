from translate import Translator
from discord.ext import commands

class Utility(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def trans(self,ctx,arg,lang):
        translator = Translator(to_lang=f"{lang}")
        await ctx.send(f"{translator.translate(arg)}")

def setup(client):
    client.add_cog(Utility(client))