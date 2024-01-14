from discord import app_commands
from discord.ext import commands, tasks
import random
from discord.ext.commands import BucketType, cooldown
import discord
from datetime import datetime, timedelta
import asyncio

class opd(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.maps = ['Elephant', 'Rust Belt', 'Sins of The Father', 'Carriers of the Vine',
                     'Hide and Seek', 'Buy Cheap, Buy Twice', 'Thank You, Come Again', 'Twisted Nerve',
                     'Relapse', 'Neon Tomb', 'Ides of March', 'A Lethal Obsession',
                     'Greased Palms', 'Sinuous Trail', 'The Spider', 'Valley of the Dolls',
                     '23 Megabytes a Second', 'Ends of the Earth']

        # Initialize last_map_time with the current time
        self.last_map_time = datetime.utcnow()

        # Start the background task to change the map every 24 hours
        self.change_map_task.start()

    def cog_unload(self):
        # Stop the background task when the cog is unloaded
        self.change_map_task.cancel()

    @tasks.loop(hours=24)
    async def change_map_task(self):
        # Change the map every 24 hours
        global new_map
        new_map = random.choice(self.maps)
        print(f"Changed map to: {new_map}")
        
        # Reset last_map_time to the current time when the task is restarted
        self.last_map_time = datetime.utcnow()
        
        # Reschedule the task after it has completed its current iteration
        await asyncio.sleep(24 * 60 * 60)  # Ensure a small delay to let the loop complete
        self.change_map_task.restart()

    @app_commands.command(name='opd', description='Mostra a OPERAÇÃO DO DIA que dá bônus de pontos de carreira.')
    async def opd(self, interaction: discord.Interaction):
        # Calculate the time difference since the last map change
        time_since_last_change = datetime.utcnow() - self.last_map_time

        # Update the last map time
        self.last_map_time = datetime.utcnow()

        # Calculate the remaining time until the next map change
        time_until_next_change = timedelta(hours=24) - time_since_last_change

        opd_embed = discord.Embed(
            title='OPERAÇÃO DO DIA:',
            color=discord.Color.dark_orange()
        )
        opd_embed.add_field(name=f'', value=f'- **{new_map}** (Nota A+)')
        opd_embed.add_field(name=f'', value=f'Tempo até o próximo mapa: **{time_until_next_change}**', inline=False)

        message = await interaction.response.send_message(embed=opd_embed)
        emoji_fire = '🔥'
        emoji_skull = '☠️'
        # Adiciona a reação à mensagem
        message = await interaction.original_response()		
        await message.add_reaction(emoji_fire)
        await message.add_reaction(emoji_skull)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(opd(bot))
