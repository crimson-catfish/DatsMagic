import api, logger
from api import participate

current_round = api.rounds_info()["now"]
logger = logger.Logger(current_round)

frame = participate(test=True)

    