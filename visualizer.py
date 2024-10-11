import rewind_client, sys, os, json
import math as m
import random

a = 1


def draw_enemies(enemies_on_map):
    for enemy in enemies_on_map:
        rc.rectangle(enemy['x']*a, enemy['y']*a, enemy['x']*a + a, enemy['y']*a + a, rc.RED)
        # draw velocity vector
        rc.line(enemy["x"], enemy["y"], enemy["velocity"]['x'], enemy["velocity"]['y'], rc.DARK_RED)


def draw_anomalies(anomalies_on_map):
    for anomaly in anomalies_on_map:
        rc.circle(anomaly["x"], anomaly["y"], anomaly["radius"], rc.BLUE)
        rc.circle(anomaly["x"], anomaly["y"], anomaly["effectiveRadius"], rc.DARK_BLUE)

        # draw velocity vector
        rc.line(anomaly["x"], anomaly["y"], anomaly["velocity"]['x'], anomaly["velocity"]['y'], rc.DARK_BLUE)


def draw_bounties(bounties):
    for bounty in bounties:
        rc.circle(bounty["x"], bounty["y"], bounty["radius"], rc.DARK_GREEN)


rc = rewind_client.RewindClient()

# draw from file if file name was provided in args
# to test this run rewind-viewer app, than:
# python ./visualizer.py sample_log.json 
if len(sys.argv) == 2:
    log_file_name = os.path.join("logs", sys.argv[1])
    print(log_file_name)
    f = open(log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    for frame in log["frames"]:
        draw_bounties(frame["bounties"])
        draw_anomalies(frame["anomalies"])
        
        rc.end_frame()
