import api, frame_logger, visualizer, rounds_utility
import error_checker

test_or_not = True

print("collecting round info")
rounds_info = api.rounds_info()
current_round = rounds_info["now"]

print("connecting to game")
frame = api.participate(test_or_not)
if not error_checker.ok(frame):
    exit()

print("connecting to logger")
logger = frame_logger.Logger(current_round)

print("connecting to visualizer")
vs = visualizer.Visualizer(frame["mapSize"])

while True:
    if not error_checker.ok(frame):
        break

    logger.log(frame)
    vs.draw_frame(frame)
    frame = api.participate(test_or_not)

    # process frame
    
    # command = ???
    
    # frame = api.send_command(command)
    