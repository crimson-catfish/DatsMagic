import api, frame_logger, visualizer, error_checker, strategy.commander
import time

test_or_not = True

print("collecting round info")
rounds_info = api.rounds_info()
current_round = rounds_info["now"]

print("connecting to game")
frame = api.participate(test_or_not)
if not error_checker.ok(frame):
    exit()

last_time = time.time()

print("connecting to logger")
logger = frame_logger.Logger(current_round)

print("connecting to visualizer")
vs = visualizer.Visualizer(frame["mapSize"])

while True:
    if not error_checker.ok(frame):
        break

    if len(frame["errors"]) > 0:
        print(frame["errors"])

    # print("logging...")
    logger.log(frame)
    vs.draw_frame(frame)

    # print("calculating strategy...")
    command = strategy.commander.process_all_transports(frame)

    sleep_time = 0.33 - time.time() + last_time
    if sleep_time > 0:
        time.sleep(sleep_time)
    last_time = time.time()

    # print("waiting for api...")
    frame = api.send_command(command)
