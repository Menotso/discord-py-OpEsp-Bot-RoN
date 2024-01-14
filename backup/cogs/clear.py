import discord
from discord import app_commands
from discord.ext import commands

# 1 - Change filename.

class clear(commands.Cog): # 2 - change class name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    # CLEAR chat messages COMMAND
    @commands.command(aliases=['limpar'])
    @commands.has_permissions(manage_messages=True) # Permite usar o comando caso o usuário possuir permissão para manusear mensagens
    async def clear(self, ctx, amount=10):
        amount += 1
        if amount > 101:    
            await ctx.reply('Não é possível deletar mais de 100 mensagens.')
        else:
            await ctx.channel.purge(limit=amount)
            print(f'{amount - 1} Mensagens deletadas.')

        # 3 - Insert command and change its name
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(clear(bot)) # 4 - Change the prefix "shutdown"