#!/usr/bin/env python3

import asyncio
import logging
import time
import discord
from discord.ext import commands
from src.core.config import Settings

logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

settings = Settings()
loop = asyncio.get_event_loop()


KonekoBot = commands.AutoShardedBot(
    # Customizable when running the bot using the "-c" or "--command-prefix" option.
    command_prefix=commands.when_mentioned_or(settings.prefix),
    # Customizable when running the bot using the "-p" or "--pm-help" option.
    pm_help=settings.pm_help,
    owner_id=settings.owner_id,
)

KonekoBot.uptime = time.time()
KonekoBot.dry_run = settings.dry_run


# Function called when the bot is ready.
@KonekoBot.event
async def on_ready():
    game = settings.prefix + "help for help"
    activity = discord.Game(name=game)
    await KonekoBot.change_presence(status=discord.Status.online, activity=activity)
    # Bot logged in.
    print(f'Logged in as {KonekoBot.user}')
    print(f'I am in {len(KonekoBot.guilds)} guilds.')


if __name__ == '__main__':
    for extension in settings.toggle_extensions:
        KonekoBot.load_extension("src.modules." + extension)
    for extension in settings.core_extensions:
        KonekoBot.load_extension(extension)

    if KonekoBot.dry_run is True:
        print("Quitting: dry run")
        close = loop.create_task(KonekoBot.close())
        loop.run_until_complete(close)
        loop.close()
        exit(0)

    KonekoBot.uptime = time.time()
    print("Logging into Discord...")
    KonekoBot.run(settings.token)

    try:
        loop.run_until_complete(KonekoBot)
    except discord.LoginFailure:
        print("Could not login.")
    except Exception as e:
        loop.run_until_complete(KonekoBot.close())
    finally:
        loop.close()
        exit(1)
