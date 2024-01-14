import discord
from discord import app_commands
from discord.ext import commands

class shutdown(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    # SHUTDOWN THE BOT    
    @commands.command(name="shutdown", aliases=['close', 'stop', 'parar', 'fechar', 'desligar']) # Todos os aliases executam este código, PRECISA ser uma lista.
    @commands.has_permissions(administrator=True) # Permite usar o comando caso o usuário possuir permissão de ADMINISTRADOR
    async def shutdown(self, ctx: commands.Context):
        await ctx.message.delete()
        await ctx.send(f'Estou me desligando...')
        await self.bot.close()
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(shutdown(bot))
    

