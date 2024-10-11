# detect if it's time to use shield
def needed(enemies_nearby: list, transport: dict) -> bool:
    return (len(enemies_nearby) > 1 or
            (len(enemies_nearby) == 1 and (
                    enemies_nearby[0]["enemy"]["health"] > transport["health"] or
                    enemies_nearby[0]["enemy"]["shieldLeftMs"] > 0)))
