import discord
from discord.ext import commands

# 1 - Change Filename

class rulesembed(commands.Cog): # 2 - Chance Class Name
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    # EMBED de Informações do usuário
    @commands.command(name="rulesembed", aliases=['rules', 'rule', 'regra', 'regras'])
    @commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
    @commands.has_permissions(administrator=True) # Permite usar o comando caso o usuário possuir permissão de ADMINISTRADOR
    async def rulesembed(self, ctx):
        
        await ctx.message.delete()
        # Embed de imagem sozinha
        embed_rules_image = discord.Embed(color=discord.Colour.dark_orange())
        embed_rules_image.set_image(url='https://media.discordapp.net/attachments/1032063754843738202/1185249698555121684/GIF_REGRAS.gif?ex=658eeccd&is=657c77cd&hm=ed857e5c99ef956fdb70880edf0b175755e6174269c67966bd2dbd155bbb429a&=&width=687&height=250')
        
        # Embed de regras
        embed_rules = discord.Embed(color=discord.Colour.light_embed())
        embed_rules.add_field(name='', value=f'<:1_:1109695579568742490> **Não trate mal outros usuários**\n> Somos uma comunidade inclusiva, qualquer tipo de discurso de ódio ou chacota a outros membros é proibido, recepcione bem novatos e não use palavras de baixo calão com frequência. Grupos ou panelinhas que excluam ou menosprezem outros membros são proibidos.', inline=False)
        embed_rules.add_field(name='', value=f'<:2_:1109695576913747991> **Sem conteúdo inapropriado**\n> Isso inclui mas não se limita a mídia sensível/NSFW, "humor pesado", conteúdo adulto e conotação sexual ou sugestiva desnecessária. É proibido referências a extremismo, mesmo em tom de ironia ou meme.', inline=False)
        embed_rules.add_field(name='', value=f'<:3_:1109695575944871996> **Não atrapalhe o fluxo dos canais**\n> Por favor não envie spam, flood, correntes ou qualquer coisa que atrapalhe o fluxo dos canais. Não tente burlar nossos filtros automáticos - eles existem por um motivo.', inline=False)
        embed_rules.add_field(name='', value=f'<:4_:1109695573264715796> **Sem divulgação ou autopromoção**\n> Não faça propaganda, divulgue ou ofereça algo de forma generalizada, exceto se autorizado.', inline=False)
        embed_rules.add_field(name='', value=f'<:5_:1109695571956088862> **Não peça ou compartilhe informações pessoais**\n> Não pergunte ou compartilhe idade, fotos (exceto de figuras públicas), endereço, número de telefone etc. Você pode ser moderado se acharmos que você não está seguro com suas próprias informações ou que está pedindo informações que você não deveria ter.', inline=False)
        embed_rules.add_field(name='', value=f'<:c6_:1180307649326219384> **Sugira mudanças de forma construtiva**\n> Caso você queira fazer uma crítica às regras (ou à staff ou servidor), faça apenas na categoria de Suporte se possível apresentando uma solução junto. Não tente menosprezar, causar vexame ou humilhar membros da Staff.', inline=False)
        embed_rules.add_field(name='', value=f'<:c7_:1180307650660020335> **Requisição de idade mínima**\n> A idade mínima para acessar o Discord é 13 anos, conforme os TOS do Discord. [Leia mais.](https://support.discord.com/hc/en-us/articles/360040724612-Why-is-Discord-asking-for-my-birthday-)\n> Perguntar informações pessoais (incluindo idade) é contra nossas regras, assim como zombar alguém por ser menor de idade.)', inline=False)
        
        # Última Embed de regras com footer.
        embed_rules_last = discord.Embed(color=discord.Colour.dark_orange())
        embed_rules_last.add_field(name='', value=f'<:DiscordModeration:1180289235375378564> Você também precisa seguir os [Termos de Serviço](https://discord.com/tos), as [Diretrizes da Comunidade](https://discord.com/guidelines) do Discord e as legislações do Brasil e outros países.', inline=False)
        embed_rules_last.add_field(name='', value=f'<a:Information:1180289249623429243> Você também precisa cumprir todas as regras no seu **perfil do Discord** (avatar, banner, bio, etc) e nas **Mensagens Diretas** dos membros.', inline=False)
        embed_rules_last.add_field(name='', value=f'<a:Moderator_Color28:1180289264047628419> Nem todas as quebras de regras vão te banir do servidor ou deixar de castigo instantaneamente, você pode apenas receber um alerta nas Mensagens Diretas. Por causa disso, deixe as DMs abertas neste servidor.', inline=False)
        embed_rules_last.set_footer(text='OpEsp ROLEPLAY. Todos os direitos Reservados.')
        
        # Itera e retorna os 3 embeds
        embeds = [embed_rules_image, embed_rules, embed_rules_last]

        for embed in embeds:
            await ctx.send(embed=embed)
        
            # 3 - Insert command and change its name
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(rulesembed(bot)) # 4 - Change the prefix "shutdown"