import json


class Logger:
    def __init__(self, current_round: str):
        self.file = open("logs/round" + current_round.replace(":", ".") + ".json", 'w+')
        self.file.write("{\"frames\": [\n")
        self.first = True

    def log(self, frame_data: dict):
        frame_data_json = json.dumps(frame_data)
        if not self.first:
            self.file.write(",")
        self.file.write(frame_data_json)
        self.first = False

    def __del__(self):
        self.file.write("\n]}")
        self.file.close()
