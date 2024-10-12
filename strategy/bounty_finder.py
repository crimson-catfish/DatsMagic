def get_closest_bounty(bounties: dict, transports: dict) -> dict:
    bounty_for_carpet = {transports[0]["id"]: None,
                         transports[1]["id"]: None,
                         transports[2]["id"]: None,
                         transports[3]["id"]: None,
                         transports[4]["id"]: None}
    for transport in transports:
        bounty_x = None
        bounty_y = None
        vector_length_squared = 9999999999
        x = transport["x"]
        y = transport["y"]
        for bounty in bounties:
            vector = [bounty["x"] - x, bounty_y - y]
            if vector[0]**2 + vector[1]**2 < vector_length_squared:
                bounty_x = bounty[x]
                bounty_y = bounty[y]
                vector_length_squared = vector[0]**2 + vector[1]**2
        bounty_for_carpet[transports[0]["id"]] = [bounty_x, bounty_y]
    return bounty_for_carpet
