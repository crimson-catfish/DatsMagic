import math

import anomaly_finder
from strategy import bounty_finder


def clamp_vector(vec: dict, size):
    magnitude = math.sqrt(vec["x"] ** 2 + vec["y"] ** 2)

    if magnitude <= size:
        return vec

    normalized_direction = {"x": vec["x"] / magnitude, "y": vec["y"] / magnitude}

    return {"x": int(normalized_direction["x"] * size), "y": int(normalized_direction["y"] * size)}


def acceleration(frame: dict, transport: dict, enemies_nearby: list):
    # move to center by default
    center = {"x": frame["mapSize"]["x"] / 2 - transport["x"], "y": frame["mapSize"]["y"] / 2 - transport["y"]}
    clamped_center = clamp_vector(center, frame["maxSpeed"] * 0.3)
    accel = {"x": clamped_center["x"] - transport["velocity"]["x"],
             "y": clamped_center["y"] - transport["velocity"]["y"]}

    bounty_for_transport = bounty_finder.get_closest_bounty(frame["bounties"], frame["transports"])
    if bounty_for_transport[transport["id"]]['x'] is not None:
        accel['x'] = bounty_for_transport[transport["id"]]['x'] - transport['x'] - transport["velocity"]["x"]
        accel['y'] = bounty_for_transport[transport["id"]]['y'] - transport['y'] - transport["velocity"]["y"]

    # cancel anomaly effects
    accel['x'] -= transport["anomalyAcceleration"]['x']
    accel['y'] -= transport["anomalyAcceleration"]['y']

    for enemy_nearby in enemies_nearby:
        # ignore enemies too far
        if enemy_nearby["sqr_distance"] > (transport["velocity"]["x"] ** 2 + transport["velocity"]["y"] ** 2) * 10:
            continue

        transport_predicted_position = {"x": transport["x"] + transport["velocity"]["x"] * 2,
                                        "y": transport["y"] + transport["velocity"]["y"] * 2}

        enemy_predicted_position = {"x": enemy_nearby["enemy"]["x"] + (enemy_nearby["enemy"]["velocity"]["x"] * 2),
                                    "y": enemy_nearby["enemy"]["y"] + (enemy_nearby["enemy"]["velocity"]["y"] * 2)}

        sqr_predicted_distance = (transport_predicted_position["x"] - enemy_predicted_position["x"]) ** 2 + (
                transport_predicted_position["y"] - enemy_predicted_position["y"]) ** 2

        if sqr_predicted_distance < 2500:
            accel["x"] = transport["x"] - enemy_predicted_position["x"] - transport["velocity"]["x"]
            accel["y"] = transport["y"] - enemy_predicted_position["y"] - transport["velocity"]["y"]

    # overwrite accel if we close to wall  
    if transport["x"] + transport["velocity"]["x"] > frame["mapSize"]["x"] * 0.95:
        accel["x"] = -frame["maxAccel"]
    elif transport["x"] + transport["velocity"]["x"] < frame["mapSize"]["x"] * 0.05:
        accel["x"] = frame["maxAccel"]
    if transport["y"] + transport["velocity"]["y"] > frame["mapSize"]["y"] * 0.95:
        accel["y"] = -frame["maxAccel"]
    elif transport["y"] + transport["velocity"]["y"] < frame["mapSize"]["y"] * 0.05:
        accel["y"] = frame["maxAccel"]

    return clamp_vector(accel, frame["maxAccel"])
