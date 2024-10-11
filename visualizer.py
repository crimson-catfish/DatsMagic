import rewind_client, sys, os, json
import math as m
import random

a = 32 #for rectangle

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
        rc.circle(i["x"]*a, i["y"]*a, i["radius"]*a, rc.BLUE)
        rc.circle(i["x"]*a, i["y"]*a, i["effectiveRadius"]*a, rc.DARK_BLUE)
    pass


# something like enemies
def draw_enemies(enemies_on_map):
    for i in enemies_on_map:
        rc.rectangle(i['x']*a, i['y']*a, i['x']*a + a, i['y']*a + a, rc.RED)
    # rc.
    pass


def draw_bounties(bounties_on_map):
    for i in bounties_on_map:
        rc.circle(i["x"]*a, i["y"]*a, i["radius"]*a, rc.DARK_GREEN)




