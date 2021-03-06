import discord
from discord.ext import commands
import asyncio
import datetime
import random
from discord.ext.commands import bot
import time

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        global role
        role = discord.utils.get(member.guild.roles, id=788445212351135746)
        global welcome_channel
        welcome_channel = bot.get_channel(788422093556678716)
        await member.add_roles(role)
        await welcome_channel.send(f"Vítej {member} na serveru! Nezapomeň si přešíst #788420405890252842!")


    @commands.command()
    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}")
        em = discord.Embed(color=discord.Color.red())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount + 1)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def qp(self, ctx, *, question):
        await ctx.channel.purge(limit=1)
        em = discord.Embed(color=discord.Color.blue())
        em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        em.add_field(name=f"{question}", value="✅ ano    ❎ ne")
        message = await ctx.channel.send(embed=em)
        await message.add_reaction(emoji="✅")
        await message.add_reaction(emoji="❎")


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gw(self, ctx, mins: int, prize: str):
        em = discord.Embed()
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins * 60)
        em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        em.title = prize
        em.description = "React To Giveaway With 🎉 To Join."
        em.add_field(name='Giveaway end date', value=end, inline=False)
        msg = await ctx.send(embed=em)
        await msg.add_reaction('🎉')
        time.sleep(mins - 60)
        nmsg = await ctx.channel.fetch_message(msg.id)
        users = nmsg.reaction[0].users().flatten()
        users.pop(users.index(bot.users))
        winner = random.choice(users)
        await ctx.send(f"Blahopřeji! {winner.mention} vyhrál {prize}!")


    @commands.command()
    async def invites(self, ctx, author):
        global totalInvites
        totalInvites = 0
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses
        await ctx.send(f"{author} invited {totalInvites} member{'' if totalInvites == 1 or 0 else 's'} to the server!")


def setup(bot):
    bot.add_cog(mod(bot))