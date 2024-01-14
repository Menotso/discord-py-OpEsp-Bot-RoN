import random
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from datetime import datetime

class giveaway(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.entries = set()

    @app_commands.command()
    async def giveaway(self, interaction: discord.Interaction, prize: str, winners: int = 1, end_time: str = None):
        if end_time is None:
            return await interaction.response.send_message('Faltou inserir a data término do sorteio.', ephemeral=True)
        elif winners < 1:
            return await interaction.response.send_message('Insira uma quantidade de ganhadores válida.', ephemeral=True)

        try:
            data_obj = datetime.strptime(end_time, '%d/%m/%Y%H:%M')
			
        except ValueError:
            return await interaction.response.send_message('Formato de data/hora inválido. Utilize "DD/MM/AAAAHH:MM".', ephemeral=True)

        timestamp_futura = round(int(data_obj.timestamp()))

        embed_waitprize = discord.Embed(
            title = f'{prize}',
            colour = discord.Colour.yellow(),
            #timestamp=interaction.message.created_at
            )
        
        embed_waitprize.add_field(name='', value=f'Reaja a esta mensagem para participar do sorteio de {prize}\n**Quantidade de Ganhadores:** {winners}\n**Término:** <t:{timestamp_futura}:R>', inline=False)
        
        await interaction.response.send_message(embed=embed_waitprize)
        #await interaction.response.send_message(f"Reaja a esta mensagem para participar do sorteio!\n\n**Prêmio:** {prize}\n**Ganhadores:** {winners}\n**Término:** <t:{timestamp_futura}:F>")

        emoji = '🎉'
        # Adiciona a reação à mensagem
        message = await interaction.original_response()
        await message.add_reaction(emoji)
        #await add_reaction(emoji)

        # Espera até a data/hora do sorteio
        while datetime.now().timestamp() < timestamp_futura:
            await asyncio.sleep(5)

        # Obtém as reações da mensagem
        message = await interaction.channel.fetch_message(message.id)
        
        reaction = discord.utils.get(message.reactions, emoji=emoji)

        # Obtém os participantes (usuários que reagiram com o emoji)
        participants = [user async for user in reaction.users()]

        # Filtra os participantes para remover bots
        participants = [participant for participant in participants if not participant.bot]
        
        # Criar filtro: conta criada a partir de.....

        if not participants:
            await interaction.response.send_message("Não há membros elegíveis para o sorteio.", ephemeral=True)
        elif len(participants) < winners:
            await interaction.response.send_message("Refaça sua lista do sorteio! Todos iriam ganhar com esta última configuração.", ephemeral=True)
        else:
            # Seleciona os ganhadores
            winners_list = random.sample(participants, min(winners, len(participants)))
            # Anuncia os vencedores
            embed_prizesent = discord.Embed(
            title = f'{prize}',
            colour = discord.Colour.darker_gray(),
            #timestamp=interaction.message.created_at
            )
        
            embed_prizesent.add_field(name='', value=f'**__Resultado__** do sorteio de **{prize}**\n**Quantidade de Ganhadores:** {winners}\n**Participantes:** {len(participants)}\n**Término:** <t:{timestamp_futura}:R>\n\n**__Sorteados:__** {", ".join(winner.mention for winner in winners_list)}', inline=False)

            await interaction.edit_original_response(embed=embed_prizesent)
            # await interaction.followup.send(embed=embed_prizesent)

            
            # content = f"**Prêmio:** {prize}\n**Ganhadores:** {winners}\n**Término:** <t:{timestamp_futura}:F>\n\nSorteados: {[', '.join(str(winner).mention for winner in winners_list)]}"
            # await interaction.followup.send(content)
            
            #await interaction.response.edit_message(content=f"🐺 **Prêmio:** {prize}\n**Ganhadores:** {winners}\n**Término:** <t:{timestamp_futura}:F>\n\nSorteados: {[', '.join(winner.mention) for winner in winners_list]}")
            #for winner in winners_list:
                #await interaction.response.send_message(f"🎉 {winner}")

async def setup(bot):
    await bot.add_cog(giveaway(bot))