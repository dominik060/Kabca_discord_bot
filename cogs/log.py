from datetime import datetime
from discord import Embed
from discord.ext.commands import Cog
from discord.ext import commands


class log(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
            self.log_channel = self.bot.get_channel(789229853576527935)


	@Cog.listener()
	async def on_user_update(self, before, after):
		if before.name != after.name:
			embed = Embed(title="Username change",
						  colour=after.colour,
						  timestamp=datetime.utcnow())

			fields = [("Before", before.name, False),
					  ("After", after.name, False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed=embed)

		if before.discriminator != after.discriminator:
			embed = Embed(title="Discriminator change",
						  colour=after.colour,
						  timestamp=datetime.utcnow())

			fields = [("Before", before.discriminator, False),
					  ("After", after.discriminator, False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed=embed)

		if before.avatar_url != after.avatar_url:
			embed = Embed(title="Avatar change",
						  description="New image is below, old to the right.",
						  colour=self.log_channel.guild.get_member(after.id).colour,
						  timestamp=datetime.utcnow())

			embed.set_thumbnail(url=before.avatar_url)
			embed.set_image(url=after.avatar_url)

			await self.log_channel.send(embed=embed)

	@Cog.listener()
	async def on_member_update(self, before, after):
		if before.display_name != after.display_name:
			embed = Embed(title="Nickname change",
						  colour=after.colour,
						  timestamp=datetime.utcnow())

			fields = [("Before", before.display_name, False),
					  ("After", after.display_name, False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed=embed)

		elif before.roles != after.roles:
			embed = Embed(title="Role updates",
						  colour=after.colour,
						  timestamp=datetime.utcnow())

			fields = [("Before", ", ".join([r.mention for r in before.roles]), False),
					  ("After", ", ".join([r.mention for r in after.roles]), False)]

			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)

			await self.log_channel.send(embed=embed)


	@Cog.listener()
	async def on_message_delete(self, message):
		if not message.author.bot:
			if ',spam' in message:
				embed = Embed(title="Message delet",
							  description=f"Action by {message.author.display_name}.",
							  colour=message.author.colour,
							  timestamp=datetime.utcnow())

				fields = [("Content", message.content, False)]

				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)

				await self.log_channel.send(embed=embed)
			else:
				print('deleted message wihout ,spam')

def setup(bot):
	bot.add_cog(log(bot))
