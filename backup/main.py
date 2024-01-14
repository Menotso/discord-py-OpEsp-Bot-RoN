import random
import discord
from discord import ui #app_commands
#from discord.ui import Select
from datetime import datetime
from discord.ext import commands, tasks
import platform
from captcha.image import ImageCaptcha
import asyncio
from cogs.levelsystem import levelsystem

id_do_servidor = 1114290574044971031
id_cargo_atendente = 1114290574678310914 # alterar, atual: programador
token_bot = 'MTE3OTg5OTg2NDk5ODQ5MDIwMg.GuC1EJ.L3epBdcPcOzhsvJARn_EdWFB5hjTVgUAWFpvAQ' # 'MTE4NTAxMTk5NDkxNTUxNjUwNg.Gyei0V.Z09adck77yZ40zbet8Qk3LlXXygbD3vhHCAvhs'
all_intents = discord.Intents.all() # Isso é necessário para acessar alguns eventos, como membros entrando no servidor

# ----------------------------Persistência de Botões------------------------------------
class PersistentViewBot(commands.Bot):
    def __init__(self):
        # Permite utilizar os comandos ctx do bot e neste formato, também os slash_commands.
        super().__init__(command_prefix='!', intents=all_intents) # help_command=None evita um erro ao criar um comando help, pois ele já existe embutido no discord.py
        
# ------------------------------------COGS---------------------------------                

        self.cogslist = ["cogs.treecommandcog", "cogs.shutdown", "cogs.sync",
                         "cogs.slashcommandcog", "cogs.clear", "cogs.userinfo",
                         "cogs.kick", "cogs.ban", "cogs.reloadcogfile",
                         "cogs.giveaway", "cogs.atimestamp", "cogs.atstamp",
                         "cogs.rulesembed", "cogs.invite", "cogs.reactionrole",
                         "cogs.opd", "cogs.ops", "cogs.levelsystem",
                         "cogs.cargo", "cogs.steamid"] # Insert "cogs." + filename here
    
# -----------------------------ENCERRADO-COGS---------------------------------
    async def setup_hook(self):        
        # Carregando os cogs da lista e retornando os PRONTOS e os que deram ERRO
        #await self.add_cog(levelsystem(bot=self))
        print('[COG:TEST] Código passou de levelsystem.py')
        for ext in self.cogslist:
            try:
                await self.load_extension(ext)
                print(f"(READY) - COG: {ext}")
            except Exception as e:
                print(f"(ERROR) loading cog {ext}: {e}")
        
        print('(READY) - NON-SLASH "$COMMANDS" in COGS')
        
        # Incluir nome das classes que precisam de persistência de botões aqui:
        # Nota: Garantir que as classes tenham o timeout=None e seus botões possuem custom_id.
        self.add_view(DropdownView())
        # 
        
        
        
            
        #self.add_view(CreateTicket())
        #self.add_view(Dropdown())
        #self.add_view(Fecharticket())
        print('(READY) - Setup_hook()')
    print('(READY) - PersistentViewBot()')    
    
# -----------------------ENCERRADO--Persistência de Botões------------------------------------

# Define o prefixo de comandos por servidor:
guild_prefixes = {}
def get_prefix(bot, message):
    if message:
        if message.guild.id in guild_prefixes:
            return guild_prefixes[message.guild.id]
    return "!"

bot = PersistentViewBot()

# Usuário define o prefixo do próprio servidor:
@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx: commands.Context, new_prefix: str):
    guild_prefixes.update({ctx.message.guild.id: new_prefix})
    await ctx.send("Prefix has been updated.")
print('(READY) PREFIX SLASH COMMAND')

@bot.event
async def on_ready():
    print(f'(LOGGED IN): ' + f'{bot.user}')
    print(f'(BOT ID): {bot.user.id}')
    print(f'(DISCORD VERSION): ' + discord.__version__)
    print(f'(PYTHON VERSION): ' + str(platform.python_version()))

    # Contador de membros
    update_member_count.start()
    print('(READY) UPDATE_MEMBER_COUNT TASK')
    # Muda o status do bot
    status = discord.Status.idle # status: online, offline, dnd, idle
    
    # activity: discord.Game(name="a game"), discord.Activity(type=discord.ActivityType.watching, name='a video'), discord.Activity(type=discord.ActivityType.listening, name="a song")), discord.Streaming(name="My Stream", url=my_twitch_url))
    activity = discord.Game(name='Ready or Not')
    await bot.change_presence(status=status, activity=activity)
    print(f'(READY) BOT PRESENCE STATUS: {status}\n(READY) BOT PRESENCE ACTIVITY: {activity}')
    
@bot.event
async def on_button_click(interaction, button, user):
    for cog in bot.cogs.values():
        await cog.on_button_click(interaction, button, user)

# Quando um membro entrar, faça isso:
@bot.event
async def on_member_join(member):
    
    role = discord.utils.get(member.guild.roles, name="Verificação Pendente")
    
	# Enviar mensagem com os botões
    channel = member.guild.system_channel
    
    embed_bem_vindo1 = discord.Embed(color=discord.Colour.dark_orange())
    embed_bem_vindo1.set_image(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185272842548424794/boas_vindas.gif?ex=658f025a&is=657c8d5a&hm=8bfcc97e44649f83ecddfe23e18ce8c312a48eccc5049c6ada2f48b26ea7830b&')
    
    # Criar a mensagem de boas-vindas
    embed_bem_vindo2 = discord.Embed(title='⠀⠀⠀⠀⠀OpEsp Roleplay - Boas Vindas', color=discord.Colour.dark_orange())
    embed_bem_vindo2.set_thumbnail(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')    

    embed_bem_vindo2.set_image(url='https://media1.tenor.com/m/_ha0lKTbRUgAAAAd/ready-or-not-neon-tomb.gif') # INSERIR BANNER AQUI
    embed_bem_vindo2.add_field(name=f'', value=f'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Operador {member.mention}!\nBem-vindo ao servidor mais imersivo de Ready or Not!\n\n Aprenda a jogar conosco, leia o nosso primeiro curso <#1185264572458872903> ou sinta-se à vontade para perguntar no chat <#1114290575588474952>.\n- Evite quebrar nossas diretrizes.\n- Veja nossa operação do dia **/opd** ou da semana **/ops** que te dão bônus quando fizer o seu **/relatorio** no tópico <#1185771784591642716>, lembre de anexar a imagem do final da operação;\n- Visualize como funciona a progressão de patentes no servidor usando **/progresso**\n- Cadastre seu steamid usando **/registrarsteam** e exiba com /steamid;\n- Aperte nos botões abaixo para ser redirecionado e ler nossas **regras**, ir em **suporte** para __atendimento__ ou se inscrever para Staff.', inline=False)	# Emojis do embed de boas vindas
    embed_bem_vindo2.set_footer(text='OpEsp ROLEPLAY. Todos os direitos reservados.', icon_url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')
    name_custom_emoji_cargos = 'TP_Color_GoldenCrown39'
    custom_emoji_cargos_id = 1185024440770252891
    name_custom_emoji_regras = 'apprentice_mod-1'
    custom_emoji_regras_id = 1185024384763707483
    name_custom_emoji_suporte = 'Union_Moderation-1'
    custom_emoji_suporte_id = 1185024455123161178
    channel_1_link = 'https://discord.com/channels/1114290574044971031/1185026136825135174'
    channel_2_link = 'https://discord.com/channels/1114290574044971031/1114290575156465684'
    channel_3_link = 'https://discord.com/channels/1114290574044971031/1185026136825135174'
    
	# emoji=discord.PartialEmoji(animated=False/True, id=custom_emoji_ID, name=custom_emoji_NAME)
	# Criar a classe View para conter os botões
 
    view_boas_vindas = discord.ui.View()
    view_boas_vindas.add_item(discord.ui.Button(
		label="cargos",
		style=discord.ButtonStyle.link,
		url=channel_1_link,
		emoji=discord.PartialEmoji(animated=False, id=custom_emoji_cargos_id, name=name_custom_emoji_cargos)
	))
    view_boas_vindas.add_item(discord.ui.Button(
		label="regras",
		style=discord.ButtonStyle.link,
		url=channel_2_link,
		emoji=discord.PartialEmoji(animated=True, id=custom_emoji_regras_id, name=name_custom_emoji_regras)
	))
    view_boas_vindas.add_item(discord.ui.Button(
		label="suporte",
		style=discord.ButtonStyle.link,
		url=channel_3_link,
		emoji=discord.PartialEmoji(animated=True, id=custom_emoji_suporte_id, name=name_custom_emoji_suporte)
	))
    
    await channel.send(f'||{member.mention}||', embeds=[embed_bem_vindo1, embed_bem_vindo2], view=view_boas_vindas), await member.add_roles(role)
    

print('(READY) EVENT: ON_MEMBER_JOIN()')

#@bot.event
# Caso um membro sair do servidor
#async def on_member_remove(member):
#    channel = member.guild.system_channel
#    await channel.send(f'{member.mention} Até logo operador!')
#print('(READY) EVENT: ON_MEMBER_REMOVE()')
    
#@bot.event
# Filtro de palavras enviadas pelos usuários, retorna uma resposta.
#async def on_message(message):
    #if message.content.startswith('/') or message.content.startswith('$'):
    #    return # ignora a mensagem
    #else:
        #not_allowed_content = ['comprar', 'vender', 'trocar']
        # print(f"(FILTER) Verificando Mensagem Recebida: {message.content}") # demonstra no OUTPUT do console as mensagens que o bot identifica, vulgo TODAS do chat do DISCORD. (não tirar hashtag 30NOV23)
        #if message.author == bot.user:  # Evita responder a si mesmo
            #return "tentei responder a mim mesmo"

        # Caso alguma palavra do filtro seja enviada, devolve uma mensagem.
        #if any(word in message.content.lower() for word in not_allowed_content):
        #    channel = message.channel
        #    await channel.send(f'Isso não é permitido aqui. {message.author.mention} Utilize nosso site oficial: [Google](https://www.google.com.br)') # Não esquecer do "https://"
        #await bot.process_commands(message) # Não retirar esta linha de comando, pois o bot PARA de identificar outros comandos ctx.
#print('(READY) - EVENT: ON_MESSAGE FILTER')
    
# Task de contador de membros
@tasks.loop(seconds=300)  # Atualiza a cada 5 minutos (altere conforme necessário)
async def update_member_count():
    counter_channel = 1185023932856795137 # ID do canal para colocar o contador
    guild = bot.get_guild(id_do_servidor) # ID do servidor atual
    channel = guild.get_channel(counter_channel) 
    members = [member for member in guild.members if not member.bot]
    
    if guild and channel:
        # member_count = guild.member_count (inserido após "Membros:" abaixo)
        member_count = len(members)
        await channel.edit(name=f"🟠 Operadores: {member_count}")
    print('(UPDATED) UPDATE_MEMBER_COUNT TASK')

# ---------------------------CTX COMMANDS--------------------------------------
# Evento de notificar mensagem em canal de anúncio
@bot.event
async def on_message(message):
    external_announcement_channel_ID = 1185263617118048318 # Canal de anúncios que vem de outro servidor/canal
    
    if message.channel.id == external_announcement_channel_ID: # Verifique se a mensagem foi enviada no canal de anúncios
        
        if message.author != bot.user: # Verifique se o autor da mensagem não é o bot para evitar loops
            internal_announcement_channel_ID = 1185268713570709714 # ID do canal para colocar o anuncio
            bot_id = 1179899864998490202 # ID DO BOT
            bot_role = 1185267818510434384 # ID do cargo do BOT
            
            guild = bot.get_guild(id_do_servidor) # ID do servidor atual
            
            internal_channel = guild.get_channel(internal_announcement_channel_ID) # Define o canal interno para divulgação
            
            member = [member for member in guild.members if member.id == bot_id] # procura o bot no servidor comparando o ID
            
            if member: 
                member = member[0] # Se o bot existir extrai a informação dele
                
                roles = [role for role in member.roles] # Verifique se o membro (BOT) tem o cargo específico
                mention_role = [role.mention for role in roles if role.id == bot_role] # Caso o cargo existir, mencione ele
                
                # Notifique no canal de anúncios mencionando o cargo
                await notificar_canal_com_cargo(internal_channel, mention_role[0], message) # execute a função que notifica o cargo no canal correto

    await bot.process_commands(message)

async def notificar_canal_com_cargo(canal_de_anuncio, cargo_alvo, mensagem):
    # Envia uma mensagem mencionando o cargo alvo
    await canal_de_anuncio.send(f"> Viciados em **{cargo_alvo}**!\n> **Anúncio do __Ready or Not__ no ar!**\n> {mensagem.jump_url}")


# ---------------------ENCERRADO-CTX COMMANDS----------------------------------

# Retorna a data e hora atual em formato TIMESTAMP do discord
def discord_timestamp_now():
    timestamp_now = round(datetime.now().timestamp())
    return timestamp_now

# Retorna a data e hora atual conforme desejado
def data_hora():
    agora = datetime.now()
    data = agora.date()
    hora = agora.hour
    minuto = agora.minute
    segundo = round(agora.second, 2)
    dia = agora.day
    mes = agora.month
    ano = agora.year
    
    return f"{dia}/{mes}/{ano} {hora}:{minuto}:{segundo}"

### Cria o protocolo de tickets:
# Obter a data atual voltado para os tickets
def data_atual():
    data_atual = datetime.now()

    # Formatar a data sem traços
    data_formatada = data_atual.strftime(f"%d%m%Y")

    # Retornar a data formatada
    return data_formatada

# Conta os tickets criados por dia
contagem = 0
def contador():
    global contagem # Permite modificar a variável global
       
    # Define a data do contador
    data_atual_contador = data_atual()
    
    # Compara com a data formatada da função, caso seja diferente, retorna o número "1".
    if data_atual_contador != data_atual():
        contagem = 1
    else:
        contagem += 1
    return contagem

# Cria o protocolo de ticket "data_atual() + contador()" em formato string
def id_ticket():
    if contagem < 10:
        retorno_id_ticket = data_atual() + "00" + str(contador())
    elif contagem < 100:
        retorno_id_ticket = data_atual() + "0" + str(contador())
    else:
        retorno_id_ticket = data_atual() + str(contador())
    return retorno_id_ticket
### Encerrado o protocolo de Tickets

# Cria as opções do setup e a área de seleção
class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(value="atendimento",label="Atendimento", emoji="📨"),
            discord.SelectOption(value="comandos",label="Comandos", emoji="♻"),
            discord.SelectOption(value="staff", label="Me inscrever na Staff", emoji="✍")
            #discord.SelectOption(value="sorteio",label="Sorteio", emoji="🍀"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )
    async def callback(self, interaction: discord.Interaction):
        # Retorna um Embed dos comandos do bot que exigem slash
        if self.values[0] == "comandos":
                      
            embed = discord.Embed(
            title = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   Lista de Comandos',
            description = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀**OpEsp ROLEPLAY!**',
            colour = discord.Colour.dark_orange(),
            timestamp=interaction.message.created_at
            )

            embed.set_author(name='Corregedoria', icon_url='https://cdn.discordapp.com/attachments/1185031046228627546/1185031089815826462/OPESP_ICON.jpeg?ex=658e2134&is=657bac34&hm=2b0e5cc3b3b06b4606109ebe8817f7a8b492baf40223c5bcb0202fdabb6b957a&')

            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')    

            
            #embed.add_field(name='**⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   Qual minha finalidade?**', value=f"Olá, Meu propósito é aprimorar a atuação dos moderadores e poder melhor atender você!Dentre as minhas funções posso listar:\n> ✍Verifico membros;\n> 🛠Possuo Ferramentas de moderação;\n> 📝Atribuição de Cargos;\n> 📋Automatizo tarefas; e\n> 📕Atribuo Avisos e Punições aos operadores;\n\nSe tiver alguma dúvida ou precisar de ajuda não hesite em abrir um atendimento!")

            embed.add_field(name='**⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   Comandos do operador:**', value='', inline=False)
            embed.add_field(name='**/verificar**', value='Novos membros utilizam para acessar o servidor.', inline=False)            
            embed.add_field(name='**/progresso**', value='Mostra as patentes alcançadas e pontos do operador.', inline=False)
            embed.add_field(name='**/opd**', value='Mostra a **operação do DIA** - **12%** de pontos a mais no relatório.', inline=False)
            embed.add_field(name='**/ops**', value='Mostra a **operação da SEMANA** - **20%** de pontos a mais no relatório.', inline=False)
            embed.add_field(name='**/relatorio**', value='Anexe a imagem de pontos da operação, insira a pontuação da missão e digite o nome dos operadores.\n- Caso seja uma **operação especial** do tipo "**diário**", "**semanal**" ou "**oficial**" **apenas insira o parâmetro opcional "operacao_especial" do comando e digite** "diário" se for diário, "semanal" se for semanal ou "oficial" caso seja oficial.\n- **Operação OFICIAL** Utilize os parâmetros opcionais\n> "**MVP**": para mencionar o operador que se destacou na operação; e\n> "**civil_atingido**": Especifique com "time" dentro do comando caso o time tenha atingido um civil ou mencione um operador para delatar à Corregedoria que ele atingiu um civil.', inline=False)
            embed.add_field(name='**/registrarsteam**', value='Registra o STEAM ID do membro.', inline=False)
            embed.add_field(name='**/steamid**', value='Mostra seu STEAM ID para todos.', inline=False)
            embed.add_field(name='**!convite**', value='Envia um link de convite permanente para você convidar seus amigos para o servidor.', inline=False)
                        
            embed.add_field(name='**\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   Comandos da STAFF**', value='', inline=False) 
            embed.add_field(name='**/atstamp**', value='Retorna um timestamp de uma data-hora quando inserido o formato DD/MM/AAAAhh:mm', inline=False)
            embed.add_field(name='**/atimestamp**', value='Retorna o timestamp atual.', inline=False)
            embed.add_field(name='**/ban**', value='BANIR um membro do servidor.', inline=False)
            embed.add_field(name='**/kick**', value='KICKAR um membro do servidor.', inline=False)
            embed.add_field(name='**/addrole**', value='adiciona um cargo ao membro, exemplo: /addrole @Moderador @Menotso.', inline=False)
            embed.add_field(name='**/removerole**', value='remove um cargo ao membro, exemplo: /addrole @Moderador @Menotso.', inline=False)
            embed.add_field(name='**/reloadcogfile**', value='Recarrega um arquivo COG.', inline=False)
            embed.add_field(name='**/verificapontos**', value='Verifica os pontos atuais de um operador com base no ID dele', inline=False)
            embed.add_field(name='**/alterapontos**', value='Altera os pontos de um operador com base no ID dele', inline=False)
            #embed.add_field(name='**/sorteio**', value='(Em desenvolvimento)', inline=False)
            embed.add_field(name='**/backup_points**', value='Faz um back-up dos PONTOS de todos os operadores.', inline=False)
            embed.add_field(name='**/backup_steamid**', value='Faz um back-up do STEAM ID de todos os operadores..', inline=False)
            embed.add_field(name='**!sync**', value='Sincroniza todos os comandos do BOT com o servidor do DISCORD.', inline=False)
            embed.add_field(name='**!clear**', value='Deleta um número específico de mensagens, exemplo: "!clear 10" deleta 10 mensagens.', inline=False)
            #embed.add_field(name='**!regras**', value='Envia o Embed de regras do servidor. (Em desenvolvimento)', inline=False)
            embed.add_field(name='**!reactionrole**', value='Envia o Embed de cargo por reações.', inline=False)
            embed.add_field(name='**!userinfo @membro**', value='Retorna informações do membro.', inline=False)

            embed.set_footer(text='OpEsp ROLEPLAY. Todos os direitos Reservados.', icon_url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')

            await interaction.response.send_message(embed = embed, ephemeral=True)

        # Retorna uma mensagem particular para criar ticket    
        elif self.values[0] == "atendimento":
            await interaction.response.send_message("🔽 Clique abaixo para criar um ticket\n || Caso não consiga criar, selecione 'Atendimento' novamente para reabrir esta mensagem.||",ephemeral=True,view=CreateTicket(), delete_after=60)
        
        # [ASD] Será implementado um redirecionamento para os sorteios
        #elif self.values[0] == "sorteio":
            #await interaction.response.send_message("🍀 Ainda será implementado...",ephemeral=True, delete_after=10)
        elif self.values[0] == "staff":
            staff_modal = Staff_Modal_UI()
            await interaction.response.send_modal(staff_modal)
            
# Inserir a descrição de DropdownView
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())

# Todo o processo de abertura/fechamento de ticket
class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    @discord.ui.button(label="Abrir Ticket",style=discord.ButtonStyle.grey,emoji="➕")
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                # Caso o objetivo seja reabrir o mesmo tópico para utilizar como outras threads do mesmo usuário inserir "Thread" após a variável ticket.
                    ticket = None
                else:
                    await interaction.response.send_message(ephemeral=True,content=f"✉ Você já possui um atendimento em andamento!", delete_after=25)
                    return

        async for thread in interaction.channel.archived_threads(private=True):
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                # Caso o objetivo seja reabrir o mesmo tópico para utilizar como outras threads do mesmo usuário inserir "Thread" após a variável ticket.
                    ticket = None
                else:
                    await interaction.edit_original_response(content=f"✉ Você já possui um atendimento em andamento!", view=None, delete_after=25)
                    return
        
        if ticket != None:
            await ticket.edit(archived=False,locked=False)
            await ticket.edit(name=f"✉ {interaction.user.name} ({id_ticket()})) ID: ({interaction.user.id})",auto_archive_duration=None,invitable=False)
        else:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({id_ticket()})",auto_archive_duration=None)#,type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True,content=f"📨 Criei um ticket para você! {ticket.mention}\n - Tickets sem resposta por mais de 24 horas serão fechados.", delete_after=40)
        await ticket.send(f"📩  **|** {interaction.user.mention} ID: ({interaction.user.id}) {(interaction.guild.get_role(1114290574678310914).mention)} Ticket criado!\n\n Envie todas as informações possíveis sobre seu caso e aguarde até que a administração responda.\n\nApós a sua questão ser sanada, você pode encerrar o atendimento!")
        await ticket.send(view=Fecharticket())
        
import discord

# Cria o botão de fechar ticket
class Fecharticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        self.fechou_ticket = False  # Adiciona a variável de controle

    @discord.ui.button(label="Fechar Ticket", style=discord.ButtonStyle.red, emoji='❌')
    async def botao_fecharticket(self, interaction: discord.Interaction, button: discord.ui.Button, custom_id='fecharticket'):
        # Verifica se o ticket já foi fechado
        if self.fechou_ticket:
            await interaction.response.send_message("❌ Este ticket já foi fechado anteriormente.", ephemeral=True, delete_after=20)
            return

        mod = interaction.guild.get_role(id_cargo_atendente)
        if str(interaction.user.name) in interaction.channel.name or mod in interaction.author.roles:
            await interaction.response.send_message(f"💌 O ticket foi arquivado por {interaction.user.mention}, obrigado por entrar em contato!")
            await interaction.channel.edit(archived=True, locked=True)
            self.fechou_ticket = True  # Define a variável como True após o fechamento
        else:
            await interaction.response.send_message("❌ Isso não pode ser feito aqui...", ephemeral=True, delete_after=20)

            
print('(READY) - TICKET THREAD')

# ------------------------------------------------Comandos SLASH------------------------------------------------
# Painel Geral do bot "/setup"
@bot.tree.command(name = 'setup', description='Setup')
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def setup(interaction: discord.Interaction):
    support_image_embed = discord.Embed(color=discord.Colour.dark_orange())
    support_image_embed.set_image(url='https://media.discordapp.net/attachments/1032063754843738202/1185249699024875560/GIF_SUPORTE.gif?ex=658eeccd&is=657c77cd&hm=40e21fde908391628f523cd5adb0cbd1191445c229c2c170778e70d55f81ff62&=&width=687&height=250')

    await interaction.response.send_message(embed=support_image_embed, view=DropdownView()) 

# Verifica membros atribuindo um cargo utilizando um captcha enviado na DM@bot.tree.command(name='verificar', description='Seja verificado e tenha acesso ao servidor.')
@bot.tree.command(name='verificar', description='Seja verificado e tenha acesso ao servidor.')
async def verificar(ctx):

    image = ImageCaptcha(width=280, height=90)
    
    captcha_text = random.randint(100000, 999999)

    captcha_text = str(captcha_text)
    data = image.generate(captcha_text)
    
    image.write(captcha_text, 'captcha/CAPTCHA.png')

    sender = ctx.user
    attach_role1 = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   PATENTE ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
    attach_role2 = 'Recruta'
    attach_role3 = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ CERTIFICAÇÕES⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
    attach_role4 = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ CONDECORAÇÕES⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀' # Nome dos CARGOS que serão atribuídos ao membro
    attach_role5 = '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ EXTRAS⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
    role_has = discord.utils.get(ctx.guild.roles, name=attach_role1) # Verifica se o membro já possui o cargo
    
    if role_has in ctx.user.roles:
        await ctx.response.send_message('✅ **Você já foi verificado!**', ephemeral=True)
            
    else:      
        await ctx.response.send_message('Te enviei uma mensagem no privado!', ephemeral=True, delete_after=45)

        while True:
        
            await sender.send('✍ Escreva o que está no CAPTCHA!', file=discord.File('captcha/CAPTCHA.png'))
            print(captcha_text)
            
            try:
                msg = await bot.wait_for('message', check=lambda check: check.author == sender, timeout=120)
                
                if msg.content == captcha_text:
                    await sender.send('✅ Correto! Você está verificado.\n\nAgora você faz parte da **OpEsp ROLEPLAY**, o roleplay mais imersivo para àqueles que desejam sentir na pele o realismo dos Operadores Especiais!\n\nAcesse o canal de <#1185233979570389063> para informações de como o servidor funciona;\nAcesse a aba de adestramento e faça nosso primeiro curso introdutório: <#1185264572458872903>')

                    role_append1 = discord.utils.get(ctx.guild.roles, name=attach_role1)
                    await sender.add_roles(role_append1)

                    role_append2 = discord.utils.get(ctx.guild.roles, name=attach_role2)
                    await sender.add_roles(role_append2)

                    role_append3 = discord.utils.get(ctx.guild.roles, name=attach_role3)
                    await sender.add_roles(role_append3)

                    role_append4 = discord.utils.get(ctx.guild.roles, name=attach_role4)
                    await sender.add_roles(role_append4)
                    
                    role_append5 = discord.utils.get(ctx.guild.roles, name=attach_role5)
                    await sender.add_roles(role_append5)

                    role_removal = discord.utils.get(ctx.guild.roles, name='Verificação Pendente')
                    await sender.remove_roles(role_removal)
                    
                    break  # Exit the loop if verification is successful
                else:
                    await sender.send('❌ Incorreto! Tente novamente.')
            
            except asyncio.TimeoutError:
                await sender.send('❌ Tempo limite atingido. Tente novamente mais tarde.')
                break  # Exit the loop if timeout occurs


            


# Modal de sugestão que será mostrado ao usuário após utilizar o comando /suggest

class Staff_Modal_UI(discord.ui.Modal, title='Registre sua aplicação para Staff'):
    staffapp_name = ui.TextInput(style=discord.TextStyle.short,
                            label='QUAL É SEU NOME REAL? E DO STEAM?',
                            required=True,
                            placeholder="📋 Digite seu nome real e o do Steam também",
                            
                            )
    staffapp_aboutme = ui.TextInput(style=discord.TextStyle.paragraph,
                            label='FALE UM POUCO SOBRE VOCÊ:',
                            required=True,
                            max_length=1000,
                            placeholder="✍ Horário disponível, Idade, Educação, Estilo de Vida, Emprego, Hobbies, Motivações, Metas",
                        
                        )
    staffapp_motivation = ui.TextInput(style=discord.TextStyle.paragraph,
                            label='SUAS MOTIVAÇÕES:',
                            required=True,
                            max_length=500,
                            placeholder="✍ Como você pode contribuir para a OpEsp - Roleplay?",
                            
                            ) 
    staffapp_dif = ui.TextInput(style=discord.TextStyle.paragraph,
                            label='Diferencial:',
                            required=True,
                            max_length=800,
                            placeholder="✍ Qual é o seu propósito ao se candidatar para a função?",
                            
                            )   
    staffapp_role_requirements = ui.TextInput(style=discord.TextStyle.paragraph,
                            label='Qual Cargo e Cumpre Requisitos?',
                            required=True,
                            max_length=450,
                            placeholder="✍ Cargo que está aplicando e informe se cumpre todos os requisitos (sim/não/quais)",
                            
                            )    
    
    # Quando o usuário completar o MODAL de SUGESTÃO será executado isto
    async def on_submit(self, interaction: discord.Interaction):        
        name_value = self.staffapp_name.value
        aboutme_value = self.staffapp_aboutme.value
        motivation_value = self.staffapp_motivation.value
        dif_value = self.staffapp_dif.value
        role_requirements_value = self.staffapp_role_requirements.value
        
        embed = discord.Embed(title=f'Aplicação para Staff',
                              description=f'**Nome Real/Steam:**\n {name_value}\n\n**\nSobre mim:**\n {aboutme_value}\n\n**Motivação:**\n {motivation_value}\n\n**Diferencial:**\n {dif_value}\n\n**Cargo e Requisitos:**\n {role_requirements_value}',
                              color=discord.Color.yellow())
        embed.set_author(name=interaction.user.name + f' (ID: {interaction.user.id})', icon_url=interaction.user.avatar)
        embed.add_field(name='\n📅 Data-Hora:', value=f'<t:{discord_timestamp_now()}:F>', inline=False)
        # await channel.send(embed=embed)
        
        # Envia o embed para o canal de feedback
        feedback_channel_id = 1114290575156465686
        feedback_channel = interaction.guild.get_channel(feedback_channel_id)
        await feedback_channel.send(embed=embed)

        # Cria um tópico com o nome e id do usuário no canal específico
        topic_name = f"{interaction.user.name} (ID: {interaction.user.id})"
        user_topic_channel = await feedback_channel.create_thread(name=topic_name, auto_archive_duration=None)
        
        # Envia o mesmo embed para o tópico criado
        # ID do cargo específico que você deseja mencionar
        cargo_id = 1114290574678310914 # cargo que será mencionado no THREAD
        # Obtém o objeto de cargo usando o ID
        cargo = interaction.guild.get_role(cargo_id)
        
        await user_topic_channel.send(f'||{cargo.mention}||', embed=embed)
        
        await interaction.response.send_message(f'Obrigado pela aplicação, {interaction.user.mention}. A Staff analisará cuidadosamente sua inscrição e retornará na sua mensagem privada com o resultado. Pedimos que não fique perguntando sobre o andamento do processo.', ephemeral=True, delete_after=45)

# Comando de Ping-Pong
@bot.tree.command(name="ping",description='Jogue Ping-Pong com o Bot!')
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("**Pong**\n https://tenor.com/view/%E4%B9%92%E4%B9%93-ping-pong-table-tennis-funny-table-tennis-funny-gif-12978619")

print('(READY) - SLASH "/COMMANDS"')            
# -------------------------------------Encerrado-Comandos SLASH-----------------------------------------

# Starta o bot:
bot.run(token_bot)