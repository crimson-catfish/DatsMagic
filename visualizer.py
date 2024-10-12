import rewind_client, sys, os, json


class Visualizer:
    def __init__(self, map_size: dict):
        self.rc = rewind_client.RewindClient()
        self.rc.set_options(layer=1, permanent=True)
        self.rc.rectangle(0, 0, map_size["x"], map_size["y"], self.rc.BACKGROUND, fill=True)
        self.rc.end_frame()

    def draw_enemies(self, enemies_on_map, transport_radius):
        for enemy in enemies_on_map:
            # calculate enemy direction
            x_dir = enemy["velocity"]['x']
            y_dir = enemy["velocity"]['y']

            self.rc.circle(enemy['x'], enemy['y'], transport_radius, self.rc.RED, fill=True)

            # draw velocity vector
            self.rc.line(enemy["x"], enemy["y"], enemy['x'] + x_dir, enemy['y'] + y_dir, self.rc.DARK_RED)

    def draw_anomalies(self, anomalies_on_map):
        for anomaly in anomalies_on_map:
            if anomaly["strength"] < 0:
                color = 0x2f00ff0f
            else:
                color = 0x2f000fff
                # Зеленые отталкивают, синие притягивают
            self.rc.circle(anomaly["x"], anomaly["y"], anomaly["radius"], 0x90f700ff, True)
            self.rc.circle(anomaly["x"], anomaly["y"], anomaly["effectiveRadius"], color, True)
            # draw velocity vector
            self.rc.line(anomaly["x"], anomaly["y"],
                         anomaly["x"] + anomaly["velocity"]['x'],
                         anomaly["y"] + anomaly["velocity"]['y'],
                         self.rc.DARK_BLUE)

    def draw_bounties(self, bounties):
        for bounty in bounties:
            self.rc.circle(bounty["x"], bounty["y"], bounty["radius"], self.rc.GOLD, True)

    def draw_transports(self, transports_on_map, transport_radius, attack_radius):
        for transport in transports_on_map:
            # calculate transport direction
            x_dir = transport["velocity"]['x']
            y_dir = transport["velocity"]['y']

            self.rc.circle(transport['x'], transport['y'], transport_radius, self.rc.GREEN, fill=True)

            # draw velocity vector
            self.rc.line(transport["x"], transport["y"], transport["x"] + x_dir, transport['y'] + y_dir,
                         self.rc.GREEN)

            # draw shoot radius
            self.rc.circle(transport['x'], transport['y'], attack_radius, self.rc.GREEN)

    def draw_hp(self, transports, enemies):
        for transport in transports:
            self.rc.circle_popup(transport['x'],
                                 transport['y'],
                                 50, "ally health: " + str(transport["health"]))
        for enemy in enemies:
            self.rc.circle_popup(enemy['x'],
                                 enemy['y'],
                                 50, "enemy health: " + str(enemy["health"]))

    def draw_constants(self, frame):
        self.rc.message("maxAccel" + ': ' + str(frame["maxAccel"]))
        self.rc.message("maxSpeed" + ': ' + str(frame["maxSpeed"]))
        self.rc.message("points" + ': ' + str(frame["points"]))

    def draw_bounty_howmany(self, bounties):
        for bounty in bounties:
            self.rc.circle_popup(bounty['x'],
                                 bounty['y'],
                                 30, "points: " + str(bounty["points"]))

    def draw_frame(self, frame_to_draw: dict):
        self.draw_constants(frame_to_draw)
        self.draw_bounty_howmany(frame_to_draw["bounties"])
        self.draw_hp(frame_to_draw["transports"], frame_to_draw["enemies"])
        self.draw_bounties(frame_to_draw["bounties"])
        self.draw_anomalies(frame_to_draw["anomalies"])
        self.draw_enemies(frame_to_draw["enemies"], frame_to_draw["transportRadius"])
        self.draw_transports(frame_to_draw["transports"], frame_to_draw["transportRadius"],
                             frame_to_draw["attackRange"])
        self.rc.end_frame()

# draw from file if file name was provided in args
# to test this run rewind-viewer app, than:
# python ./visualizer.py sample_log.json 
if len(sys.argv) == 2:
    log_file_name = os.path.join("logs", sys.argv[1])
    f = open(log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    vs = Visualizer(log["frames"][0]["mapSize"])

    for frame in log["frames"]:
        vs.draw_frame(frame)
