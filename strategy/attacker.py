import math


# simplest aim - hit enemy and don't shoot yourself
def aim_one_target(frame: dict, transport: dict, enemies_nearby: list):
    if transport["attackCooldownMs"] > 0:
        return None

    for enemy_nearby in enemies_nearby:
        if enemy_nearby["enemy"]["shieldLeftMs"] > 0:
            continue

        if enemy_nearby["enemy"]["health"] <= frame["attackDamage"]:
            if enemy_nearby["sqr_distance"] > frame["attackExplosionRadius"]:
                return {"x": enemy_nearby["enemy"]["x"], "y": enemy_nearby["enemy"]["y"]}

            direction = {"x": enemy_nearby["enemy"]["x"] - transport["x"],
                         "y": enemy_nearby["enemy"]["y"] - transport["y"]}

            magnitude = math.sqrt(direction["x"] ** 2 + direction["y"] ** 2)

            normalized_direction = {"x": direction["x"] / magnitude,
                                    "y": direction["y"] / magnitude}

            return {"x": transport["x"] + normalized_direction["x"] * enemy_nearby["sqr_distance"],
                    "y": transport["y"] + normalized_direction["y"] * enemy_nearby["sqr_distance"]}

        return None
