import api, frame_logger
from api import participate

current_round = api.rounds_info()["now"]
logger = frame_logger.Logger(current_round)

frame = participate(test=True)
logger.log(frame)
logger.log(frame)

    