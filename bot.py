import sys
import traceback
import discord
from discord.ext import commands
import random
import math
from math import pi
import time
import requests
from discord.ext.commands import Bot
import os
import keep_alive
from keep_alive import keep_alive

bot: Bot = commands.Bot(command_prefix=',')
#bot.remove_command('help')
init_extension = ['cogs.fun', 'cogs.kraviny', 'cogs.math', 'cogs.mod']
if __name__ == '__main__':
    for extension in init_extension:
        try:
            bot.load_extension(extension)
            print(f'Nacteno {extension}')
        except Exception as e:
            print(f'Nepodarilo se nacist {extension}.', file=sys.stderr)
            traceback.print_exc()
          
"""@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('cs'):
        await message.channel.send('cs debílku!')
    if message.content.startswith('5'):
        await message.channel.send('jsi L')
    if message.content.startswith('nn'):
        await message.channel.send('ale jj')
    if message.content.startswith('jj'):
        await message.channel.send('ale nn')
    if message.content.startwith('https://giphy.com'):
        await message.channel.send('Už zase gif')
    if message.content.startwith('https://tenor.com'):
        await message.channel.send('Už zase gif')        
    if message.content.startswith('ty mlč'):
        await message.channel.send('nn')
    if message.content.startswith('ty mlc'):
        await message.channel.send('nn')"""  
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='všechen tvůj pohyb!'))
    print('-' * len(str(bot.user.id)))
    print('Bot:')
    print(bot.user.name)
    print(bot.user.id)
    print('-' * len(str(bot.user.id)))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.channel.send("Tenhle command neznám! Zkus ,help")


            
            
# Commands



@bot.command()
async def lol(ctx, victim: discord.User, amount=2, *agrs):
    response = ""
    for arg in agrs:
        response = response + " " + arg                   
    for _ in range(amount):
        await victim.send(response)                   
                   

    

#@bot.command()
#async def help(ctx):
    #em = discord.Embed(color=discord.Color.green())
    #em.title = 'Kabča commands'
    #em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    #em.description = 'Vytvořil D0M1'
    #em.add_field(name="prefix", value=",", inline=False)
    #em.add_field(name="info", value="zobrazím informace o sobě")
    #em.add_field(name="ping", value="zobrazím svoji odezvu", inline=False)
    #em.add_field(name="clear (číslo)", value="vymažu počet zpráv", inline=False)
    #em.add_field(name="8b (otázka)", value="odpovím na otázku", inline=False)
    #em.add_field(name="help", value="zobrazí ti tadytu zprávu", inline=False)
    #em.add_field(name="cat", value="ukážu ti náhodný obrázek kočky", inline=False)
    #em.add_field(name="say (co)", value="napíšu to co ty", inline=False)
    #em.add_field(name="xd", value="napíšu xdddddddddd", inline=False)
    #em.add_field(name="math (příklad)", value="vypočtu ti matematický příklad", inline=False)
    #em.add_field(name="pytlik", value="nech se překvapit", inline=False)
    #em.add_field(name="dedavlese", value="nech se překvapit", inline=False)
    #em.add_field(name="qp (otázka)", value="quick poll(ano, ne)", inline=False)
    #em.add_field(name="poll (otázka)", value="stajný jak qp, ale lépe vypadá", inline=False)
    #em.add_field(name="spam (co)", value="prostě budu spamit dokud mě nevypneš", inline=False)
    #em.add_field(name="stop", value="zrusi spam", inline=False)
    #em.add_field(name="ban (jméno, důvod)", value="prostě ban", inline=False)
    #em.add_field(name="unban (jméno)", value="prostě unban", inline=False)
    #em.add_field(name="invites (jméno)", value="invites", inline=False)
    #em.add_field(name="help", value="zobrazím tadytu zprávu", inline=False)
    #em.set_footer(text="Kabča tě vidí!!!!")
    #await ctx.channel.send(embed=em)


@bot.command(pass_context=True)
async def info(ctx):
    em = discord.Embed(color=discord.Color.green())
    em.title = 'Kabča info'
    em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    em.description = 'Vytvořil D0M1'
    em.add_field(name="Servery", value=len(bot.guilds))
    em.add_field(name="Online Uživatelé",
                 value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})))
    em.add_field(name='Kanály', value=f"{sum(1 for g in bot.guilds for _ in g.channels)}")
    em.set_footer(text="Kabča opravuje písemky")
    await ctx.channel.send(embed=em)




@bot.command(pass_context=True)
async def ping(ctx):
    em = discord.Embed(color=discord.Color.blue())
    em.add_field(name="Pong!", value=f"{round(bot.latency * 1000)}ms")
    await ctx.channel.send(embed=em)




@bot.command()
async def jnds(ctx):
    response = "MĚLI BYST SE POMODLIT A POŽÁDAT KABČU, ABY BYL PRODLOUŽEN NOUZOVÝ STAV A VY NEŠLI DO ŠKOLY"
    await ctx.channel.send(response)


                   


# JOKES

@bot.command()
async def dedavlese(ctx):
    response = """
Běží děda po lese
všechno na něm třese se
přehání to s projímadlem
třese mu to s jeho sádlem
máš to marný staříku nedoběhneš k hajzlíku!!!!
                """
    await ctx.channel.send(response)


@bot.command()
async def pytlik(ctx):
    response = """
Dnes ráno na záchodě,
strašlivě jsem vykřik.
Pod prkýnko od hajzlíku,
přiskřip jsem si pytlík.
"""
    await ctx.channel.send(response)
    
keep_alive()
bot.run("TOKEN")
