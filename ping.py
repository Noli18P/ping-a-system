#!/usr/bin/python3
#author: NOLI

import os,sys,signal,re

def main(ip):
    ping = str(os.system(f'ping -c 1 {ip} > ping.txt'))
    with open('./ping.txt', 'r') as f:
        ping_results = f.readlines()
        line = str(ping_results[1]).replace(' ','')
        
        ttl = re.findall('=\d\d|=\d\d\d', line)
        ttl = ttl[0]
        ttl = ttl.replace('=','')
        
        if int(ttl) == 64 or int(ttl) == 63:
            print('\n[!] The operative system is Linux!')
        else:
            print('\n[!] The operative system is Windows!')


def exit(sig,frame):
    print('\n[!] Wait...')
    sys.exit(1)

signal.signal(signal.SIGINT,exit)

if __name__ == '__main__':
    try: 
        target_ip = sys.argv[1]
    
        main(target_ip)

    except IndexError:
        print('\n [!] Usage: sudo python3 ping.py target_ip')
