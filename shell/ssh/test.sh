#!/bin/sh
server_id='rwpt@106.54.146.131'
city_id='242'
date_tag='*'
ssh  -t -t rwpt@106.54.150.46  2>&1 << eeooff
cd /data/algschedule/algdata/wencan/
tar -czvf  lineSeg.tar.gz  ./${city_id}/${date_tag}/lineSeg/seg
exit
eeooff

scp  rwpt@106.54.150.46:/data/algschedule/algdata/wencan/lineSeg.tar.gz ./

ssh  -t -t rwpt@106.54.150.46  2>&1 << eeooff
rm -rf /data/algschedule/algdata/wencan/lineSeg.tar.gz 
exit
eeooff







