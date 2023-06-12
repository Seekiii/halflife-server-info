<h1>Half-Life Server Info</h1>

- Games from which servers you can obtain information:: [ `Counter Strike` / `Half-Life` / `Call Of Duty` / `Team Fortress 2` ]

<h1>Usage:</h1>

- Install "a2s" module: ```pip install python-a2s```
- Edit `app.py` file and change ip `192.168.1.0:12345` to server IP. (line: 53)
- Run app: `python app.py`

<h1>Informations:</h1>

- `a2s` is a module that provides functionality for querying game servers using the A2S protocol (Server queries in the Source engine). It allows you to obtain information about players, server settings, and more.

<h1>Other: </h1>

- The information you will get from `get_players(ip)`:
```json
[
    {
        "id": 0,
        "name": "Mohawk",
        "score": 27,
        "duration": 2999.144775390625
    },
    {
        "id": 1,
        "name": "Jaric Zivadin",
        "score": 1,
        "duration": 104.42972564697266
    }
]
``` 

- The information you will get from `get_info(ip)`:
```json
{
    "protocol": 47,
    "server_name": "Emirates-KiNGS \u4e97 ||\u0347\u033fP\u0347\u033fU\u0347\u033fB\u0347\u033fL\u0347\u033fI\u0347\u033fC\u0347\u033f| \u272a",
    "map_name": "de_dust2",
    "game": "Counter-Strike",
    "folder": "cstrike",
    "players": 32,
    "max_players": 32,
    "bots": 0,
    "server_type": "Dedicated Server",
    "platform": "Linux",
    "pass_protected": false,
    "vac": true,
    "ping": 0.0470000000204891
}
```
