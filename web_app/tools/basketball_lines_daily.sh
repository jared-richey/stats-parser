#!/usr/bin/env bash

set -e

SCRIPT_PATH=$(readlink -f "$0")

my_dir=$(dirname "$SCRIPT_PATH")

echo "Running curl command to retrieve basketball stats" 
curl -s -H "Content-type: text/html" https://www.espn.com/mens-college-basketball/lines > $my_dir/basketball_lines.html

echo "Parsing basketball stats"
python3 $my_dir/basketball_parser.py > $my_dir/basketball_stats.txt
