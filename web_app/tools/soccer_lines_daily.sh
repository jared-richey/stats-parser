#!/usr/bin/env bash

set -e

SCRIPT_PATH=$(readlink -f "$0")

my_dir=$(dirname "$SCRIPT_PATH")

echo "Running curl command to retrieve soccer stats" 
curl -s -H "Content-type: text/html" https://www.espn.com/soccer/scoreboard > $my_dir/soccer_lines.html

echo "Parsing soccer stats" 
python3 $my_dir/soccer_parser.py > $my_dir/soccer_stats.txt