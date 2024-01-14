import discord
from discord import app_commands
from discord.ext import commands

# 1 - Change Filename

class treecommandcog(commands.Cog): # 2 - Change Class Name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @app_commands.command(name='treecommandcog', description='Exemplo de TREE COMMAND em COG') # 3 - Change Command Name
    @commands.has_permissions(administrator=True)
    async def tree_command_cog(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"Olá {interaction.user.name} !")    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(treecommandcog(bot)) # 4 - Change the prefix "cog1"
