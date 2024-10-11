import math


# simplest aim - hit low hp enemy and don't shoot yourself
# TODO: make it's copy and implement more complicated aim strategy like shooting someone more than one hit hp, and taking bounty to credit 
def aim_one_hit(frame: dict, transport: dict, enemies_nearby: list):
    if transport["attackCooldownMs"] > 0:
        return None

    for enemy_nearby in enemies_nearby:
        if enemy_nearby["enemy"]["shieldLeftMs"] > 0:
            continue

        if enemy_nearby["enemy"]["health"] <= frame["attackDamage"]:
            # if enemy too close
            if enemy_nearby["sqr_distance"] <= frame["attackExplosionRadius"] ** 2:
                # all below is to avoid shooting self
                direction = {"x": enemy_nearby["enemy"]["x"] - transport["x"],
                             "y": enemy_nearby["enemy"]["y"] - transport["y"]}

                magnitude = math.sqrt(direction["x"] ** 2 + direction["y"] ** 2)

                normalized_direction = {"x": direction["x"] / magnitude,
                                        "y": direction["y"] / magnitude}

                return {"x": transport["x"] + normalized_direction["x"] * enemy_nearby["sqr_distance"] * 1.01,
                        "y": transport["y"] + normalized_direction["y"] * enemy_nearby["sqr_distance"] * 1.01}

            # if enemy too far
            if enemy_nearby["sqr_distance"] > frame["attackRange"] ** 2:
                # TODO: don't try to shoot further than we can. try to hit enemy with explosion area instead 
                return None

            return {"x": enemy_nearby["enemy"]["x"], "y": enemy_nearby["enemy"]["y"]}
