import discord
from discord.ext import commands
import random
import math
from math import pi, sin, acos, e, erf, exp, log, asin, atan, inf, pow, tau, prod, ceil, comb, cos, cosh, dist, erfc, \
    fabs, fmod, fsum, gcd, log2, modf, nan, perm, sinh, sqrt, __spec__, tan, tanh, acosh, asinh, atan2, atanh, expm1, \
    floor, frexp, gamma, hypot, isinf, isnan, isqrt, __loader__, ldexp, log1p, log10, trunc, lgamma, copysign, degrees, \
    factorial, isclose, isfinite, radians, remainder
import time
import requests
from discord.ext.commands import Bot
import pyautogui

client: Bot = commands.Bot(command_prefix=',')


# Events

@client.event
async def on_ready():
    print('Bot is ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='všechen tvůj pohyb!'))


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')


# Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ban(member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def kick(member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def say(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response)


@client.command()
async def spam(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response * 10)


@client.command()
async def jnds(ctx):
    response = "MĚLI BYST SE POMODLIT A POŽÁDAT KABČU, ABY BYL PRODLOUŽEN NOUZOVÝ STAV A VY NEŠLI DO ŠKOLY"
    await ctx.channel.send(response)


@client.command()
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.channel.send(data['file'])

@client.command()
async def dog(ctx):
    response = requests.get('https://random.dog')
    data = response.json()
    await ctx.channel.send(data['file'])
# JOKES

@client.command()
async def dedavlese(ctx):
    response = """
Běží děda po lese
všechno na něm třese se
přehání to s projímadlem
třese mu to s jeho sádlem
máš to marný staříku nedoběhneš k hajzlíku!!!!
                """
    await ctx.channel.send(response)


@client.command()
async def pytlik(ctx):
    response = """
Dnes ráno na záchodě,
strašlivě jsem vykřik.
Pod prkýnko od hajzlíku,
přiskřip jsem si pytlík.
"""
    await ctx.channel.send(response)


@client.command()
async def xd(ctx):
    response = "xd"
    await ctx.channel.send(response)


@client.command()
async def math(ctx, *, expression: str):
    calculation = eval(expression)
    await ctx.send('Math: {}\nAnswer: {}'.format(expression, calculation))


@client.command()
async def beemovie(ctx):
    response = open('beemovie.txt', 'r')
    for line in response.readline():
        await ctx.channel.send(line)
        pyautogui.press('enter')

client.run('bot token')
