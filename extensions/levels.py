from decouple import config
from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
import mysql
import mysql.connector
from mysql.connector import Error

class Levels(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def create_connection(self, ctx):
        connection = None
        mydb = mysql.connector.connect(
            host="192.168.2.132",
            user="root",
            password="L0l!2779")
        print(mydb)


def setup(client):
    client.add_cog(Levels(client))