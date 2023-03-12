import discord

class Bot:

    def __init__(self, token: str):
        self.TOKEN = token

    def run_discord_bot(self):
        client = discord.Client(intents=discord.Intents.default())

        @client.event
        async def on_ready():
            print(f"{client.user} is now running")
        
        client.run(self.TOKEN)
