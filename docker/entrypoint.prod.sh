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

python ./launch_redis_workers.py

redis-cli FLUSHALL

