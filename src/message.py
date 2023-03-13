from enum import Enum


class MessageType(Enum):
    HELP = 0
    INFO = 1
    UNKNOWN = 2
    QUESTION = 3
    COMMAND = 4


class ParsedMessage():
    """ Message class (data wrapper).
    """

    def __init__(self, message_channel, message_sender, message_content, \
                 message_type = MessageType.UNKNOWN, question_str = None, command = None):
        """ Constructor.
        """
        self.message_channel = message_channel
        self.message_sender = message_sender
        self.message_content = message_content
        self.message_type = message_type
        self.question_str = question_str
        self.command = command
        
