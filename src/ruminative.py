#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
@author: AlwaysLivid
@version: 0.35
@description: A simple reconnaissance tool utilizing Shodan.
'''

import sys, urllib, os, shodan
import secret

# Parts of this code were inspired by the following repositories:
# https://github.com/PaulSec/Shodan-mattermost

logo = '''
________                     _____                 _____ _____                
___  __ \____  _________ ___ ___(_)_______ ______ ___  /____(_)___   _______  
__  /_/ /_  / / /__  __ `__ \__  / __  __ \_  __ `/_  __/__  / __ | / /_  _ \ 
_  _, _/ / /_/ / _  / / / / /_  /  _  / / // /_/ / / /_  _  /  __ |/ / /  __/ 
/_/ |_|  \__,_/  /_/ /_/ /_/ /_/   /_/ /_/ \__,_/  \__/  /_/   _____/  \___/  
... v0.35 - written with love by AlwaysLivid. <3
'''

def intro():
    os.system('clear')
    print(logo)

def fetch_public_ip():
    try:
        ip = ""
        provider = "http://ip.42.pl/raw"
        with urllib.request.urlopen(provider) as ip: 
            ip = ip.read().decode('utf-8')
        return ip
    except Exception as e:
        print("[!] An error occured while fetching the public IP address!")
        print("[!] Exception: {}".format(e))

def create_shodan_obj():
    try:
        token = ""
        token = secret.token
        return shodan.Shodan(token)
    except Exception as e:
        print("[!] An error occured while creating a Shodan object!")
        print("[!] Exception: {}".format(e))

def shodan_search(shodan_obj, ip):
    try:
        print("\n[*] Basic Information")
        result = shodan_obj.host(ip)
        hostname = "N/A"
        if len(result['hostnames']) > 0: # Borrowed from PaulSec.
            hostname = result['hostnames'][0]
            print("[*] IP Address: {} ({})".format(result['ip_str'], hostname))
            print("[*] Country: {}".format(result.get('country_name', 'N/A')))
            print("[*] City: {}".format(result.get('city', 'N/A')))
            print("[*] Organization: {}".format(result.get('org.get', 'N/A')))
            print("[*] ISP: {}".format(result.get('isp', 'N/A')))
            print("[*] ASN: {}".format(result.get('asn', 'N/A')))
            print("[*] Operating System: {}".format(result.get('os', 'N/A')))
            print("[*] Last Update: {}".format(result.get('last_update', 'N/A')))
        exit(0)
    except Exception as e:
        print("[!] An error occured while gathering the results!")
        print("[!] Exception: {}".format(e))

def main():
    shodan_search(create_shodan_obj(), fetch_public_ip())

if __name__ == "__main__":
    intro()
    if len(sys.argv) != 2 and len(secret.token) == 0:
        print("[*] It looks like you haven't entered a token in the token.py file!")
        print("[*] Would you like to enter one now? (Y/N)")
        answer = input().lower()
    if answer == "y":
        secret.token = input("[!] Enter your token: ")
    else:
        sys.exit(1)
    main()