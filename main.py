import discord
import random
import json

from module.Buttons import Buttons
from module.Client import MyClient

with open("config/config.json", "r") as f:
    config_data = json.load(f)
    TOKEN = config_data["TOKEN"]
    GUILD = discord.Object(config_data["GUILDS_ID"])

def run():
    # initialize

    client = MyClient()

    # commands

    @client.tree.command(guild=GUILD, name="calculator", description="Sends an interactive calculator")
    async def calculator(interaction: discord.Interaction):
        await interaction.response.send_message("```Begin Calculating```", view=Buttons())

    @client.tree.command(guild=GUILD, name="calc", description="command line calculator")
    async def calc(interaction: discord.Interaction, expression: str):
        result = str(eval(expression))
        await interaction.response.send_message(result)

    @client.tree.command(guild=GUILD, name="dice", description="roll dice")
    async def calc(interaction: discord.Interaction, count:int = 1):
        result = random.randint(1, 7 * count)
        await interaction.response.send_message(content=f"```Your dice🎲 is: {result}```")

    client.run(TOKEN)


if __name__ == "__main__":
    run()