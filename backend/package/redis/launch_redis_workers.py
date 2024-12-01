# ------------------------------------------------------------------------------ #
# @Author:        F. Paul Spitzner
# @Created:       2024-12-01 14:43:31
# @Last Modified: 2024-12-01 15:23:01
# ------------------------------------------------------------------------------ #
# Launches redis workers via python, instead of cli.
# The advantage is that this way we can read the package config, (and,
# e.g. set the number of workers and logging there)
# ------------------------------------------------------------------------------ #


import os
from typing import Optional

try:
    from ..logger import log
except ImportError:
    from package.logger import log


def start_workers(n: Optional[int] = None):
    if n is None:
        n = int(os.environ.get("NUM_REDIS_WORKERS", 4))

    log.info(f"Starting {n} redis workers")
    for i in range(n):
        worker_name = "Package_worker" + str(i)
        os.system(
            f'rq worker QVA --log-format "Preview worker $i: %(message)s" > /dev/null &'
        )
    log.info(f"Started {n} redis workers")


if __name__ == "__main__":
    start_workers()
