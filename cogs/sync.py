import discord
from discord import app_commands
from discord.ext import commands

# 1 - Change filename.

class sync(commands.Cog): # 2 - change class name
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Sync all the commands:    
    @commands.command(name='sync') # 3 - Change command name
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx):
        await ctx.bot.tree.sync()
        await ctx.reply('(READY) SLASH CMDs SYNCED', ephemeral=True)
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(sync(bot)) # 4 - Change the prefix "shutdown"