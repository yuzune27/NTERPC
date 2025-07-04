import time
from discordrp import Presence
from src.settings import read_ver, get_userdata
from src.proc import process_check
from src.RPCData import RPCData, TimeStamps, Assets, convert_to_dict
from src.PlayerData import PlayerData

def visible_set(uid: int, uid_visible: bool):
    if uid_visible:
        uid_str = f"UID: {uid}"
    else:
        uid_str = "UID: ****"
    return uid_str

def rpc(player_data: PlayerData):
    cid = "1389789692878393424"

    start_time = int(time.time())
    version = read_ver()

    state = visible_set(player_data.UID, player_data.UIDVisible)

    data = RPCData(
        assets=Assets(
            large_image="nte_ico",
            large_text="NTERPC",
            small_image="nte_ico_s",
            small_text="v" + version,
        ),
        timestamps=TimeStamps(start=start_time),
        details=player_data.Player,
        state=state
    )

    with Presence(cid) as presence:
        presence.set(convert_to_dict(data))
        while True:
            if process_check():
                if player_data != get_userdata():
                    player_data = get_userdata()
                    data.details = player_data.Player
                    data.state = visible_set(player_data.UID, player_data.UIDVisible)

                    presence.set(convert_to_dict(data))
                time.sleep(15)
            else:
                break