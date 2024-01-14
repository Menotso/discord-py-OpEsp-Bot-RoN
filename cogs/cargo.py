import discord
from discord import app_commands
from discord.ext import commands

class cargo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="addrole",
        description="Atribui um cargo a um operador mencionado.",
    )
    @commands.has_permissions(administrator=True)
    async def addrole(self, interaction: discord.Interaction, cargo: discord.Role, membro: discord.Member):
        try:
            await membro.add_roles(cargo)
            await interaction.response.send_message(f"Cargo {cargo.mention} atribuído a {membro.mention}.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Erro ao atribuir cargo: {e}", ephemeral=True)


    @app_commands.command(
        name="removerole",
        description="Retira um cargo de um membro mencionado.",
    )
    @commands.has_permissions(administrator=True)
    async def removerole(self, interaction: discord.Interaction, cargo: discord.Role, membro: discord.Member):
        try:
            await membro.remove_roles(cargo)
            await interaction.response.send_message(f"Cargo {cargo.mention} retirado de {membro.mention}.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Erro ao retirar cargo: {e}", ephemeral=True)
            
async def setup(bot):
    await bot.add_cog(cargo(bot))