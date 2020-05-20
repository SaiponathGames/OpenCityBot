from discord.ext import commands


def is_guild_owner():
    async def predicate(ctx):
        return ctx.author == ctx.guild.owner

    return commands.check(predicate)
