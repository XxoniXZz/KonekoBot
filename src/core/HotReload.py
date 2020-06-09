"""
Module to reload cogs on the go.
"""

# Builtins
import logging

# Pip
import traceback
from typing import List

from discord.ext import commands

from src.utils.general import DiscordEmbed

module_logger = logging.getLogger('koneko.HotReloading')


class HotReload(commands.Cog):
    """Class for reloading ."""

    __slots__ = ('bot',)

    def __init__(self, bot):
        self.bot = bot

    def cog_check(self, ctx) -> bool:
        """Cog check

        Only returns true for bot owner."""
        return self.bot.is_owner(ctx.author)

    @commands.command(aliases=["load"], hidden=True)
    async def reload(self, ctx, *extensions) -> None:
        for extension in extensions:
            method, icon = (
                (self.bot.reload_extension, ":repeat:")
                if extension in self.bot.extensions else
                (self.bot.load_extension, ":inbox_tray:")
            )

            try:
                method(extension)
            except Exception as exc:  # pylint: disable=broad-except
                traceback_data = ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__, 1))

                await DiscordEmbed.error(ctx, title=f"{icon}:warning: {extension}", description=f"```python\n {traceback_data}```")
            else:
                await DiscordEmbed.confirm(ctx, title=f"{icon} {extension}")

    @commands.command(hidden=True)
    async def unload(self, ctx, extensions: List[str]) -> None:
        for extension in extensions:
            icon = ":outbox_tray:"
            try:
                self.bot.unload_extension(extension)
            except Exception as exc:  # pylint: disable=broad-except
                traceback_data = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__, 1))

                await DiscordEmbed.error(ctx, title=f"{icon}:warning: `{extension}`", description=f"```python\n {traceback_data}```")
            else:
                await DiscordEmbed.confirm(ctx, title=f"{icon} `{extension}`")


def setup(bot) -> None:
    """The setup function to add this cog to Koneko."""
    bot.add_cog(HotReload(bot))
