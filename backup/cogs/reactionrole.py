import discord
from discord.ext import commands

class reactionrole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_message_id = 1185286245073555580 # Initialize to None
        self.emoji_to_role = {
            discord.PartialEmoji(name='papelcaneta', id=1185273807238344796): 1185267818510434384,  # ID of the role associated with unicode emoji 'to49'. # TOP
            #discord.PartialEmoji(name='jungle', id=1180236604363784352): 1180234615089274912,  # ID of the role associated with unicode emoji 'jungle'. # JUNGLE
            #discord.PartialEmoji(name='midlol', id=1180236606221860945): 1180234697993891880,  # ID of the role associated with unicode emoji 'midlol'. # MID
            #discord.PartialEmoji(name='bottom69', id=1180236596944048290): 1180234797415661658,  # ID of the role associated with a partial emoji's ID. # ADC
            #discord.PartialEmoji(name='support', id=1180237429576310924): 1180234893419089972,  # ID of the role associated with unicode emoji 'support'. # SUP
            #discord.PartialEmoji(name='📰'): 1180237850927710280,  # ID of the role associated with unicode emoji '📰'. # Patch Notes
        }

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reactionrole(self, ctx):
        embed_reaction_role = discord.Embed(
            title='Reaja com os emojis abaixo para obter os cargos.',
            color=discord.Color.dark_orange()
        )
        embed_reaction_role.set_image(url='https://media.discordapp.net/attachments/1032063754843738202/1185249698156646491/GIF_CARGOS.gif?ex=658eeccc&is=657c77cc&hm=411fee3a6957afe68557879e95e8b1f2b9e23e624256fe1194dc01933b68cf9b&=&width=687&height=250')
        embed_reaction_role.add_field(name='', value=f'> Caso deseje receber uma notificação quando o **Ready or Not** lançar uma atualização **(Patch-Notes)**, reaja com 📰 para receber o cargo: {(ctx.guild.get_role(1185267818510434384).mention)}.', inline=False)

        await ctx.message.delete()
        
        message_to_react = await ctx.send(embed=embed_reaction_role)
        self.role_message_id = message_to_react.id  # Set the role_message_id

        # Add reactions to the message
        for emoji in self.emoji_to_role:
            await message_to_react.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        try:
            await member.add_roles(role)
        except discord.HTTPException:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        try:
            await member.remove_roles(role)
        except discord.HTTPException:
            pass



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(reactionrole(bot))
