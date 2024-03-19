echo "0 11 * * * cd /app/tools && ./basketball_lines_daily.sh >> /var/log/cron.log 2>&1"
echo "0 6 * * * cd /app/tools && ./soccer_lines_daily.sh >> /var/log/cron.log 2>&1"
echo ""
             