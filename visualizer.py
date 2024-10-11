import rewind_client, sys, os, json


class Visualizer:
    rc = rewind_client.RewindClient()

    def draw_enemies(self, enemies_on_map):
        for enemy in enemies_on_map:
            self.rc.rectangle(enemy['x'], enemy['y'], enemy['x'] + 2, enemy['y'] + 2, self.rc.RED)
            # draw velocity vector
            self.rc.line(enemy["x"], enemy["y"], enemy["velocity"]['x'], enemy["velocity"]['y'], self.rc.DARK_RED)

    def draw_anomalies(self, anomalies_on_map):
        for anomaly in anomalies_on_map:
            self.rc.circle(anomaly["x"], anomaly["y"], anomaly["radius"], self.rc.BLUE)
            self.rc.circle(anomaly["x"], anomaly["y"], anomaly["effectiveRadius"], self.rc.DARK_BLUE)
            # draw velocity vector
            self.rc.line(anomaly["x"], anomaly["y"], anomaly["velocity"]['x'], anomaly["velocity"]['y'],
                         self.rc.DARK_BLUE)

    def draw_bounties(self, bounties):
        for bounty in bounties:
            self.rc.circle(bounty["x"], bounty["y"], bounty["radius"], self.rc.DARK_GREEN)

    def draw_transports(self, transports_on_map):
        for transport in transports_on_map:
            self.rc.rectangle(transport["velocity"]['x'], transport["velocity"]['y'],
                              transport["velocity"]['x'] + 1, transport["velocity"]['y'] + 1, self.rc.GREEN)
            # draw velocity vector
            self.rc.line(transport["x"], transport["y"], transport["velocity"]['x'], transport["velocity"]['y'],
                         self.rc.GREEN)

    def draw_frame(self, frame_to_draw: dict):
        self.draw_bounties(frame_to_draw["bounties"])
        self.draw_anomalies(frame_to_draw["anomalies"])
        self.draw_enemies(frame_to_draw["enemies"])
        self.draw_transports(frame_to_draw["transports"])

        self.rc.end_frame()


# draw from file if file name was provided in args
# to test this run rewind-viewer app, than:
# python ./visualizer.py sample_log.json 
if len(sys.argv) == 2:
    log_file_name = os.path.join("logs", sys.argv[1])
    print(log_file_name)
    f = open(log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    vs = Visualizer()

    for frame in log["frames"]:
        vs.draw_frame(frame)
