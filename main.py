import api, frame_logger, visualizer

current_round = api.rounds_info()["now"]
logger = frame_logger.Logger(current_round)
vs = visualizer.Visualizer()

frame = api.participate(test=True)

while True:
    if "error" in frame:
        print("ERROR: ", frame["error"])
        if frame["error"] == 'realm not found':
            print("сервер не работает(наверное)")
        break
    logger.log(frame)
    vs.draw_frame(frame)
    frame = api.participate()

    # process frame
    
    # command = ???
    
    # frame = api.send_command(command)
    