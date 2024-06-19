#!/usr/bin/env python
# coding=utf-8
'''
'''
import sys
import time

from argparse import ArgumentParser
from common.logo import logo
from load_module import load_module

if __name__ == '__main__':
    logo()
    randomtime = str(int(time.time()))
    parser = ArgumentParser(description='API KEY Verify')
    parser.add_argument("-t", "--type", help='Select API Type')
    parser.add_argument("-f", "--files", default='key.txt', help='read the apikey from the file')

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
    else:
        load_module(args.type, args.files)
