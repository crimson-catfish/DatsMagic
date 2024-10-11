import api, frame_logger
from api import participate

current_round = api.rounds_info()["now"]
logger = frame_logger.Logger(current_round)

frame = participate(test=True)

# while True:
    # logger.log(frame)

    # process frame
    
    # command = ???
    
    # frame = api.send_command(command)
    