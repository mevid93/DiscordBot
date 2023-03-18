
from src.parsed_command import CommandType

STANDARD_RESPONSE_UNKNOWN = "Received unknown command sequence! No actions taken..."
STANDARD_RESPONSE_INFO = "GigaChad bot (https://github.com/mevid93/DiscordBot)"
STANDARD_RESPONSE_HELP = \
    """
    ```
    Usage: <botname> [global options] command [command options] [arguments...]

    Commands:
        info          show bot details
        question      ask a question
        music         play music
        stop          stop all background processes

    Global options:
        --help, -h    show help
    ```
    """
STANDARD_RESPONSE_STOP = "Stopping all active background processes..."
STANDARD_RESPONSE_INSTRUCTION = "Command is missing arguments. Add **--help** after the command to get more information."


def get_standard_response(command_type: CommandType) -> str:
    """ Returns string repsonse based on command type.
    """
    if command_type == CommandType.UNKNOWN:
        return STANDARD_RESPONSE_UNKNOWN
    if command_type == CommandType.INFO:
        return STANDARD_RESPONSE_INFO
    if command_type == CommandType.HELP:
        return STANDARD_RESPONSE_HELP
    if command_type == CommandType.STOP:
        return STANDARD_RESPONSE_STOP
    if command_type == CommandType.INSTRUCTION:
        return STANDARD_RESPONSE_INSTRUCTION
    return None
