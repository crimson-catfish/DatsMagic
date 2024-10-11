import api
import rounds_utility


def ok(frame: dict) -> bool:
    if "error" in frame:
        print(frame["error"] + " " + str(frame["errCode"]))
        if frame["error"] == 'realm not found':
            print("time before next round: " + str(rounds_utility.time_before_next_round(api.rounds_info())))
        return False
    
    return True
