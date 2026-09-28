# Лабораторная работа 0 - свой сервис

## Stack
- Arch Linux
- Python + Flask
- MariaDB

## Deployment (as root)
```
pacman -S git python3 mariadb

cd /var
git clone https://github.com/itmo-cloud-team/lab0 teamairlines && cd $_
chmod +x deploy.sh
./deploy.sh
```
