def get_closest_bounty(bounties: dict, transports: dict) -> dict:
    bounty_for_carpet = {transports[0]["id"]: None,
                         transports[1]["id"]: None,
                         transports[2]["id"]: None,
                         transports[3]["id"]: None,
                         transports[4]["id"]: None}
    for transport in transports:
        bounty_x = None
        bounty_y = None
        vector_length_squared = 6000
        x = transport["x"] + transport["velocity"]["x"] * 2
        y = transport["y"] + transport["velocity"]["y"] * 2
        for bounty in bounties:
            vector = [bounty["x"] - x, bounty["y"] - y]
            if vector[0] ** 2 + vector[1] ** 2 < vector_length_squared:
                bounty_x = bounty["x"]
                bounty_y = bounty["y"]
                vector_length_squared = vector[0] ** 2 + vector[1] ** 2
        bounty_for_carpet[transport["id"]] = {'x': bounty_x, 'y': bounty_y}
    return bounty_for_carpet
