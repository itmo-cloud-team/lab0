#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Run it as root."
    exit 1
fi

pacman -Syu git python3 mariadb

read -p "Choose username [teamairlines]: " username
username=${username:-teamairlines}

user_password=""
while [ -z "$user_password" ]
do
read -p "Set password for user: " user_password
done

useradd -m $username
echo "$username:$user_password" | chpasswd

read -p "Enter host [0.0.0.0]: " host
host=${host:-0.0.0.0}

read -p "Enter port [5000]: " port
port=${port:-5000}

db_password=""
while [ -z "$db_password" ]
do
read -p "Enter DB password: " db_password
done

chown -R $username:$username ./
python3 -m venv .venv && source $_/bin/activate
pip3 install -r requirements.txt

mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
systemctl enable --now mariadb.service
echo "mysql:$db_password" | chpasswd

sed -i "s/HOST/$host/g" config.json.sample
sed -i "s/PORT/$port/g" config.json.sample
sed -i "s/DB_PASSWORD/$db_password/g" config.json.sample
mv config.json.sample config.json

mariadb -u mysql --password=$db_password < init.sql

sed -i "s/%dir%/$(pwd)/g" teamairlines.service
sed -i "s/%username%/$username/g" teamairlines.service
cp teamairlines.service /etc/systemd/system/

systemctl enable --now teamairlines.service
