from threading import Thread
from src.tray import taskTray
from datetime import datetime
from src.proc import process_check
from src.rpc import rpc
from src.settings import get_userdata
from src.log import log_write
import time

def app_run():
    dt_now = datetime.now().strftime("%Y%m%d%H%M%S%f")
    try:
        player_data = get_userdata()
    except Exception as e:
        log_write(dt=dt_now, status="error", app=None, content=e)
        return
    while True:
        try:
            pid = process_check()
            if pid:
                log_write(dt=dt_now, status="ok", app=pid, content=None)
                rpc(player_data)
            else:
                log_write(dt=dt_now, status="ok", app=False, content=None)
            time.sleep(15)
        except Exception as e:
            log_write(dt=dt_now, status="error", app=None, content=e)
            break

if __name__ == "__main__":
    Thread(target=app_run, daemon=True).start()
    tray = taskTray()
    tray.run_program()