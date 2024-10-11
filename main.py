import api, frame_logger, visualizer, rounds_utility

test_or_not = True

print("collecting round info")
rounds_info = api.rounds_info()
current_round = rounds_info["now"]

print("connecting to logger")
logger = frame_logger.Logger(current_round)

print("connecting to visualizer")
vs = visualizer.Visualizer()

print("connecting to game")
frame = api.participate(test_or_not)

while True:
    if "error" in frame:
        print(frame["error"] + " " + str(frame["errCode"]))
        if frame["error"] == 'realm not found':
            print("time before next round: " + str(rounds_utility.time_before_next_round(rounds_info)))
        break

    logger.log(frame)
    vs.draw_frame(frame)
    frame = api.participate(test_or_not)

    # process frame
    
    # command = ???
    
    # frame = api.send_command(command)
    