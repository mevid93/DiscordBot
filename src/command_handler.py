
from src.parsed_command import CommandType, ParsedCommand
from src.responses import get_standard_response


class CommandHandler:
    """ Class for handling parsed commands.
    """

    def __init__(self):
        pass

    async def handle_command(self, command: ParsedCommand):
        if command.command_type == CommandType.UNKNOWN:
            response = get_standard_response(CommandType.UNKNOWN)
            await command.message.channel.send(response)
        
        elif command.command_type == CommandType.INFO:
            response = get_standard_response(CommandType.INFO)
            await command.message.channel.send(response)
        
        elif command.command_type == CommandType.HELP:
            response = get_standard_response(CommandType.HELP)
            await command.message.channel.send(response)
        
        elif command.command_type == CommandType.INSTRUCTION:
            response = get_standard_response(CommandType.INSTRUCTION)
            await command.message.channel.send(response)

        elif command.command_type == CommandType.QUESTION:
            # TODO: Implement lofic for answering questions
            pass

        elif command.command_type == CommandType.STOP:
            # TODO: IMPLEMENT LOGIC FOR STOPING SERVICES
            response = get_standard_response(CommandType.STOP)
            await command.message.channel.send(response)
        
        elif command.command_type == CommandType.MUSIC:
            # TODO: IMPLEMENT LOFIC FOR PLAYING MUSIC IN THE BACKGROUND OF VOICE CHAT
            pass
