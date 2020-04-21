#!/usr/bin/python
import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a","--apikey", help="Defines a API-key", dest="API_KEY")
parser.add_argument("-m","--mode", help="Defines the Monitoring Mode", dest="MODE")
parser.add_argument("-w","--warning", default=75, help="Defines Warning value in Percent", dest="WARNING")
parser.add_argument("-c","--critical", default=90, help="Defines Critical value in Percent",dest="CRITICAL")

args = parser.parse_args()

API_KEY = args.API_KEY
MODE = args.MODE
WARNING = args.WARNING
CRITICAL = args.CRITICAL