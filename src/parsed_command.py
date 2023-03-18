from enum import Enum


class CommandType(Enum):
    HELP = 0
    INFO = 1
    UNKNOWN = 2
    QUESTION = 3
    MUSIC = 4
    STOP = 5
    INSTRUCTION = 6


class ParsedCommand():
    """ Command class (data wrapper).
    """

    def __init__(self, message, message_channel, message_sender, message_content,
                 command_type=CommandType.UNKNOWN, command_args = None):
        """ Constructor.
        """
        self.message = message
        self.message_channel = message_channel
        self.message_sender = message_sender
        self.message_content = message_content
        self.command_type = command_type
        self.command_args = command_args

    def __str__(self):
        """ Returns string representation of the class.
        """
        return f"ParsedCommand: channel={self.message_channel}, sender={self.message_sender}, " \
            f"content={self.message_content}, type={self.command_type}, " \
            f"args={self.command_args}"
