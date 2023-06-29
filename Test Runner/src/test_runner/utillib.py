## version 1.0

import re
from functools import wraps
import threading


# Windows version
def timeout(seconds, error_message="Dieser Test hat die Zeitlimite überschritten."):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = [None]  # Use a mutable object to store the result

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    result[0] = e

            timer = threading.Timer(seconds, target)

            try:
                timer.start()
                timer.join()
            except Exception as e:
                raise TimeoutError(error_message + f" ({seconds} Sekunden)") from e
            finally:
                timer.cancel()

            if isinstance(result[0], Exception):
                raise result[0]

            return result[0]

        return wrapper

    return deco


def regex_find(regex, target, inOrder=False, mode="and"):
    match = False

    for ex in regex:
        res = re.search(ex, target)
        if res is None:
            if mode == "or":
                continue
            return False
        else:
            match = True

        if inOrder:
            end = res.span()[1]
            target = target[end:]

    return match
