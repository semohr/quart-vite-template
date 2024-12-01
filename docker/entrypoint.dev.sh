#!/bin/sh

whoami
id
pwd


# ---------------------------------------------------------------------------- #
#                                  start redis                                 #
# ---------------------------------------------------------------------------- #

# running the server from inside the server dir makes imports and redis easier
cd /repo/backend

redis-server --daemonize yes

NUM_REDIS_WORKERS=4 python ./package/redis/launch_redis_workers.py
redis-cli FLUSHALL

# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                          start dev server and quart                          #
# ---------------------------------------------------------------------------- #
echo "Starting dev server and quart"
cd /repo/frontend
# pnpm run build:dev &  # use this for debugging with ios, port 5001 (no cors allowed)
pnpm run dev --host 0.0.0.0 & 

cd /repo/backend
./entrypoint.backend.dev.sh
