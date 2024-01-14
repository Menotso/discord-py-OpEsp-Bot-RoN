import discord
from discord.ext import commands

# 1 - Change Filename

class userinfo(commands.Cog): # 2 - Chance Class Name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    # EMBED de Informações do usuário
    @commands.command(name="userinfo", aliases=['memberinfo', "uinfo", "minfo"])
    @commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
    @commands.has_permissions(administrator=True) # Permite usar o comando caso o usuário possuir permissão de ADMINISTRADOR
    async def userinfo(self, ctx, member:discord.Member=None):
        if member == None:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(title='Informações de membro da comunidade:', description=f'Membro: {member.mention}', color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Nome", value=f"`{member.name}#{member.discriminator}`", inline=True)
        embed.add_field(name="Apelido", value=f'`{member.display_name}`', inline=True)
        embed.add_field(name="ID", value=f'`{member.id}`', inline=True)
        #embed.add_field(name="Status", value=f'`{member.status}`', inline=False)
        embed.add_field(name=f"Cargos ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Cargo mais alto", value=member.top_role.mention, inline=False)
        embed.add_field(name="Criado em", value=member.created_at.strftime('%a, %B, %d, %Y, %I:%M %p '), inline=False)
        embed.add_field(name="Entrou no servidor em", value=member.joined_at.strftime('%a, %B, %d, %Y, %I:%M %p '), inline=False)
        embed.set_footer(text='OpEsp ROLEPLAY. Todos os direitos reservados.')
        
        await ctx.send(embed=embed)
        
            # 3 - Insert command and change its name
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(userinfo(bot)) # 4 - Change the prefix "shutdown"