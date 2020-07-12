server_id='rwpt@106.54.146.131'
my_password='N86EhrWywgiQxQeC\r'

echo "===========genrsa===================="
expect <<EOF
spawn ssh-keygen -t rsa
set timeout 30
expect {
"Enter file in which to save the key (/Users/zheheng/.ssh/id_rsa):" { send "\r"; exp_continue}
"Enter passphrase (empty for no passphrase):" { send "\r"; exp_continue} 
"Enter same passphrase again:" { send "\r"; exp_continue}
"Overwrite (y/n)?" {send "y\r";exp_continue}
}
EOF

expect <<EOF
spawn scp /Users/zheheng/.ssh/id_rsa.pub  ${server_id}:/data/
set timeout 3

expect {
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



