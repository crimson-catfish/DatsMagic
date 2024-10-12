# TODO: process movement and don't kill yourself in the process
from strategy import bounty_finder

def clamp(val, a, b):
    if val < a:
        val = a
    elif val > b:
        val = b

    return val


def acceleration(frame: dict, transport: dict, enemies_nearby: list):
    accel = {"x": 0, "y": 0}

    bounty_for_transport = bounty_finder.get_closest_bounty(frame["bounties"], frame["transports"])
    # TODO: write into accel to move to bounty
    dir_x = bounty_for_transport[transport["id"]]['x'] - transport['x']
    dir_y = bounty_for_transport[transport["id"]]['y'] - transport['y']

    accel['x'] = clamp(dir_x,  -5,  5)
    accel['y'] = clamp(dir_y,  -5,  5)

    # overwrite accel if we close to wall  
    if transport["x"] + transport["velocity"]["x"] > frame["mapSize"]["x"] * 0.95:
        accel["x"] = -frame["maxAccel"]
    elif transport["x"] + transport["velocity"]["x"] < frame["mapSize"]["x"] * 0.05:
        accel["x"] = frame["maxAccel"]
    if transport["y"] + transport["velocity"]["y"] > frame["mapSize"]["y"] * 0.95:
        accel["y"] = -frame["maxAccel"]
    elif transport["y"] + transport["velocity"]["y"] < frame["mapSize"]["y"] * 0.05:
        accel["y"] = frame["maxAccel"]

    return accel