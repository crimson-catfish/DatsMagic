from strategy import enemies_finder, shield, attacker, move


# may get paralleled for 5 transports 
def process_all_transports(frame: dict) -> dict:
    command = {"transports": []}

    for transport in frame["transports"]:
        if transport["status"] == "dead":
            continue

        transport_command = dict()
        transport_command["id"] = transport["id"]
        transport_command["activateShield"] = False

        enemies_nearby_transport = enemies_finder.nearby(frame, transport)

        if shield.needed(enemies_nearby_transport, transport):
            transport_command["activateShield"] = True

        attack = attacker.aim_one_hit(frame, transport, enemies_nearby_transport)
        if attack is not None:
            transport_command["attack"] = attack

        acceleration = move.acceleration(frame, transport, enemies_nearby_transport)
        if acceleration is not None:
            transport_command["acceleration"] = acceleration

        command["transports"].append(transport_command)

    return command
