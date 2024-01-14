import discord
from discord import app_commands
from discord.ext import commands, tasks
from datetime import datetime

class steamid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_id_mapping = {}  # Dicionário para armazenar o mapeamento de ID para string

    @app_commands.command(
        name="registrarsteam",
        description="Registra o STEAM ID.",
    )
    async def registrarsteam(self, interaction: discord.Interaction, entrada: str):
        user_id = interaction.user.id

        if user_id in self.user_id_mapping:
            # Se o usuário já está no dicionário, retorna o ID correspondente
            id_associado = self.user_id_mapping[user_id]
            await interaction.response.send_message(f"Você já está associado ao ID: {id_associado}", ephemeral=True)
        else:
            # Se o usuário não está no dicionário, armazena a entrada fornecida
            self.user_id_mapping[user_id] = entrada
            await interaction.response.send_message(f"STEAM ID registrado com sucesso! Seu ID: {user_id}", ephemeral=True)

    @app_commands.command(
        name="steamid",
        description="Mostra seu STEAM ID para todos.",
    )
    async def obter_id(self, interaction: discord.Interaction):
        user_id = interaction.user.id

        if user_id in self.user_id_mapping:
            # Se o usuário está no dicionário, retorna a string associada
            id_associado = self.user_id_mapping[user_id]
            await interaction.response.send_message(f"> **STEAM ID** do {interaction.user.mention}: **{id_associado}**")
        else:
            # Se o usuário não está no dicionário, informa que a string não foi encontrada
            await interaction.response.send_message("Você não tem um STEAM ID registrado. Use **/registrarsteam** para registrar.", ephemeral=True)
            
    @app_commands.command(
        name="backup_steamid",
        description="Faz backup dos STEAM ID e envia na DM do usuário.",
    )
    @commands.has_permissions(administrator=True)
    async def backup_steamid(self, interaction: discord.Interaction):
        backup_dict = self.user_id_mapping.copy()
        await interaction.user.send(f"**({datetime.now().strftime('%d-%m-%Y')})** - Backup de **STEAM ID:**\n{backup_dict}")
        await interaction.response.send_message(f'Te enviei uma mensagem no privado com o **backup** de **STEAM ID!**', ephemeral=True, delete_after=10)

    @tasks.loop(hours=24)
    async def backup_loop(self):
        # Get the current date
        current_date = datetime.now().strftime('%d-%m-%Y')

        # Send the backup to the first administrator found in the bot's guilds
        """for guild in self.bot.guilds:
            for member in guild.members:
                if member.guild_permissions.administrator:
                    admin_user = member
                    break"""
        #else:
            # If no administrator found, send the backup to the bot owner
        admin_user = self.bot.owner

        backup_dict = self.user_id_mapping.copy()
        await admin_user.send(f"**({current_date})** - Backup de **STEAM ID:**\n{backup_dict}")

async def setup(bot):
    await bot.add_cog(steamid(bot))
