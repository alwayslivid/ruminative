#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: AlwaysLivid
@description: A simple reconnaissance tool utilizing Shodan.
'''

import sys, urllib, os, shodan
import secret

logo = '''
  ________                     _____                 _____ _____                
  ___  __ \\____  _________ ___ ___(_)_______ ______ ___  /____(_)___   _______  
  __  /_/ /_  / / /__  __ `__ \\__  / __  __ \\_  __ `/_  __/__  / __ | / /_  _ \\ 
  _  _, _/ / /_/ / _  / / / / /_  /  _  / / // /_/ / / /_  _  /  __ |/ / /  __/ 
  /_/ |_|  \\__,_/  /_/ /_/ /_/ /_/   /_/ /_/ \\__,_/  \\__/  /_/   _____/  \\___/  
                         Copyright (C) 2019 AlwaysLivid

===============================================================
======================= DISCLAIMER ============================
===============================================================
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; read the LICENSE.md file for details.
===============================================================
'''

provider = "http://ip.42.pl/raw"
with urllib.request.urlopen(provider) as ip:
    try:
        ip = ip.read().decode('utf-8')
    except Exception as e:
        print("\n[!] An error occurred while fetching the public IP address!")
        print("[!] Exception: {}".format(e))

def create_shodan_obj():
    try:
        return shodan.Shodan(secret.token)
    except Exception as e:
        print("[!] An error occurred while creating a Shodan object!")
        print("[!] Exception: {}".format(e))

def shodan_scan(shodan_object): # WIP
    scan = shodan_object.scan([ip])
    print("[!] Scan complete! (ID: {})".format(scan["id"]))

def print_results(result, hostname):
    print("\n[*] Basic Information")
    try:
        if len(result['hostnames']) > 0:
            hostname = result['hostnames'][0]
            # print("[*] IP Address: {} ({})".format(result['ip_str'], hostname))
            print("[*] Country: {}".format(result.get('country_name', hostname)))
            print("[*] City: {}".format(result.get('city', hostname)))
            print("[*] Organization: {}".format(result.get('org.get', hostname)))
            print("[*] ISP: {}".format(result.get('isp', hostname)))
            print("[*] ASN: {}".format(result.get('asn', hostname)))
            print("[*] Operating System: {}".format(result.get('os', hostname)))
            print("[*] Last Update: {}".format(result.get('last_update', hostname)))
    except Exception as e:
        print("[!] An error occurred while creating a Shodan object!")
        print("[!] Exception: {}".format(e))

def shodan_search(shodan_object):
    try:
        print("IP Address: {}".format(ip))
        result = shodan_object.host(ip)
        hostname = "N/A"
        print_results(result, hostname)
    except Exception as e:
        print("[!] An error occurred while gathering the results!")
        print("[!] Exception: {}".format(e))
        if (str(e) == "No information available for that IP.") and not (os.environ["SHODAN_KEY"] is not None):
            print("[?] Would you like to scan this IP address? (y/N)")
            answer = input().lower().strip('\n')
            if answer == "y":
                shodan_scan(shodan_object)
            else:
                exit()

if __name__ == "__main__":
    os.system('clear')
    print(logo)
    print("[!] Checking for environment variable...")
    if "SHODAN_KEY" in os.environ:
        print("[*] Found environment variable.")
        secret.token = os.environ["SHODAN_KEY"]
    else:
        print("[!] Environment variable not found.")
        if len(secret.token) == 0:
            print("[*] It looks like you haven't entered a token in the secret.py file!")
            print("[?] Would you like to enter one now? (y/N)")
            answer = input().lower().strip('\n')
            if answer.startswith('y') == True:
                secret.token = input("[!] Enter your token: ")
            else:
                print("[!] Sorry! This tool cannot be used without a Shodan API token.")
                exit(1)
    shodan_object = create_shodan_obj()
    shodan_search(shodan_object)