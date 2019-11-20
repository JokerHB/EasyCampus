# -*- coding: utf-8 -*- 

import os
import sys
import requests
import argparse

def login(username, password):
    loginURL = 'http://10.0.0.55:801/srun_portal_pc.php?ac_id2=1&'

    loginPram = {'action':'login',
                'username': username,
                'password': password,
                'ac_id': '1',
                'user_ip': '',
                'nas_ip': '',
                'user_mac': '',
                'save_me': '1',
                'ajax': '1'}

    response = requests.post(loginURL, data=loginPram).text

    if response.split(',')[0] != 'login_ok':
        print('Can not login %s.' % username)
        exit(-1)
    else:
        print('%s login success.' % username)
        exit(1)

def logout(username, password):
    logoutURL = 'http://10.0.0.55/cgi-bin/srun_portal?'

    logoutPram = {'action':'logout',
                'username': username,
                'password': password,
                'ac_id': '1',
                'ip': '',
                'info': '',
                'callback': ''}
   
    response = requests.post(logoutURL, data=logoutPram).text

    if response != 'logout_ok':
        print('Can not logout %s.' % username)
        exit(-1)
    else:
        print('%s logout success.' % username)
        exit(1)

def config(username=None, password=None):
    if username == None or password == None:
        try:
            with open('./.easy_log_config', 'r') as f:
                data = f.readlines()
        except Exception:
            print('Can not read config file.')
            exit(-1)
        if len(data) != 2:
            print('Please re-config.')
            exit(-1)
        username = data[0].strip()
        password = data[1].strip()
        return (username, password)
    else:
        with open('./.easy_log_config', 'w') as f:
            f.write(username + '\n' + password)
        return (username, password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version', version='%(prog)s version : v 0.01', help='show the version')
    parser.add_argument('-login', action='store_true', help='login the network')
    parser.add_argument('-logout', action='store_true', help='logout the network')
    parser.add_argument('-username', '-u', help='your username of the network')
    parser.add_argument('-password', '-p', help='your password of the network')
    parser.add_argument('-config', '-c', action='store_true', help='store your username and password')
    args = parser.parse_args()

    username = args.username
    password = args.password

    if username == None or password == None:
        (username, password) = config()
    if args.config:
        config(username, password)
    if args.login:
        login(username, password)
    elif args.logout:
        logout(username, password)
