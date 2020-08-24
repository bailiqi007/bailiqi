server_id='rwpt@212.64.121.146'
my_password='N86EhrWywgiQxQeC\r'

#100
server_id='rwpt@124.70.193.211'

#242
server_id='rwpt@121.37.159.187'

server_id='rwpt@124.70.190.225'

#server_id='rwpt@121.37.140.47'

server_id='rwpt@124.70.216.62'

server_id='rwpt@124.70.192.78'

echo "===========genrsa===================="
expect <<EOF
spawn ssh-keygen -t rsa
set timeout 30
expect {
"Enter file in which to save the key (/Users/zheheng/.ssh/id_rsa):" { send "\r"; exp_continue}
"Enter passphrase (empty for no passphrase):" { send "\r"; exp_continue} 
"Enter same passphrase again:" { send "\r"; exp_continue}

"Overwrite (y/n)?" {send "n\r";exp_continue}
}
EOF

expect <<EOF
spawn scp /Users/zheheng/.ssh/id_rsa.pub  ${server_id}:/data/
set timeout 3

expect {
	"Are you sure you want to continue connecting" {send "yes\r";exp_continue} 
	"${server_id}'s password:" {send ${my_password};exp_continue}
}
EOF

expect <<EOF

spawn ssh  -t -t ${server_id}

set timeout 3
expect  {
	"${server_id}'s password:"  {send ${my_password}  ;exp_continue}
	"~" {send " cd /data && cat id_rsa.pub >> ~/.ssh/authorized_keys && exit \r" ; exp_continue}
}

EOF



