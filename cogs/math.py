import discord
import math
from discord.ext import commands
from discord.ext.commands import bot
class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx, *, expression: str):
        calculation = eval(expression)
        em = discord.Embed(color=discord.Color.green())
        em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        em.add_field(name="Math:", value=f" {str(expression)} ", inline=False)
        em.add_field(name="Answer:", value=f" {str(calculation)} ", inline=False)
        await ctx.channel.send(embed=em)


def setup(bot):
    bot.add_cog(math(bot))