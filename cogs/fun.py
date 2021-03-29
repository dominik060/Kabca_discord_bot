import re
from urllib import parse, request
import discord
import requests
from discord.ext import commands
import random
class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8b'], pass_context=True)
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        em = discord.Embed(color=discord.Color.grey())
        em.add_field(name="Qustion: ", value=f"{str(question)}", inline=False)
        em.add_field(name="Answer: ", value=f"{random.choice(str(responses))}", inline=False)
        await ctx.channel.send(embed=em)

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        await ctx.channel.send(data['file'])

    @commands.command()
    async def say(self, ctx, *args):
        response = ""
        for arg in args:
            response = response + " " + arg
        await ctx.channel.send(response)

    @commands.command()
    async def vs(self, ctx, h: int):
        r = ""
        n = "\n"
        for i in range(1, h):
            r += (h - i) * " " + i * "*" + (i - 1) * "*"+"\n"
        r += (h - 1) * " " + "|"
        await ctx.send(f"""```
        {n}{r}
        ```""")

def setup(bot):
    bot.add_cog(fun(bot))