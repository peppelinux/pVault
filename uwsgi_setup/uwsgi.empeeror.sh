#!/bin/sh
### BEGIN INIT INFO
# Provides:          pvault_uwsgi
# Required-Start:    mysql nginx
# Required-Stop:
# Should-Start:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Create dynamic part of /etc/motd
# Description:       /etc/motd is user-editable and static.  This script
#                    creates the initial dynamic part, by default the
#                    output of uname, and stores it in /var/run/motd.dynamic.
#                    Both parts are output by pam_motd.
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin
APPNAME="pVault"
COMMAND="uwsgi --emperor /opt/$APPNAME/system/uwsgi_setup &"

# enable with the followings
# update-rc.d pvault_uwsgi defaults
# update-rc.d pvault_uwsgi enable 2


case "$1" in
  start)
	su -l www-data -c "$COMMAND"
	;;
  stop)
	kill -KILL  $(ps ax | grep $APPNAME | awk -F' ' {'print $1'} | xargs echo)
	;;
  restart)
	$0 stop
	sleep 2
        $0 start
	;;
  *)
	echo "Usage: motd [start|stop|status]" >&2
	exit 1
	;;
esac

exit 0

