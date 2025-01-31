import json

import requests

token = "66fbdc38b2e2466fbdc38b2e27 "
url_main = "https://games.datsteam.dev/"
url_test = "https://games-test.datsteam.dev/"
game_name = "magcarp"
auth_header = {"X-Auth-Token": token}

url = url_test


def participate(test=False):
    global url
    if test:
        url = url_test
    else:
        url = url_main

    req = {"transports": []}

    return json.loads(
        requests.post(url + "play/" + game_name + "/player/move", headers=auth_header, json=req).content.decode(
            'utf-8'))


def rounds_info():
    return json.loads(requests.get(url + "rounds/" + game_name, headers=auth_header).content.decode('utf-8'))


def send_command(command: dict):
    return json.loads(
        requests.post(url + "play/" + game_name + "/player/move", headers=auth_header, json=command).content.decode(
            'utf-8'))
