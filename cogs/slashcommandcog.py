import discord
from discord import app_commands
from discord.ext import commands

# 1 - Change filename.

class slashcommandcog(commands.Cog): # 2 - change class name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    #COMMAND   
    @commands.command(name="slashcommandcog") # Todos os aliases executam este código, PRECISA ser uma lista.
    @commands.has_permissions(administrator=True) # Permite usar o comando caso o usuário possuir permissão de ADMINISTRADOR
    async def slashcommandcog(self, ctx: commands.Context):
        await ctx.send(f'Estou me desligando...')
    
        # 3 - Insert command and change its name
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(slashcommandcog(bot)) # 4 - Change the prefix "shutdown"