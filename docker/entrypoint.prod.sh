#!/bin/sh

echo "Running as"
id

cd /repo

mkdir -p /repo/log

# ------------------------------------------------------------------------------------ #
#                                     start server                                    #
# ------------------------------------------------------------------------------------ #

# running the server from inside the server dir makes imports and redis easier
cd /repo/server

redis-server --daemonize yes

NUM_REDIS_WORKERS=4 python ./package/redis/launch_redis_workers.py

redis-cli FLUSHALL

./entrypoint.backend.prod.sh &
