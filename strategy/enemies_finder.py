def nearby(frame: dict, transport: dict) -> list:
    enemies_nearby = []
    for enemy in frame["enemies"]:
        if enemy["status"] == "dead":
            continue

        sqr_distance = (transport["x"] - enemy["x"]) ** 2 + (transport["y"] - enemy["y"]) ** 2
        if sqr_distance > (frame["attackRange"] + frame["attackExplosionRadius"]) ** 2:
            continue

        enemy_nearby = {"enemy": enemy, "sqr_distance": sqr_distance}
        enemies_nearby.append(enemy_nearby)

    return enemies_nearby
