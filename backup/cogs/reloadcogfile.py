import discord
from discord import app_commands
from discord.ext import commands
from typing import Literal

# 1 - Change Filename

class reloadcogfile(commands.Cog): # 2 - Change Class Name
    def __init__(self, bot: commands.Bot):
        self.bot = bot 

    # Recarregar os COGS
    @app_commands.command(name="reloadcogfile", description="Recarrega uma Classe Cog")
    async def reloadcogfile(self, interaction: discord.Interaction, cog:Literal["treecommandcog", "shutdown", "sync",
                                                                            "slashcommandcog", "clear", "userinfo",
                                                                            "kick", "ban", "reloadcogfile", "giveaway",
                                                                            "atimestamp", "atstamp", "rulesembed",
                                                                            "invite", "reactionrole", "opd",
                                                                            "ops", "levelsystem", "cargo",
                                                                            "steamid"]): # insert all cog filenames here
        await self.bot.reload_extension(name="cogs."+cog) # self -> bot
        await interaction.response.send_message(f"✅ Arquivo recarregado com sucesso: **{cog}.py**.")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(reloadcogfile(bot)) # 4 - Change the prefix "cog1"

