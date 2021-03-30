#!/bin/bash --login
set -e

conda activate sudoku-solver
exec "$@"
