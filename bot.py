import discord


class Bot:
    """ Simple Discord bot class.
    """

    def __init__(self, token: str, admin: str, app_id: str):
        self.TOKEN = token
        self.ADMIN = admin
        self.APPLICATION_ID = app_id

    def should_message_be_processed(self, message, client):
        """ Takes discord message as input, and checks whether it should be processed.
            Returns True if the message should be processed.
        """
        # prevent loops by filtering messages from bot
        if message.author == client.user:
            return False
        # only allow admin to interact with the bot
        if str(message.author) != self.ADMIN:
            return False
        # only process messages where the first mention is the bot
        if len(message.mentions) == 0 or str(message.mentions[0].id) != self.APPLICATION_ID:
            return False
        return True

    def run_discord_bot(self):
        """ Set event handling and run the discord bot.
        """
        client = discord.Client(intents=discord.Intents.all())

        @client.event
        async def on_ready():
            print(f"{client.user} is now running")

        @client.event
        async def on_message(message):
            if not self.should_message_be_processed(message, client):
                return

            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            message_is_from_admin = username == self.ADMIN

            print(username, user_message, channel, message_is_from_admin)

        client.run(self.TOKEN)
