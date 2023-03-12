from bot import Bot
from dotenv import dotenv_values

ENV_VAR_FILENAME = ".env"
ENV_VAR_TOKEN = "BOT_TOKEN"

def check_configuration(config: dict):
    """ Check that all required environmental variables are present in the configuration.
        Throws an error if any of the variables is missing.
    """
    required_variables = [ENV_VAR_TOKEN]
    for variable_name in required_variables:
        if variable_name not in config.keys():
            raise Exception(f"Environmental variable {variable_name} is not defined!")

if __name__ == "__main__":
    # load environmental variables
    config = dotenv_values(ENV_VAR_FILENAME)
    
    # check that configuratio is valid
    check_configuration(config)

    token = config[ENV_VAR_TOKEN]

    Bot(token=token).run_discord_bot()
