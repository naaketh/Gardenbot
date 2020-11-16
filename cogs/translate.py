from googletrans import Translator
from discord.ext import commands

class Utility(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def trans(self,ctx,arg,lang):
        translator = Translator()
        translated = translator.translate(f'{arg}', dest=f"{lang}")
        await ctx.send(f'{translated.text}')
        translated = None
        lang = None
        arg = None

def setup(client):
    client.add_cog(Utility(client))