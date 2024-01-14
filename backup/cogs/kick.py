import discord
from discord import app_commands
from discord.ext import commands

# 1 - Change Filename

class kick(commands.Cog): # 2 - Change Class Name
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Comando de KICK
    @app_commands.command(name="kick",description='KICKAR usuário do servidor') # 3 - Change Command Name
    @commands.has_permissions(kick_members=True) # Permite usar o comando caso o usuário possuir permissão para kickar
    async def kick(self, interaction: discord.Interaction, member:discord.Member, *, motivo: str=None):
        if motivo == None:
            motivo="Nenhum motivo declarado."
        await member.kick(reason=motivo)
        await interaction.response.send_message(f'⛔ Usuário {member.mention} foi kickado. Motivo: {motivo}')

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(kick(bot)) # 4 - Change the prefix "cog1"

