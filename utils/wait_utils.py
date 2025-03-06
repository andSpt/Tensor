import os
import time


def wait_for_file_to_download(path_to_file: str, timeout=60) -> bool:
    seconds = 0
    while seconds < timeout:
        if os.path.isfile(path_to_file):
            return True
        time.sleep(1)
        seconds += 1
    return False