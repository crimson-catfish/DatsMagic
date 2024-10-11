import rewind_client, sys, os, json
import math as m
import random

rc = rewind_client.RewindClient()
input()

# draw from file if file name was provided in args
# to test this run rewind-viewer app, than:
# python ./visualizer.py sample_log.json 
if len(sys.argv) == 2:
    log_file_name = os.path.join("logs", sys.argv[1])
    f = open(log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    for frame in log["frames"]:
        # draw_bounties(frame["bounties"])
        
        rc.end_frame()

# something like blocks
def draw_anomalies(anomalies_on_map):
    for i in anomalies_on_map:
        rc.circle(anomalies_on_map[i]["x"], anomalies_on_map[i]["y"],
                  anomalies_on_map[i]["radius"], rc.BLUE)

        rc.circle(anomalies_on_map[i]["x"], anomalies_on_map[i]["y"],
                  anomalies_on_map[i]["radius"], rc.BLUE)
    # rc.
    pass

# something like enemies
def draw_group_of_other_things():
    # rc.
    pass


def draw_bounties(bounties_on_map):
    for i in range(bounties_on_map):
        rc.circle(bounties_on_map[i]["x"], bounties_on_map[i]["y"], bounties_on_map[i]["radius"], rc.DARK_GREEN)



