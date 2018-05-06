#!/bin/bash

usage() {
   echo  " Usage: $0 [start|stop|status]"
}

start_tomcat() {
rm -rf /usr/local/tomcat/temp/*
rm -rf /usr/local/tomcat/work/*
/usr/local/tomcat/bin/startup.sh
}

stop_tomcat() {

/usr/local/tomcat/bin/shutdown.sh
sleep 5;

TPID=$(ps aux |grep java |grep tomcat |grep -v 'grep' | awk '{print $2}')
    if [ -z $TPID ];then
        echo "##############################################"
	echo "tomcat stop"
    else
	kill -9 $TSTAT
        sleep 5;
	echo "##############################################"
        echo "tomcat stop"
    fi
}

status_tomcat() {
ps aux |grep java |grep tomcat |grep -v 'grep'
}

main() {
case "$1" in
  start)
     start_tomcat;;
  stop)
     stop_tomcat;;
  status)
     status_tomcat;;
    *)
     usage;;
esac
}
main $1;
