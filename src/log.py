import sys
import os
import logging

def log_write(dt, status, app, content):
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    log_dir = os.path.join(script_dir, "log")
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(__name__)
    log_path = os.path.join(log_dir, f"rpc{dt}.log")
    logging.basicConfig(filename=log_path, encoding="utf-8", level=logging.INFO, format="[%(asctime)s] %(message)s")
    if status == "ok":
        if app:
            info_text = f"NTE is running(PID: {app}). Executes an RPC function."
        else:
            info_text = f"NTE is not running. waiting..."
        logger.info(info_text)
    elif status == "error":
        logger.error(f"Unexpected error occurred.\n{content}")

