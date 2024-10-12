# TODO: process movement and don't kill yourself in the process
from strategy import bounty_finder


def acceleration(frame: dict, transport: dict, enemies_nearby: list):

    bounty_for_transport = bounty_finder.get_closest_bounty(frame["bounties"], frame["transports"])
    print(bounty_for_transport)
    
    accel = {"x": 0, "y": 0}

    if transport["x"] + transport["velocity"]["x"] > frame["mapSize"]["x"] * 0.99:
        accel["x"] = -frame["maxAccel"]
    elif transport["x"] + transport["velocity"]["x"] < frame["mapSize"]["x"] * 0.01:
        accel["x"] = frame["maxAccel"]
        
    if transport["y"] + transport["velocity"]["y"] > frame["mapSize"]["y"] * 0.99:
        accel["y"] = -frame["maxAccel"]
    elif transport["y"] + transport["velocity"]["y"] < frame["mapSize"]["y"] * 0.01:
        accel["y"] = frame["maxAccel"]

    return accel