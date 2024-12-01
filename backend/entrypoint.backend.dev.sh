#!/bin/sh

# see for available cli options:
# https://www.uvicorn.org/#command-line-options
uvicorn package:create_app --port 80 \
    --reload \
    --factory 

# if we need to debug the container without running the webserver:
# tail -f /dev/null