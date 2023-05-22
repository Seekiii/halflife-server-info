import a2s
import json

def get_players(ip):
    ip = ip.split(":")
    data = a2s.players((ip[0], int(ip[1])))
    json_data = []
    for item in data:
        json_data.append({
            "id":item.index,
            "name":item.name,
            "score":item.score,
            "duration":item.duration
        })
    return json_data

def get_info(ip):
    ip = ip.split(":")
    data = a2s.info((ip[0], int(ip[1])))
    json_data = {}

    DataTipovi = {
        "d":"Dedicated Server",
        "l":"Non-Dedicated Server",
        "p": "SourceTV (Proxy)"
    }

    DataPlatform = {
        "l":"Linux",
        "w":"Windows",
        "m": "MAC"
    }

    json_data = {
        "protocol":data.protocol,
        "server_name":data.server_name,
        "map_name":data.map_name,
        "game":data.game,
        "folder":data.folder,
        "players":data.player_count,
        "max_players":data.max_players,
        "bots":data.bot_count,
        "server_type":DataTipovi[data.server_type],
        "platform":DataPlatform[data.platform.lower()],
        "pass_protected":data.password_protected,
        "vac":data.vac_enabled,
        "ping":data.ping
    }
    return json_data



ip = "192.168.1.0:12345"
players = get_players(ip)
info = get_info(ip)

print("=================== PLAYERS ===================")
print(json.dumps(players,indent=4))
print("=================== INFO ===================")
print(json.dumps(info,indent=4))

#pip install python-a2s