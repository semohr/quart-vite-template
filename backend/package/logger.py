import logging
import os


def setup_logging() -> None:
    global log

    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    logging.basicConfig(
        format="%(relativeCreated)d [%(levelname)-4s] %(name)s - %(message)s %(filename)s:%(lineno)d",
        level=os.getenv("LOG_LEVEL_DEPENDENCIES", logging.WARNING),
    )
    rq_name = os.getenv("RQ_JOB_ID", None)
    if rq_name:
        log = logging.getLogger(f"rq-worker.{rq_name[0:8]}")
    else:
        log = logging.getLogger("main-worker")
    log.setLevel(os.getenv("LOG_LEVEL_MAIN", logging.INFO))

    log.info("Logging initialized")


log = None
setup_logging()
