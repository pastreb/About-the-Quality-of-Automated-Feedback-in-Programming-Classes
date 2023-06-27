## version 1.0

import re
from functools import wraps
import threading

def timeout(seconds, error_message='Dieser Test hat die Zeitlimite überschritten.'):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = [None]
            error = [None]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    error[0] = e

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(seconds)

            if thread.is_alive():
                thread.join()  # Wait for the thread to finish (blocking)
                raise TimeoutError(error_message + f' ({seconds} Sekunden)')

            if error[0] is not None:
                raise error[0]

            return result[0]

        return wrapper

    return deco

def regex_find(regex, target, inOrder=False, mode='and'):
    
    match = False

    for ex in regex:
        res = re.search(ex, target)
        if res is None:
            if mode=='or':
                continue
            return False
        else:
            match = True
    
        if inOrder:
            end = res.span()[1]
            target = target[end:]
    
    return match