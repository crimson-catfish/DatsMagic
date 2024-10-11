import api, frame_logger, visualizer

rounds_info = api.rounds_info()
current_round = rounds_info["now"]
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
    