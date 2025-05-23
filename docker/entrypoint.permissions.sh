#!/bin/sh

if [ ! -z "$USER_ID" ] && [ ! -z "$GROUP_ID" ]; then
    echo "Updating UID to $USER_ID and GID to $GROUP_ID"
    groupmod -g $GROUP_ID appuser
    usermod -u $USER_ID -g $GROUP_ID appuser
    chown -R appuser:appuser /home/appuser
    chown -R appuser:appuser /repo
fi
