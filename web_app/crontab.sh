#!/usr/bin/env bash
# NOTE: Times adjusted for UTC (6am EST, 7am EST, & 7:30am EST)
echo "0 10 * * * cd /app/tools && ./soccer_stats_daily.sh >> /var/log/cron.log 2>&1"
echo "0 11 * * * cd /app/tools && ./basketball_stats_daily.sh >> /var/log/cron.log 2>&1"
echo "30 11 * * * cd /app/tools && ./baseball_stats_daily.sh >> /var/log/cron.log 2>&1"
echo ""
             