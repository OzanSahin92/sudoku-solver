#!/bin/bash --login
set -e

conda activate sudsolv
exec "$@"
