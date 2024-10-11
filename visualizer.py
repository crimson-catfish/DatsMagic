import rewind_client, sys, os, json
import math as m
import random
                

def draw_bounties(bounties_on_map):
    for i in bounties_on_map:
        rc.circle(bounties_on_map[i]["x"], bounties_on_map[i]["y"], bounties_on_map[i]["radius"], rc.DARK_GREEN)


rc = rewind_client.RewindClient()

# draw from file if file name was provided in args
# to test this run rewind-viewer app, than:
# python ./visualizer.py sample_log.json 
if len(sys.argv) == 2:
    log_file_name = os.path.join("logs", sys.argv[1])
    f = open(log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    for frame in log["frames"]:
        draw_bounties(frame["bounties"])

        rc.end_frame()
