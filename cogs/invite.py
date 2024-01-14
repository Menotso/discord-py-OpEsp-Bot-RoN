import discord
from discord import app_commands
from discord.ext import commands

# 1 - Change filename.

class invite(commands.Cog): # 2 - change class name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    #COMMAND   
    @commands.command(name='invite', aliases=['convite']) # Todos os aliases executam este código, PRECISA ser uma lista.
    async def invite(self, ctx: commands.Context):
        invite_link = 'https://discord.gg/AP7E6nn3hE'
        await ctx.message.delete()
        await ctx.send(invite_link)
            
        
        # 3 - Insert command and change its name
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(invite(bot)) # 4 - Change the prefix "shutdown"