import discord
from discord.ext import commands


class Mention_Reply(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message):
		for mention in message.mentions:
			if mention == message.guild.me:
				await message.channel.send("I am OpenCityBot. My prefix is `!`. ")


def setup(bot):
	bot.add_cog(Mention_Reply(bot))