#!/bin/sh
city_id='242'
date_tag='*'
file_name=${city_id}.lineSeg.tag.gz
server_id='rwpt@106.54.146.131'

ssh  -t -t ${server_id}  2>&1 << eeooff
cd /data/algschedule/algdata/wencan/${city_id}
tar -czvf  ${file_name}  ./${date_tag}/lineSeg/seg
exit
eeooff
mkdir ../data/${city_id}

#下载并解压
scp  ${server_id}:/data/algschedule/algdata/wencan/${city_id}/${file_name}  ../data/${city_id}
tar -xzvf   ../data/${city_id}/${file_name} -C ../data/${city_id}/

ssh  -t -t ${server_id}  2>&1 << eeooff
rm -rf /data/algschedule/algdata/wencan/${file_name}
exit
eeooff


