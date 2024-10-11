import rewind_client, sys, os, json
import math as m
import random

rc = rewind_client.RewindClient()
input()

# draw from file if file name was provided in args
if len(sys.argv) == 2:
    log_file_name = os.path.join("logs", sys.argv[1])
    f = open("logs/" + log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    for frame in log["frames"]:
        # read group type, draw it
        pass

# something like blocks
def draw_group_of_things():
    # rc.
    pass

# something like enemies
def draw_group_of_other_things():
    # rc.
    pass


def draw_bounties(bounties_on_map):
    for i in bounties_on_map:
        rc.circle(bounties_on_map[i]["x"], bounties_on_map[i]["y"], bounties_on_map[i]["radius"], rc.DARK_GREEN)




