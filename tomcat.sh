#!/bin/bash

usage() {
   echo  " Usage: $0 [start|stop|status]"
}

start_tomcat() {
rm -rf /usr/local/tomcat/temp/*
rm -rf /usr/local/tomcat/work/*
/usr/local/tomcat/bin/startup.sh > /dev/null 2>&1
        echo "##############################################"
        echo "tomcat started"

}

stop_tomcat() {

/usr/local/tomcat/bin/shutdown.sh > /dev/null 2>&1
sleep 5;

TPID=$(ps aux |grep java |grep tomcat |grep -v 'grep' | awk '{print $2}')
    if [ -z $TPID ];then
        echo "##############################################"
	echo "tomcat stoped"
    else
	kill -9 $TSTAT
        sleep 5;
	echo "##############################################"
        echo "tomcat stoped"
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
