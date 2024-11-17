#!/bin/sh

whoami
id
pwd

cd /repo/frontend

# pnpm run build:dev &  # use this for debugging with ios, port 5001 (no cors allowed)
pnpm run dev & # normal dev, port 5173


mkdir -p /repo/log

cd /repo


export FLASK_ENV=development
export FLASK_DEBUG=1

# ------------------------------------------------------------------------------------ #
#                                     start server                                    #
# ------------------------------------------------------------------------------------ #

# running the server from inside the server dir makes imports and redis easier
cd /repo/server

redis-server --daemonize yes

python ./launch_redis_workers.py

redis-cli FLUSHALL

# we need to run with one worker for socketio to work (but need at least threads for SSEs)
# sufficient timout for the interactive import sessions, which may take a couple of minutes
# TODO

# if we need to debug the continaer without running the webserver:
# tail -f /dev/null
