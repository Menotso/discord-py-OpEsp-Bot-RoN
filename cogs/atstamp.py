import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta

class atstamp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @app_commands.command(name='atstamp', description='Retorna a TIMESTAMP FUTURA')
    async def atstamp(self, interaction: discord.Interaction, data_futura: str):
        if "/" not in data_futura:
            return await interaction.response.send_message("Por favor, forneça uma data válida no formato DD/MM/AAAA.", ephemeral=True)
        
        # Converte a data fornecida pelo usuário para um objeto datetime
        data_obj = datetime.strptime(data_futura, '%d/%m/%Y')
        
        # Calcula a timestamp com base na data fornecida
        timestamp_futura = round(data_obj.timestamp())
        
        # Envia a resposta com a timestamp formatada
        await interaction.response.send_message(f"timestamp para {data_futura}: {timestamp_futura} (<t:{int(timestamp_futura)}:F>)", ephemeral=True)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(atstamp(bot)) 