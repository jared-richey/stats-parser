#!/usr/bin/env bash
# NOTE: Times adjusted for UTC (6am EST, 7am EST, & 7:30am EST)
echo "0 10 * * * cd /app/tools && python3 soccer_parser.py > soccer_stats.txt >> /var/log/cron.log 2>&1"
echo "0 11 * * * cd /app/tools && python3 basketball_parser.py > basketball_stats.txt >> /var/log/cron.log 2>&1"
echo "15 11 * * * cd /app/tools && python3 nba_parser.py > nba_stats.txt >> /var/log/cron.log 2>&1"
echo "30 11 * * * cd /app/tools && python3 baseball_parser.py > baseball_stats.txt >> /var/log/cron.log 2>&1"
echo ""
             