import psutil

def process_check():
    for proc in psutil.process_iter():
        try:
            get_proc = proc.exe()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
        else:
            if "HTGame.exe" in get_proc:  # Debug -> pycharm64.exe
                return proc.pid
    return False