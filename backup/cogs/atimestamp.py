import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

# 1 - Change Filename

class atimestamp(commands.Cog): # 2 - Change Class Name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @app_commands.command(name='atimestamp', description='Retorna a TIMESTAMP atual') # 3 - Change Command Name
    async def atimestamp(self, interaction: discord.Interaction):
        timestamp_now = round(datetime.now().timestamp())
        await interaction.response.send_message(content=f"timestamp atual: '{timestamp_now}', <t:{timestamp_now}:F>", ephemeral=True)    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(atimestamp(bot)) # 4 - Change the prefix "cog1"