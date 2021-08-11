#!/usr/bin/env python3

import os
import sys
import random
import snoop
from time import sleep

# first time should run as root / you need to have systemd installed and your git creds saved

systemd_service = '''[Unit]
Description=Doing Duckery with github stats
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/bin/python3 {} --serv

[Install]
WantedBy=multi-user.target
'''
@snoop
def main():
    if "--serv" in sys.argv:
        with open("cred.txt","r") as f:
            user = f.readline()
        while (True):
            os.system("bash push.sh "+user)
            sleep(random.randrange(3600*1,3600*3))
    else:
        with open("cred.txt","w") as f: 
            f.write(input("tell me your cheater-ass github username: "))
        systemd_serv_path = "/etc/systemd/system/github_stats_ducker.service"
        with open(systemd_serv_path,"w") as f:
            f.write(systemd_service.format(__file__))
        os.system("sudo systemctl daemon-reload")
        sleep(2)
        os.system("sudo systemctl enable github_stats_ducker.service")
        sleep(2)
        os.system("sudo systemctl start github_stats_ducker.service")

main()
