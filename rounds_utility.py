from datetime import datetime


def time_before_next_round(rounds_info):
    now = datetime.fromisoformat(rounds_info['now'][:-1])

    upcoming_rounds = [
        round for round in rounds_info['rounds']
        if datetime.fromisoformat(round['startAt'][:-1]) > now
    ]

    if not upcoming_rounds:
        return None  # No upcoming rounds

    next_round = min(upcoming_rounds, key=lambda r: r['startAt'])
    start_time_next_round = datetime.fromisoformat(next_round['startAt'][:-1])

    time_difference = start_time_next_round - now
    return time_difference.total_seconds()

