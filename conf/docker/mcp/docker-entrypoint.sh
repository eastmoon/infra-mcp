#!/bin/sh
set -e

## Startup container
if [ -z "${1}" ]; then
    python main.py
fi

exec "$@"
