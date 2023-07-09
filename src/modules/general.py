from discord import app_commands, Interaction, Member
from discord.ext.commands import Cog, Bot
from discord.app_commands import Choice

class General(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    general = app_commands.Group(name="general", description="Comandos generales")

    @general.command(name="sarasa", description="Sarasa")
    @app_commands.describe(
        member='El miembro al que se le va a decir sarasa'
    )
    async def sarasa(self, interaction: Interaction, member: Member = None):
        member = member or interaction.author
        await interaction.response.send_message(f"{member.mention} sarasaaaaaaaaa!")
    

    @general.command(name="links", description="Links utiles")
    @app_commands.choices(server=[
        Choice(
            name="⬜ Notion",
            value="https://datasam.notion.site/DATA-SAM-1e9dc7b00cd6444897be928a234e2e32"
        ),
        Choice(
            name="🐈‍⬛ GitHub",
            value="https://github.com/DATA-SAM-LCD"
        ),
        Choice(
            name="🌲 Linktree",
            value="https://linktr.ee/datascience2022"
        )
    ])
    async def links(self, interaction: Interaction, server: str):
        await interaction.response.send_message(f"✨ Link: {server}")


async def setup(bot):
    await bot.add_cog(General(bot))