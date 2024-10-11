import json


class Logger:
    def __init__(self, current_round: str):
        self.file = open("logs/round" + current_round + ".json", 'w+')
        self.file.write("{\"frames\": [\n")

    def log(self, frame_data: dict):
        frame_data_json = json.dumps(frame_data)
        self.file.write(frame_data_json + ",")

    def __del__(self):
        self.file.write("\n]}")
        self.file.close()
