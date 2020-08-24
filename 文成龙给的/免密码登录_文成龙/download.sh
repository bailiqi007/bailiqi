#!/bin/sh
date_tag='*'

city_id='100'
server_id='rwpt@124.70.193.211'


city_id='242'
#city_id='051'
server_id='rwpt@121.37.159.187'

#city_id='178'
#server_id='rwpt@124.70.190.225'

#city_id='070'
#server_id='rwpt@121.37.140.47'

#city_id='025'
#server_id='rwpt@124.70.216.62'

city_id='129'
#server_No='RWPT5'
server_id='rwpt@124.70.192.78'



file_name=${city_id}.lineSeg.tag.gz

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


