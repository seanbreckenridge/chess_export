import time
from typing import Any, Optional
from functools import partial

import click
import requests

eprint = partial(click.echo, err=True)

Json = Any

BACKOFF_TIME = 15
SLEEP_TIME = 0.5


def safe_request(
    url: str,
    sleep_time: Optional[float] = None,
    backoff_time: Optional[float] = None,
    **kwargs: Any,
) -> requests.Response:
    eprint(f"Requesting {url}")
    resp: requests.Response = requests.get(url, **kwargs)
    if resp.status_code == 429:
        eprint("Error: Recieved 429 error, waiting...")
        time.sleep(backoff_time or BACKOFF_TIME)
        # recursive call
        kwargs["backoff_time"] = backoff_time
        kwargs["sleep_time"] = sleep_time
        return safe_request(url, **kwargs)
    else:
        if resp.status_code != 200:
            eprint(f"Warning: {url} recieved non 200 exit code: {resp.status_code}")
        time.sleep(sleep_time or SLEEP_TIME)
        return resp
