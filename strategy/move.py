# TODO: process movement and don't kill yourself in the process
import math

from strategy import bounty_finder


def clamp(val, a, b):
    if val < a:
        val = a
    elif val > b:
        val = b

    return val


def scale_vector(vec: dict, size):
    magnitude = math.sqrt(vec["x"] ** 2 + vec["y"] ** 2)
    normalized_direction = {"x": vec["x"] / magnitude, "y": vec["y"] / magnitude}

    return {"x": int(normalized_direction["x"] * size), "y": int(normalized_direction["y"] * size)}


def acceleration(frame: dict, transport: dict, enemies_nearby: list):
    accel = {"x": 0, "y": 0}

    bounty_for_transport = bounty_finder.get_closest_bounty(frame["bounties"], frame["transports"])
    # TODO: write into accel to move to bounty
    accel['x'] = bounty_for_transport[transport["id"]]['x'] - transport['x']
    accel['y'] = bounty_for_transport[transport["id"]]['y'] - transport['y']

    # overwrite accel if we close to wall  
    if transport["x"] + transport["velocity"]["x"] > frame["mapSize"]["x"] * 0.95:
        accel["x"] = -frame["maxAccel"]
    elif transport["x"] + transport["velocity"]["x"] < frame["mapSize"]["x"] * 0.05:
        accel["x"] = frame["maxAccel"]
    if transport["y"] + transport["velocity"]["y"] > frame["mapSize"]["y"] * 0.95:
        accel["y"] = -frame["maxAccel"]
    elif transport["y"] + transport["velocity"]["y"] < frame["mapSize"]["y"] * 0.05:
        accel["y"] = frame["maxAccel"]

    return scale_vector(accel, frame["maxAccel"])
