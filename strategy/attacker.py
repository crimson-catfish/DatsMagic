import math


# simplest aim - hit low hp enemy and don't shoot yourself
# TODO: make it's copy and implement more complicated aim strategy like shooting someone more than one hit hp, and taking bounty to credit 
def aim_one_hit(frame: dict, transport: dict, enemies_nearby: list):
    if transport["attackCooldownMs"] > 0:
        return None

    damage = frame["attackDamage"]
    target_nearby = None

    for enemy_nearby in enemies_nearby:
        if enemy_nearby["enemy"]["shieldLeftMs"] > 0:
            continue

        if target_nearby is None or int(enemy_nearby["enemy"]["health"] / damage) < int(
                target_nearby["enemy"]["health"] / damage) or (
                int(enemy_nearby["enemy"]["health"] / damage) == int(target_nearby["enemy"]["health"] / damage) and
                enemy_nearby["enemy"]["killBounty"] > target_nearby["enemy"]["killBounty"]):
            target_nearby = enemy_nearby

    if target_nearby is None:
        return None

    direction = {"x": target_nearby["enemy"]["x"] - transport["x"],
                 "y": target_nearby["enemy"]["y"] - transport["y"]}

    magnitude = math.sqrt(direction["x"] ** 2 + direction["y"] ** 2)

    normalized_direction = {"x": direction["x"] / magnitude,
                            "y": direction["y"] / magnitude}

    # if enemy too close
    if target_nearby["sqr_distance"] <= frame["attackExplosionRadius"] ** 2:
        # all below is to avoid shooting self

        return {"x": int(transport["x"] + normalized_direction["x"] * frame["attackExplosionRadius"] * 1.01),
                "y": int(transport["y"] + normalized_direction["y"] * frame["attackExplosionRadius"] * 1.01)}

    # if enemy too far
    if target_nearby["sqr_distance"] > frame["attackRange"] ** 2:
        return {"x": int(transport["x"] + normalized_direction["x"] * frame["attackRange"] * 0.9),
                "y": int(transport["y"] + normalized_direction["y"] * frame["attackRange"] * 0.9)}

    return {"x": int(target_nearby["enemy"]["x"]), "y": int(target_nearby["enemy"]["y"])}
