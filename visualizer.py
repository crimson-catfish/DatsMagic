import rewind_client, sys, os, json

CARPET_SIZE = 5

def clamp(val, a, b):
    if val < a:
        val = a
    elif val > b:
        val = b
    
    return val

class Visualizer:
    rc = rewind_client.RewindClient()

    def draw_enemies(self, enemies_on_map):
        for enemy in enemies_on_map:
            # calculate enemy direction
            x_dir = enemy["velocity"]['x'] * CARPET_SIZE * 2
            y_dir = enemy["velocity"]['y'] * CARPET_SIZE * 2

            half_size = CARPET_SIZE/2

            self.rc.circle(enemy['x'], enemy['y'], half_size, self.rc.RED, fill=True)

            # left_point = [enemy['x'] - half_size, enemy['y'] + half_size]
            # right_point = [enemy['x'] + half_size, enemy['y'] + half_size]

            # draw enemy 's triangle rotated towards direction
            # self.rc.triangle(left_point,
            #                  right_point,
            #                  [enemy['x'] + x_dir, enemy['y'] + y_dir],
            #                  self.rc.RED, fill=True)
            # draw velocity vector
            self.rc.line(enemy["x"], enemy["y"], enemy['x'] + x_dir, enemy['y'] + y_dir, self.rc.DARK_RED)

    def draw_anomalies(self, anomalies_on_map):
        for anomaly in anomalies_on_map:
            if anomaly["strength"] < 0:
                color = 0x2f00ff0f
            else:
                color = 0x2f000fff
                # Зеленые отталкивают, синие притягивают
            self.rc.circle(anomaly["x"], anomaly["y"], anomaly["radius"],  0x90f700ff, True)
            self.rc.circle(anomaly["x"], anomaly["y"], anomaly["effectiveRadius"], color, True)
            # draw velocity vector
            self.rc.line(anomaly["x"], anomaly["y"],
                         anomaly["x"] + anomaly["velocity"]['x'],
                         anomaly["y"] + anomaly["velocity"]['y'],
                         self.rc.DARK_BLUE)

    def draw_bounties(self, bounties):
        for bounty in bounties:
            self.rc.circle(bounty["x"], bounty["y"], bounty["radius"], self.rc.DARK_GREEN)

    def draw_transports(self, transports_on_map):
        for transport in transports_on_map:
            # self.rc.rectangle(transport["velocity"]['x'], transport["velocity"]['y'],
            #                   transport["velocity"]['x'] + 1, transport["velocity"]['y'] + 1, self.rc.GREEN)

            # calculate transport direction
            x_dir = transport["velocity"]['x'] * CARPET_SIZE * 2
            y_dir = transport["velocity"]['y'] * CARPET_SIZE * 2

            half_size = CARPET_SIZE/2

            self.rc.circle(transport['x'], transport['y'], half_size, self.rc.GREEN, fill=True)

            # draw transport's triangle rotated towards direction
            # self.rc.triangle([transport['x'] - half_size, transport['y'] - half_size],
            #                  [transport['x'] + half_size, transport['y'] + half_size],
            #                  [transport['x'] + x_dir, transport['y'] + y_dir],
            #                  self.rc.GREEN, fill=True)

            # draw velocity vector
            self.rc.line(transport["x"], transport["y"], transport["x"] + x_dir, transport['y'] + y_dir,
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
    f = open(log_file_name, "r", encoding="utf-8")
    log = json.load(f)

    vs = Visualizer()

    for frame in log["frames"]:
        vs.draw_frame(frame)
