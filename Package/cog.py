from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands

from .models import SayLog
from .transformers import SayLogTransform

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
        await interaction.response.send_message("Message sent!", ephemeral=True)
        await interaction.channel.send(message)

        await SayLog.create(message=message)

    @app_commands.command()
    @commands.is_owner()
    async def saylog(self, interaction: discord.Interaction["BallsDexBot"], log: SayLogTransform):
        """
        Sends a `/say` message log.

        Parameters
        ----------
        log: SayLog
            The log you want to view.
        """
        embed = discord.Embed(title="Message Log", description=log.message)

        await interaction.response.send_message(embed=embed, ephemeral=True)
