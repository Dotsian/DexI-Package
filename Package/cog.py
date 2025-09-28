from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


class SayCog(commands.Cog):
    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @app_commands.command()
    async def say(self, interaction: discord.Interaction["BallsDexBot"], message: str):
        """
        Says a message as the bot.

        Parameters
        ----------
        message: str
            The message you want to send.
        """
        await interaction.channel.send(message)
