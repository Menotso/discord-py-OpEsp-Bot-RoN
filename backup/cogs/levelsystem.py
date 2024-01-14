import discord
from discord import app_commands
from discord.ext import commands, tasks
import datetime
from discord import Button, ButtonStyle
import asyncio
import random
import re
import json

class AprovarRecusar(discord.ui.View):
    def __init__(self, bot, required_role): 
        super().__init__(timeout=None)
        self.bot = bot
        self.value = None
        self.required_role = required_role
        self.approver = None # Adiciona um atributo para armazenar o aprovador
        
    async def has_required_role(self, user):
        return self.required_role in user.roles
    
    @discord.ui.button(label="Aprovar", style=discord.ButtonStyle.green, custom_id="approve")
    async def approve_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Verifica se o usuário possui o cargo necessário
        if not await self.has_required_role(interaction.user):
            await interaction.response.send_message("> Você **NÃO** tem permissão para **APROVAR** este relatório.\n> **Aguarde alguém autorizado.**", ephemeral=True, delete_after=20)
            return
        
        self.value = "approve"
        self.approver = interaction.user  # Armazena o aprovador
        self.stop()

    @discord.ui.button(label="Recusar", style=discord.ButtonStyle.red, custom_id="reject")
    async def reject_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Verifica se o usuário possui o cargo necessário
        if not await self.has_required_role(interaction.user):
            await interaction.response.send_message("> Você **NÃO** tem permissão para **RECUSAR** este relatório.\n> **Aguarde alguém autorizado.**", ephemeral=True, delete_after=20)
            return
        
        self.value = "reject"
        self.approver = interaction.user  # Armazena o aprovador
        self.stop()
        
    async def on_timeout(self):
        print("(ERROR) A interação atingiu o tempo limite.")
        self.stop()
        self.start()
        # Você pode adicionar ações específicas aqui, se necessário

    async def on_error(self, interaction, error, item):
        print(f"(ERROR) Erro durante a interação: {error}")
        self.stop()
        self.start()
        # Você pode adicionar ações específicas aqui, se necessário
        
    # Adiciona um método para obter o nome do aprovador
    def get_approver_name(self):
        return self.approver.name if self.approver else "Nenhum"
        
    @commands.Cog.listener()
    async def on_ready(self, member):
        print('(READY) - COG: cogs.levelsystem: Aprovar')
        print('(READY) - COG: cogs.levelsystem: Recusar')
        print('(READY) - [LevelSystem.py] COG: cogs.levelsystem: /relatorio')
        print('(READY) - [LevelSystem.py] COG: cogs.levelsystem: /backup')
        print('(READY) - [LevelSystem.py] COG: cogs.levelsystem: /alterapontos')
        print('(READY) - [LevelSystem.py] COG: cogs.levelsystem: /verificapontos')
    
    """# Check if the member's ID is in the user_points dictionary
        user_id = member.id
        if user_id in self.user_points:
            # Remove the member's points from the dictionary
            del self.user_points[user_id]
            await self.save_data()  # Save the changes to the data file"""
    
    async def on_button_click(self, interaction: discord.Interaction, button: discord.ui.Button, user: discord.User):
        if isinstance(button.view, AprovarRecusar):
            if button.custom_id == 'approve':
                await button.view.approve_button_callback(interaction, button)
            elif button.custom_id == 'reject':
                await button.view.reject_button_callback(interaction, button)
        
    

class levelsystem(commands.Cog):
    async def load_data(self):
        try:
            with open("levelsystem_database.json", "r") as f:
                data = json.load(f)

            self.user_points = {int(user_id): points for user_id, points in data["user_points"].items()} #data.get("user_points", {})
            self.user_activity = data.get("user_activity", {})
            self.last_report_time = {int(user_id): datetime.datetime.fromisoformat(timestamp) for user_id, timestamp in data.get("last_report_time", {}).items()}
            self.tasklist_pontos_acrescidos = data.get("tasklist_pontos_acrescidos", [])
            self.tasklist_pontos_resetados = data.get("tasklist_pontos_resetados", [])
            self.rank_data = data.get("rank_data", [])
        except FileNotFoundError:
            # Se o arquivo não existe, inicializa as variáveis como vazias
            self.user_points = {}
            self.user_activity = {}
            self.last_report_time = {}
            self.tasklist_pontos_acrescidos = []
            self.tasklist_pontos_resetados = []
            self.rank_data = []

    async def save_data(self):
        # Crie um dicionário com os dados a serem salvos
        data = {
            "user_points": self.user_points,
            "user_activity": self.user_activity,
            "last_report_time": {str(user_id): str(timestamp) for user_id, timestamp in self.last_report_time.items()}, #self.last_report_time,
            "tasklist_pontos_acrescidos": self.tasklist_pontos_acrescidos,
            "tasklist_pontos_resetados": self.tasklist_pontos_resetados,
            "rank_data": self.rank_data
        }
    
        # Converter objetos datetime para strings
        for user_id, timestamp in self.last_report_time.items():
            if isinstance(timestamp, type(datetime)):
                data["last_report_time"][str(user_id)] = timestamp.isoformat()
    
        with open("levelsystem_database.json", "w") as f:
            json.dump(data, f, indent=4)
    
    def __init__(self, bot):
        self.bot = bot
        self.required_role_id = 1114290574678310914
        self.user_points = {}  # Dicionário para armazenar os pontos dos usuários
        self.user_activity = {}
        self.last_report_time = {}
        self.tasklist_pontos_acrescidos = []
        self.tasklist_pontos_resetados = []
        self.rank_data = []  # Variável para armazenar os dados do ranking"""

        
            # cargos
        recruta = 1114290574644760690
        soldado = 1114290574644760691
        cabo = 1114290574644760692
        terceiro_sg = 1114290574644760693
        segundo_sg = 1114290574644760694
        primeiro_sg = 1114290574644760695
        sub_tenente = 1114290574644760696
        segundo_tenente = 1114290574661521468
        primeiro_tenente = 1114290574661521469
        capitao = 1114290574661521470
        major = 1114290574661521471
        tenente_coronel = 1114290574661521472
        coronel = 1114290574661521473
        
        # Pontuações para cada cargo
        self.progression_roles = [
            {"role_id": recruta, "points_required": 0},
            {"role_id": soldado, "points_required": 8000},
            {"role_id": cabo, "points_required": 16000},
            {"role_id": terceiro_sg, "points_required": 35000},
            {"role_id": segundo_sg, "points_required": 49000},
            {"role_id": primeiro_sg, "points_required": 65000},
            {"role_id": sub_tenente, "points_required": 86000},
            {"role_id": segundo_tenente, "points_required": 104000},
            {"role_id": primeiro_tenente, "points_required": 125000},
            {"role_id": capitao, "points_required": 150000},
            {"role_id": major, "points_required": 177000},
            {"role_id": tenente_coronel, "points_required": 207000},
            {"role_id": coronel, "points_required": 240000},
        ]
        
    async def has_required_role(self, user_id):
        user = await self.bot.fetch_user(user_id)
        return self.required_role_id in [role.id for role in user.roles]    

                  
    async def update_roles(self, member):
        # Obtém o cargo de Recruta
        recruta_role_id = 1114290574644760690
        recruta_role = member.guild.get_role(recruta_role_id)

        # Remove o cargo de Recruta se estiver presente
        if recruta_role in member.roles:
            await member.remove_roles(recruta_role)

        # Obtém o cargo atual do membro após remover o cargo de Recruta
        current_roles = set(role.id for role in member.roles)

        # Remove o cargo da patente anterior
        for role_info in self.progression_roles[1:]:
            if role_info["role_id"] in current_roles:
                cargo_anterior_id = role_info["role_id"]
                cargo_anterior = member.guild.get_role(cargo_anterior_id)
                await member.remove_roles(cargo_anterior)
                break

        # Adiciona o novo cargo com base nos pontos
        for role_info in reversed(self.progression_roles):
            if self.user_points[member.id] >= role_info["points_required"]:
                novo_cargo = member.guild.get_role(role_info["role_id"])
                if novo_cargo:
                    await member.add_roles(novo_cargo)
                break
    
    # Comando de RELATÓRIO
    @app_commands.command(
        name="relatorio",
        description="Envie um relatório com uma IMAGEM, a PONTUAÇÃO da operação e os OPERADORES envolvidos."
    )
    async def relatorio(self,
                        interaction: discord.Interaction,
                        attachment: discord.Attachment,
                        pontuacao: int,
                        operadores: str,
                        operacao_especial: str = None,
                        mvp: discord.Member = None,  # New parameter for MVP
                        civil_atingido: str = None):
        
        await self.load_data()
        pontuacao_final = pontuacao
        operacao_especial = operacao_especial.lower()
        #civil_atingido = civil_atingido.lower()
        
        # Transformação da pontuação para cada tipo de operação
        if operacao_especial == 'diario' or operacao_especial == 'diário' or operacao_especial == 'dia' or operacao_especial == 'diaria' or operacao_especial == 'diária' or operacao_especial == 'opd':
            pontuacao_final *= 1.12
        elif operacao_especial == 'semanal' or operacao_especial == 'ops':
            pontuacao_final *= 1.20
        elif operacao_especial == 'oficial' or operacao_especial == 'opof' or operacao_especial == 'opf':
            pontuacao_final *= 1.30
                
        if civil_atingido and operacao_especial not in ['opof', 'opf', 'oficial']:
            await interaction.response.send_message('civil_atingido só pode ser utilizado em operação OFICIAL.', ephemeral=True)
        if mvp and operacao_especial not in ['opof', 'opf', 'oficial']:
            await interaction.response.send_message('MVP só pode ser utilizado em operação OFICIAL.', ephemeral=True)

        
        # Verifica se o comando foi usado no canal correto
        canal_relatorio = 1185771784591642716
        if  interaction.channel.id != canal_relatorio:  # Substitua pelo ID do canal desejado
            await interaction.response.send_message("❌**ERRO!** Este comando só pode ser usado no tópico: <#1185771784591642716>.", ephemeral=True)
            return
        
        operadores_list = []
        for member_name in operadores.split(', '):
            # Dentro do loop for member_name in operadores.split():
            try:
                #member_name = member_name.lstrip('@')
                member_name = re.sub(r'<@!|<@|>', '', member_name)
                member = interaction.guild.get_member_named(member_name)
                if member:
                    operadores_list.append(member)
                else:
                    await interaction.user.send(f"Não foi possível encontrar o membro para: {member_name}")
            except Exception as e:
                await interaction.user.send(f"Erro ao processar o membro {member_name}: {e}")
        print(f'\n\n[LevelSystem.py] Lista de operadores:\n{operadores_list}')

        if operadores:
            # Adiciona os IDs dos membros mencionados à lista de pontos
            for member in operadores_list:                
                if member.id not in self.user_points:
                    self.user_points[member.id] = 0
            print('[LevelSystem.py] Adicionando operadores na lista de pontos')
        else:
            user_id = interaction.user.id
            # Inicializa os pontos do usuário se ainda não existirem
            if user_id not in self.user_points:
                self.user_points[user_id] = 0
            print('[LevelSystem.py] Adicionando UM operador na lista de pontos')

        # Cria um ID de relatório de 10 dígitos aleatórios
        report_id = ''.join(random.choices('0123456789', k=13))
        
        # Cria o embed original
        embed = discord.Embed(title=f"⠀⠀⠀   Relatório de Operador\n⠀⠀⠀   (ID: {report_id})", color=discord.Colour.dark_orange())
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.add_field(name="Relator", value=interaction.user.mention, inline=False)
        
        # Adiciona os membros mencionados
        if operadores:
            mention_str = '\n'.join([member.mention for member in operadores_list])
            embed.add_field(name="Operadores:", value=mention_str, inline=False)
        else:
            await interaction.user.send("Nenhum membro válido encontrado com este nome.")
        print('[LevelSystem.py] Operadores mencionados no embed')
        
        if not operacao_especial:
            embed.add_field(name="Pontuação", value=str(pontuacao), inline=True)
            
        elif operacao_especial == 'diario' or operacao_especial == 'diário' or operacao_especial == 'dia' or operacao_especial == 'diaria' or operacao_especial == 'diária' or operacao_especial == 'opd':
            embed.add_field(name="Pontuação", value=f'**OPD:** (+12%)\n{str(round(pontuacao_final))}', inline=True)
            
        elif operacao_especial == 'semanal' or operacao_especial == 'ops' or operacao_especial == 'semana':
            embed.add_field(name="Pontuação", value=f'**OPS:** (+20%)\n{str(round(pontuacao_final))}', inline=True)
            
        elif operacao_especial == 'oficial' or operacao_especial == 'opof' or operacao_especial == 'opf':
            embed.add_field(name="Pontuação", value=f'**OPOF:** (+30%)\n{str(round(pontuacao_final))}', inline=True)
        else:
            embed.add_field(name="Pontuação", value=str(pontuacao), inline=True)
        

        if operacao_especial:   
                # Em caso de MVP em operação OFICIAL
                embed.add_field(name='MVP:', value=f'- **{mvp.display_name}** (**5%** a mais de pontos: **{int(pontuacao_final*1.05)}**)', inline=False)                

                # Em caso de civil morto em OPERAÇÃO OFICIAL:
                if civil_atingido in ["equipe", "time", "e", "t", "grupo", "operadores", "agentes", "membros"]:
                    embed.add_field(name='- Houve registro de civil atingido?', value=f'**A Equipe** atingiu um civil. __Penalidade de pontuação do time__: **-200**. ({pontuacao_final - 200})', inline=False)
                    
                elif civil_atingido.startswith('<@') and civil_atingido.endswith('>'):
                    member_id_str = civil_atingido[2:-1]
                    if member_id_str.isdigit():
                        member_id = int(member_id_str)  # Obtém o ID do membro da menção
                        member = interaction.guild.get_member(member_id)
                        if member:
                            embed.add_field(name="Houve registro de civil atingido?", value=f"- **{member.display_name}** atingiu um civil! __Penalidade de pontuação individual:__ **-1000**.", inline=False)
                        else:
                            embed.add_field(name="Houve registro de civil atingido?", value=f"- Membro não encontrado com ID: {member_id}", inline=False)
                    else:
                        embed.add_field(name="Houve registro de civil atingido?", value="- ID do membro inválido na menção.", inline=False)
                elif not civil_atingido:
                    embed.add_field(name='', value='- Sem ocorrência de civis atingidos.', inline=False)
                else:
                    embed.add_field(name='', value='- Sem ocorrência de civis atingidos.', inline=False)
        
        
        embed.set_image(url=attachment)
        embed.set_footer(text=f"⏳ Relatório em Análise. Enviado por {interaction.user.name}.\n\nOpEsp ROLEPLAY. Todos os direitos reservados.")             
        
        # No momento de instanciar a view, passe o objeto de cargo diretamente
        #cargo_avaliador_relatorios = 1114290574678310914
        required_role=interaction.guild.get_role(self.required_role_id)
        view = AprovarRecusar(bot=self.bot, required_role=required_role)
        
        message = await interaction.response.send_message(embed=embed, view=view)
        print('[LevelSystem.py] Embed enviado pela primeira vez.')
        
        try:
            await view.wait()
        except asyncio.TimeoutError:
            print('(ERROR) [LevelSystem.py] Tempo do relatório esgotado. asyncio.TimeoutError.')
            await message.edit(embed=embed, view=view)
            await view.wait()
        
        # Modifica o embed original com base na escolha do usuário
        if view.value == "approve":
            if operacao_especial:
                    
                # Em caso de MVP em operação OFICIAL
                self.user_points[mvp.id] += pontuacao_final * 0.05
                

                # Em caso de civil morto em OPERAÇÃO OFICIAL:
                if civil_atingido.startswith('<@') and civil_atingido.endswith('>'):
                    member_id_str = civil_atingido[2:-1]
                    if member_id_str.isdigit():
                        member_id = int(member_id_str)  # Obtém o ID do membro da menção
                        member = interaction.guild.get_member(member_id)
                    self.user_points[member_id] -= 1000  # Deduzir 1000 pontos do operador mencionado por matar civil.
                                            
                elif civil_atingido in ["equipe", "time", "e", "t", "grupo", "operadores", "agentes", "membros"]:
                    
                    pontuacao_final -= 200  # Deduct 200 points for the whole team if a civilian is killed
            
            print('[LevelSystem.py] Iniciando aprovação de Embed')
            embed.add_field(name='Análise:', value='APROVADO', inline=True)
            
            approver_mention = view.approver.mention if view.approver else "Nenhum"
            # Adiciona o aprovador ao embed
            # approver_name = view.get_approver_name()
            embed.add_field(name="Analista:", value=approver_mention, inline=True)
            
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')    
            embed.set_footer(text=f"\n✅ A CORREGEDORIA APROVOU em {datetime.datetime.now().strftime('%d-%m-%Y')}.\n\nOpEsp ROLEPLAY. Todos os direitos reservados.") #icon_url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')
            embed.title = f"⠀⠀⠀ 🟢 RESULTADO\n⠀⠀⠀              de\n⠀⠀⠀        Relatório\n⠀(ID: {report_id})"
            await interaction.edit_original_response(embed=embed, view=None)
            #embed.title = f"⠀⠀⠀ 🟢 RESULTADO\n⠀⠀⠀              de\n⠀⠀⠀        Relatório\n⠀(ID: {report_id})"
            #await interaction.followup.send(embed=embed)
            
            
            print('[LevelSystem.py] Embed foi alterado para APROVADO')
            
            
            if not operacao_especial:
                points_to_add = pontuacao
            elif operacao_especial == 'diario' or operacao_especial == 'diário' or operacao_especial == 'dia' or operacao_especial == 'diaria' or operacao_especial == 'diária' or operacao_especial == 'opd':
                points_to_add = pontuacao_final
            elif operacao_especial == 'semanal' or operacao_especial == 'ops':
                points_to_add = pontuacao_final
            elif operacao_especial == 'oficial' or operacao_especial == 'opof' or operacao_especial == 'opf':
                points_to_add = pontuacao_final
            else:
                points_to_add = pontuacao
            
            if operadores:
                # Adiciona os pontos aos membros mencionados
                for member in operadores_list:
                    self.user_points[member.id] += points_to_add
                print('[LevelSystem.py] Pontos foram acrescidos a cada membro da lista.')
            
            if operadores:
                print('[LevelSystem.py] Iniciando troca de cargos.')
                # Adiciona o novo cargo para os membros mencionados
                print('[LevelSystem.py] Iniciando adição de cargos')
                for member in operadores_list:
                    await self.update_roles(member)
                print('[LevelSystem.py] Acrescido os cargos aos operadores.')
                await self.save_data()

        elif view.value == "reject":
            print('[LevelSystem.py] Iniciando Recusa de Relatório')
            embed.add_field(name='Análise:', value='RECUSADO.', inline=True)
            
            # Adiciona o aprovador/recusador ao embed
            approver_mention = view.approver.mention if view.approver else "Nenhum"

            embed.add_field(name="Analista:", value=approver_mention, inline=False)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')
            embed.set_footer(text=f"❌ A CORREGEDORIA RECUSOU em {datetime.datetime.now().strftime('%d-%m-%Y')}.\n\nOpEsp ROLEPLAY. Todos os direitos reservados.") #icon_url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')
            print('[LevelSystem.py] Relatório recusado.')
            embed.title = f"⠀⠀⠀ 🔴 RESULTADO\n⠀⠀⠀              de\n⠀⠀⠀        Relatório\n⠀(ID: {report_id})"
            await interaction.edit_original_response(embed=embed, view=None)
            #embed.title = f"⠀⠀⠀ 🔴 RESULTADO\n⠀⠀⠀              de\n⠀⠀⠀        Relatório\n⠀(ID: {report_id})"
            #await interaction.followup.send(embed=embed)           
            
    async def reward_activity(self, user):
        # Caso o operador não esteja no dicionário de atividades, acrescenta ele
        if user.id not in self.user_activity:
            self.user_activity[user.id] = 0
            
        self.user_activity[user.id] += 1
        # Add 350 points to the user
        self.user_points[user.id] += 300
        await self.update_roles(user)

        # Inform the user of the activity reward
        await user.send("Você recebeu 300 pontos por enviar e/ou participar de 3 relatórios!")

    async def reset_activity(self, user):
        # Caso o operador não esteja no dicionário de atividades, acrescenta ele   
        if user.id not in self.user_activity:
            self.user_activity[user.id] = 0
            
        # Reseta os pontos do usuário para zero.
        self.user_activity[user.id] = 0
        await user.send(f"Você não enviou e/ou não participou de 3 relatórios hoje. Seus {self.user_activity[user.id]} pontos de atividade foram resetados para **zero.**.")


# ---------------------------- TASKS.LOOP --------------------------------------------
    # DECAIMENTO DE RANK A CADA 24H
    @tasks.loop(hours=24)
    async def daily_decay(self):
        guild_id = 1114290574044971031
        guild = self.bot.get_guild(guild_id)

        # Ensure user_points and last_report_time are initialized
        if not hasattr(self, 'user_points'):
            self.user_points = {}
        if not hasattr(self, 'last_report_time'):
            self.last_report_time = {}

        # Load user_points from the levelsystem_database.json file
        await self.load_data()

        # Caso o operador não esteja no dicionário de atividades, acrescenta ele
        for user_id in self.user_points.keys():
            if user_id not in self.last_report_time:
                self.last_report_time[user_id] = datetime.datetime.utcnow()

        for user_id, last_report_time in self.last_report_time.items():
            user = await guild.fetch_member(user_id)
            if user:
                delta = datetime.datetime.utcnow() - last_report_time
                if user.roles not in self.progression_roles[7:-1]:  # Se o usuário não for 2ºten ou acima não desconte seus pontos
                    pass
                elif delta.days >= 1 or not await self.is_coronel(user):
                    await self.decay_points(user)
                    print(f'[LevelSystem.py] DEDUZINDO pontuação do usuário: "{user.display_name}" por inatividade.')

        # Save user_points to the levelsystem_database.json file
        await self.save_data()
    print('(READY) - [LevelSystem.py] TASK.LOOP: DAILY DECAY POINTS')

    @daily_decay.before_loop
    async def before_daily_decay(self):
        await self.bot.wait_until_ready()

    async def decay_points(self, user):
        if user.id in self.user_points:
            decay_rate = 0.00005  # 0.005%
            self.user_points[user.id] -= int(self.user_points[user.id] * decay_rate)
            await self.update_roles(user)
    print('(READY) - [LevelSystem.py] TASK.LOOP: BEFORE [DAILY DECAY POINTS]')

    # TASK DE PONTOS DE ATIVIDADE
    @tasks.loop(hours=24)
    async def daily_activity_reward(self):
        for user_id, activity_count in self.user_activity.items():
            user = await self.bot.fetch_user(user_id)
            if user and activity_count >= 3:
                await self.reward_activity(user)
                
                self.tasklist_pontos_acrescidos.append(user.display_name)
                print(f'[LevelSystem.py] Pontos ACRESCIDOS: Usuário: {user.display_name}') # verificar possibilidade de montar e resetar uma lista diária para enviar na minha DM
            elif self.user_activity[user.id] == 0:
                pass
            else:
                await self.reset_activity(user)
                print(f'[LevelSystem.py] Pontos RESETADOS: Usuário: {user.display_name}') # verificar possibilidade de montar e resetar uma lista diária para enviar na minha DM
                self.tasklist_pontos_resetados.append(user.display_name)
        
        owner_id = 226839699275120642 # ID do usuário que receberá o backup
        owner_msg = await self.bot.fetch_user(owner_id)  # Replace USER_ID with the specific user's ID
        await owner_msg.send(f"**({datetime.datetime.now().strftime('%d-%m-%Y')})** - BACKUP - **Operadores com Pontos ACRESCIDOS:**\n{self.tasklist_pontos_acrescidos}")
        await owner_msg.send(f"**({datetime.datetime.now().strftime('%d-%m-%Y')})** - BACKUP - **Operadores com Pontos de atividade RESETADOS:**\n{self.tasklist_pontos_resetados}")
        self.tasklist_pontos_acrescidos = []
        self.tasklist_pontos_resetados = []
        
    print('(READY) - [LevelSystem.py] TASK.LOOP: ACTIVITY REWARD')

    @daily_activity_reward.before_loop
    async def before_daily_activity_reward(self):
        await self.bot.wait_until_ready()
    print('(READY) - [LevelSystem.py] TASK.LOOP: BEFORE_LOOP [ACTIVITY REWARD]')

    # ENVIA O BACKUP POINTS A CADA 24H PARA MIM
    @tasks.loop(hours=24)
    async def backup_points_task(self):
        # Carregar dados do arquivo ao iniciar
        await self.load_data()
        owner_id = 226839699275120642 # ID do usuário que receberá o backup
        user = await self.bot.fetch_user(owner_id)  # Replace USER_ID with the specific user's ID
        if self.user_points:
            await user.send(f"**({datetime.datetime.now().strftime('%d-%m-%Y')}) - BACKUP DE PONTOS:**\n{self.user_points}\n.")
        
            # Após usar as variáveis nos loops ou comandos, atualize os dados no arquivo
            await self.save_data()
    print('(READY) - [LevelSystem.py] TASK.LOOP: BACKUP POINTS')
    
    @backup_points_task.before_loop
    async def before_backup_points_task(self):
        await self.bot.wait_until_ready()
    print('(READY) - [LevelSystem.py] TASK.LOOP: BEFORE_LOOP [BACKUP POINTS]')
    
    # CASO O OPERADOR POSSUA 90 PONTOS DE ATIVIDADE OU SEJA CORONEL, NÃO DECAIA OS PONTOS DELE:
    @tasks.loop(hours=24)
    async def check_activity(self):
        tasklist_pontos_decrescidos_meio_porcento = []
        for user_id, activity_count in self.user_activity.items():
            user = await self.bot.fetch_user(user_id)
            if user and activity_count >= 90 or await self.is_coronel(user):
                pass
            elif user and not user.roles in self.progression_roles[6:-1]:
                pass
            elif user and activity_count == 0 or user.roles in self.progression_roles[6:-1]: # verificar se o cargo do usuário está em progression roles a partir do índice de segundo tenente.
                await self.decay_points(user)
                tasklist_pontos_decrescidos_meio_porcento.append(user.display_name)
        
        owner_id = 226839699275120642 # ID do usuário que receberá o backup
        owner_msg = await self.bot.fetch_user(owner_id)  # Replace USER_ID with the specific user's ID
        await owner_msg.send(f"**({datetime.datetime.now().strftime('%d-%m-%Y')})** - BACKUP - **Pontos DECRESCIDOS:**\n{tasklist_pontos_decrescidos_meio_porcento}\n.")
    print('(READY) - [LevelSystem.py] TASK.LOOP: CHECK ACTIVITY')
    
    @check_activity.before_loop
    async def before_check_activity(self):
        await self.bot.wait_until_ready()
    print('(READY) - [LevelSystem.py] TASK.LOOP: BEFORE_LOOP [CHECK ACTIVITY]')

    @tasks.loop(hours=24)  # Intervalo em horas
    async def update_rank_loop(self):
        GUILD_ID = 1114290574044971031
        guild_id = GUILD_ID  # Substitua pelo ID do seu servidor
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return

        members = [await guild.fetch_member(user_id) for user_id, _ in self.user_points.items() if guild.get_member(user_id)]
        members = [member for member in members if member]

        sorted_members = sorted(members, key=lambda member: self.user_points[member.id], reverse=True)[:10]

        self.rank_data = []
        for idx, user in enumerate(sorted_members, start=1):
            mention_role_ids = [role.id for role in user.roles if role.id in [r["role_id"] for r in self.progression_roles]]
            
            if mention_role_ids:
                mention_role = discord.utils.get(user.roles, id=mention_role_ids[0]).mention
            else:
                mention_role = "Sem patente"

            self.rank_data.append({
                'idx': idx,
                'user_mention': user.mention,
                'mention_role': mention_role,
                'points': self.user_points[user.id]
                })
            
    print('(READY) - [LevelSystem.py] TASK.LOOP: UPDATE_RANK_LOOP')
    
    @update_rank_loop.before_loop
    async def before_update_rank_loop(self):
        await self.bot.wait_until_ready()

    # Verifica se o usuário é CORONEL:
    async def is_coronel(self, user):
        GUILD_ID = 1114290574044971031
        guild = self.bot.get_guild(GUILD_ID)  # Replace GUILD_ID with your actual guild ID
        coronel_role = discord.utils.get(guild.roles, name='Coronel')  # Replace 'Coronel' with the actual role name

        if coronel_role in user.roles:
            return True
        return False
        
    
# ----------------------ENCERRADO--TASKS.LOOP --------------------------------------------
      
    # RANK TOP 10 PONTOS
    @app_commands.command(
        name="rank",
        description="Exibe o Rank de Pontuação dos Operadores"
    )
    async def rank(self, interaction: discord.Interaction):
        GUILD_ID = 1114290574044971031
        guild_id = GUILD_ID  # Substitua pelo ID do seu servidor
        guild = self.bot.get_guild(guild_id)
        await self.load_data()
        
        if not guild:
            return

        members = [await guild.fetch_member(user_id) for user_id, _ in self.user_points.items() if guild.get_member(user_id)]
        members = [member for member in members if member]

        sorted_members = sorted(members, key=lambda member: self.user_points[member.id], reverse=True)[:10]

        self.rank_data = []
        for idx, user in enumerate(sorted_members, start=1):
            mention_role_ids = [role.id for role in user.roles if role.id in [r["role_id"] for r in self.progression_roles]]
            
            if mention_role_ids:
                mention_role = discord.utils.get(user.roles, id=mention_role_ids[0]).mention
            else:
                mention_role = "Sem patente"

            self.rank_data.append({
                'idx': idx,
                'user_mention': user.mention,
                'mention_role': mention_role,
                'points': self.user_points[user.id]
                })
            await self.save_data()
            
        # BACKUP DAQUI
        if not self.rank_data:
            await interaction.response.send_message("Os dados do ranking ainda não foram atualizados. Tente novamente mais tarde.")
            return

        embed = discord.Embed(
            title="Rank de Pontuação dos Operadores",
            color=discord.Colour.dark_orange()
        )

        for data in self.rank_data:
            embed.add_field(
                name=f"",
                value=f"{data['idx']}. **{data['user_mention']}** | **Patente:** {data['mention_role']} | **Pontuação:** {data['points']}",  # Adicione outros detalhes ou deixe em branco
                inline=False
            )

        await interaction.response.send_message(embed=embed)
        
        # BACKUP ATÉ AQUI
    print('(READY) - [LevelSystem.py] /rank')
            
    # Comando de BACKUP do sistema:
    @app_commands.command(
name="backuplevelsystem",
description="Backup do sistema de patentes")
    @commands.has_permissions(administrator=True)
    async def backuplevelsystem(self, interaction: discord.Interaction):
        # Após usar as variáveis nos loops ou comandos, atualize os dados no arquivo
        if self.user_points:
            await self.save_data()
                
            backup_points_dict = self.user_points.copy()
            backup_activity_dict = self.user_activity.copy()
            backup_last_report_time_dict = self.last_report_time.copy()
            message = await interaction.user.send(f"**{datetime.datetime.now().strftime('%d-%m-%Y')}**\nBACKUP DE **PONTOS DE CARREIRA**:\n{backup_points_dict}\n.")
            await interaction.user.send(f"BACKUP DE **PONTOS DE ATIVIDADE**:\n{backup_activity_dict}\n.")
            await interaction.user.send(f"BACKUP DE **TEMPO DO ÚLTIMO RELATÓRIO**:\n{backup_last_report_time_dict}\n.")
            await interaction.response.send_message(f'Te enviei uma mensagem no privado com o **backup** do sistema de patentes! {message.jump_url}', ephemeral=True, delete_after=10)

    @app_commands.command(
            name="progresso",
            description="Mostra as patentes alcançadas e pontos do operador."
        )
    async def progresso(self, interaction: discord.Interaction):
        # Obtém o ID do autor da interação
        user_id = interaction.user.id

        if user_id not in self.user_activity:
            self.user_activity[user_id] = 0

        embed_cargos = discord.Embed(color=discord.Colour.dark_orange())
        embed_cargos.set_image(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185249698156646491/GIF_CARGOS.gif?ex=658eeccc&is=657c77cc&hm=411fee3a6957afe68557879e95e8b1f2b9e23e624256fe1194dc01933b68cf9b&')


        # Inicializa a mensagem do embed
        embed = discord.Embed(title="⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   Corregedoria\nPatentes e Pontuações de Operador", color=discord.Colour.dark_orange())
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')    
        embed.set_image(url='https://i.makeagif.com/media/5-06-2017/rJYquW.gif')

        # Adiciona informações sobre as patentes e pontos
        for role_info in self.get_roles_info():
            role_id = role_info["role_id"]
            role = interaction.guild.get_role(role_id)

            # Verifica se o usuário possui a patente
            if role in interaction.user.roles:
                points_required = role_info["points_required"]
                embed.add_field(name=f"", value=f"🟢{role.mention} - ({points_required}) Você está aqui!", inline=False)
            else:
                points_required = role_info["points_required"]
                embed.add_field(name=f"", value=f"🔴{role.mention} - requer ({points_required}) pontos", inline=False)

        # Adiciona informações sobre os pontos do usuário
        if user_id in self.user_points:
            embed.add_field(name="", value=f'Pontos Atuais: {str(int(self.user_points[user_id]))}', inline=False)
        else:
            embed.add_field(name="**\nPontuação:**", value="Você ainda não possui pontos.", inline=False)
            
        embed.add_field(name="**\nPontos de atividade:**", value=f"{self.user_activity[user_id]}", inline=False)
            
        embed.add_field(name='', value='- Utilize o comando **/relatorio** para registrar pontos de carreira e ser promovido.', inline=False)
        embed.add_field(name='', value='- Ganhe 350 pontos a mais **por dia** que participar ou enviar 3 relatórios!', inline=False)
        embed.add_field(name='', value='- A partir da patente de **Segundo Tenente** você precisará **participar ou enviar pelo menos um relatório por dia** para não perder **0,005%** (meio porcento) de pontuação ao dia não jogado.', inline=False)
        embed.set_footer(text='OpEsp ROLEPLAY. Todos os direitos reservados.', icon_url='https://cdn.discordapp.com/attachments/1032063754843738202/1185243152316108922/EMOJI_512X512.png?ex=658ee6b4&is=657c71b4&hm=44a2c47ce9cac736ea9344912b56e60e2271e247fba38d53e33b71c673df895e&')
        
        # Envia o embed
        await interaction.response.send_message(embeds=[embed_cargos, embed], ephemeral=True)
        
        # Método auxiliar para obter informações sobre as patentes
    def get_roles_info(self):
        progression_roles = [
        {"role_id": 1114290574644760690, "name": "Recruta", "points_required": 0},
        
        {"role_id": 1114290574644760691, "name": "Soldado", "points_required": 8000},
        
        {"role_id": 1114290574644760692, "name": "Cabo", "points_required": 16000},
        
        {"role_id": 1114290574644760693, "name": "Terceiro Sargento", "points_required": 35000},
        
        {"role_id": 1114290574644760694, "name": "Segundo Sargento", "points_required": 49000},
        
        {"role_id": 1114290574644760695, "name": "Primeiro Sargento", "points_required": 65000},
        
        {"role_id": 1114290574644760696, "name": "Subtenente", "points_required": 86000},
        
        {"role_id": 1114290574661521468, "name": "Segundo Tenente", "points_required": 104000},
        
        {"role_id": 1114290574661521469, "name": "Primeiro Tenente", "points_required": 125000},
        
        {"role_id": 1114290574661521470, "name": "Capitão", "points_required": 150000},
        
        {"role_id": 1114290574661521471, "name": "Major", "points_required": 177000},
        
        {"role_id": 1114290574661521472, "name": "Tenente-Coronel", "points_required": 207000},
        
        {"role_id": 1114290574661521473, "name": "Coronel", "points_required": 240000},
        ]
        return progression_roles
    

    @app_commands.command(
        name="alterapontos",
        description="Altera os pontos de um operador com base no ID dele",
    )
    @commands.has_permissions(administrator=True)
    async def alterapontos(self, interaction: discord.Interaction, operador: discord.Member, novo_valor: int):
        user_id = operador.id #str(operador.id)
        await self.load_data()
        
        if user_id in self.user_points:
            
            # Se o usuário está no dicionário, altera o valor da chave
            self.user_points[user_id] = novo_valor
            
            # Verifica e Atualiza a patente atual do operador:
            await self.update_roles(operador)
            await self.save_data()  # Save the changes to the data file
            
            await interaction.response.send_message(f"Os pontos do operador **{operador}** foram alterados para **{novo_valor}**", ephemeral=True)
            
        else:
            self.user_points[user_id] = novo_valor
            await self.update_roles(operador)
            await self.save_data()  # Save the changes to the data file
            
            # Se o usuário não está no dicionário, informa que o usuário não foi encontrado
            await interaction.response.send_message(f"Operador {operador} não encontrado.\nEle foi inserido no sistema e os pontos foram alterados para **{novo_valor}**.", ephemeral=True)
        
        
    async def get_user_points(self, user_id):
        # Função para obter os pontos de um usuário com base no arquivo levelsystem_database.json
        try:
            with open("levelsystem_database.json", "r") as f:
                data = json.load(f)
            return data["user_points"].get(str(user_id), None)
        except FileNotFoundError:
            return None
    
    @app_commands.command(
    name="verificapontos",
    description="Verifica os pontos atuais de um operador com base no ID dele",
)
    @commands.has_permissions(administrator=True)
    async def verificapontos(self, interaction: discord.Interaction, operador: discord.Member):
        user_id = operador.id
        await self.update_roles(operador)
        # Se o usuário está no dicionário, obtém o valor da chave
        pontos_atuais = await self.get_user_points(user_id)
        if pontos_atuais is not None:
            await interaction.response.send_message(f"O operador **{user_id}** possui **{int(pontos_atuais)}** pontos.", ephemeral=True)
        else:
            await interaction.response.send_message(f"Operador **{user_id}** não encontrado. Certifique-se de que mencionou corretamente.", ephemeral=True)

    print('(READY) - [LevelSystem.py] LOADED.')
async def setup(bot) -> None:
    cog = levelsystem(bot)
    await bot.add_cog(cog)
    #await bot.add_cog(levelsystem(bot))
    cog.backup_points_task.start()
    cog.daily_decay.start()
    await cog.update_rank_loop()
    await cog.check_activity()
    await cog.daily_activity_reward()
    await cog.load_data()