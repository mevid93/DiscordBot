
from src.parsed_command import CommandType, ParsedCommand


class CommandParser():
    """ Class for parsing bot commands.
    """

    def __init__(self):
        """ Constructor.
        """
        self.background_processes = [] # array of background processes

    def parse_command(self, message) -> ParsedCommand:
        """ Method for parsing bot commands received from discord message.
        """
        channel = str(message.channel)
        sender = str(message.author)
        content = str(message.content)

        content_parts = content.split()

        # try to parse messages that have minimum of two parts after split
        if len(content_parts) < 2:
            return ParsedCommand(message, channel, sender, content, CommandType.UNKNOWN)
        if content_parts[1] == "--help" or content_parts[1] == "-h":
            return ParsedCommand(message, channel, sender, content, CommandType.HELP)
        if content_parts[1] == "info":
            return ParsedCommand(message, channel, sender, content, CommandType.INFO)
        if content_parts[1] == "stop":
            return ParsedCommand(message, channel, sender, content, CommandType.STOP)
        
        # not enough arguments
        if len(content_parts) == 2 and content_parts[1] == "question":
            return ParsedCommand(message, channel, sender, content, CommandType.INSTRUCTION)
        if len(content_parts) == 2 and content_parts[1] == "music":
            return ParsedCommand(message, channel, sender, content, CommandType.INSTRUCTION)

        # try to parse messages that have minimum of three parts after split
        if len(content_parts) < 3:
            return ParsedCommand(message, channel, sender, content, CommandType.UNKNOWN)
        if content_parts[1] == "question":
            return ParsedCommand(message, channel, sender, content, CommandType.QUESTION, " ".join(content_parts[2:]))
        if content_parts[1] == "music":
            return ParsedCommand(message, channel, sender, content, CommandType.MUSIC, " ".join(content_parts[2:])) 
        
        # if flow ends here --> unknown message type
        return ParsedCommand(message, channel, sender, content, CommandType.UNKNOWN)
