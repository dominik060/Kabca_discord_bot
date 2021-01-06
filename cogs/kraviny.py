import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
class kraviny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hlasky(self, ctx):
        f = open("hlasky.txt", 'r')
        h = f.readlines()
        await ctx.send(random.choice(h))

    @commands.command()
    async def addhl(self, ctx, co):
        yourID = 616550140408496128
        if ctx.message.author.id == yourID:
            f = open("hlasky.txt", 'a')
            f.write(f'\n{co}')
            f.close()
        else:
            ctx.send('Nemáš povolení:)')
        await ctx.send(f"Do hlášek bylo přídáno: {co}")

def setup(bot):
    bot.add_cog(kraviny(bot))
