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
        rc.circle(anomaly["x"], anomaly["y"], anomaly["radius"], 0x90f700ff, True)
        rc.circle(anomaly["x"], anomaly["y"], anomaly["effectiveRadius"], 0x2f0000ff, True)
        # draw velocity vector
        rc.line(anomaly["x"], anomaly["y"], anomaly["velocity"]['x'], anomaly["velocity"]['y'], rc.DARK_BLUE)


def draw_bounties(bounties):
    for bounty in bounties:
        rc.circle(bounty["x"], bounty["y"], bounty["radius"], rc.DARK_GREEN)


def draw_transports(transports_on_map):
    for transport in transports_on_map:
        rc.rectangle(transport["velocity"]['x'], transport["velocity"]['y'],
                     transport["velocity"]['x']+1, transport["velocity"]['y']+1,rc.GREEN)
        # draw velocity vector
        rc.line(transport["x"], transport["y"], transport["velocity"]['x'], transport["velocity"]['y'], rc.GREEN)


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
        draw_enemies(frame["enemies"])
        draw_transports(frame["transports"])
        
        rc.end_frame()
