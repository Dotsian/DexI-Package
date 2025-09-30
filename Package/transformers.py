from typing import Iterable, Optional

import discord
from discord import app_commands

from ballsdex.core.bot import BallsDexBot 
from ballsdex.core.utils.transformers import ModelTransformer

from .models import SayLog 


class SayLogTransformer(ModelTransformer[SayLog]):
    name = "saylog"
    model = SayLog()

    def key(self, model: SayLog) -> str:
        return model.name.lower()

    async def load_items(self) -> Iterable[SayLog]:
        return await SayLog.all()

    async def get_options(self, _, value: str) -> list[app_commands.Choice[str]]:
        items = await self.load_items()
        return [      
            app_commands.Choice(name =a.name, value=a. name)
            for a in items
            if value.lower() in a.name.lower()
        ][:25]

    async def transform(
        self, interaction: discord.Interaction["BallsDexBot"], value: str
    ) -> Optional[SayLog]:
        for a in await self.load_items():
            if a.name.lower() == value.lower():
                return a

        await interaction.response.send_message(
            "The log could not be found. Please use the autocompletion.",
            ephemeral=True,
        )

        return None       
            
SayLogTransform = app_commands.Transform[SayLog, SayLogTransformer] 
