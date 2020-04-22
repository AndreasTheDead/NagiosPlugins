#!/usr/bin/python3
import requests
from sys import exit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a","--apikey", help="Defines a API-key", dest="API_KEY")
parser.add_argument("-m","--mode", help="Defines the Monitoring Mode", dest="MODE")
parser.add_argument("-w","--warning", default=75, help="Defines Warning value in Percent (Default 75)", dest="WARNING")
parser.add_argument("-c","--critical", default=90, help="Defines Critical value in Percent (Default 90)", dest="CRITICAL")
parser.add_argument("-t","--target", default="127.0.0.1", help="Can be used to select a Target (Default 127.0.0.1)", dest="TARGET")
parser.add_argument("-p","--port", default=10080, help="Sets the Port (Default 10080)", dest="PORT")

args = parser.parse_args()

API_KEY = args.API_KEY
MODE = args.MODE
WARNING = args.WARNING
CRITICAL = args.CRITICAL
TARGET = args.TARGET
PORT = str(args.PORT)

if MODE == "usernumber":
	res = requests.get("http://"+TARGET+":"+PORT+"/1/serverinfo", headers={"x-api-key":API_KEY})
	result = res.json()
	if result["status"]["message"] == "ok":
		max_clients = int(result["body"][0]["virtualserver_maxclients"])
		current_clients = int(result["body"][0]["virtualserver_clientsonline"])-int(result["body"][0]["virtualserver_queryclientsonline"])
		if CRITICAL > round(current_clients/max_clients*100) > WARNING:
			print("Warning! They are "+str(current_clients)+ " of max "+str(max_clients)+" Clients online. (approx. "+str(round(current_clients/max_clients*100))+"%)")
			exit(1)
		elif CRITICAL < round(current_clients/max_clients*100) > WARNING:
			print("Critical! They are "+str(current_clients)+ " of max "+str(max_clients)+" Clients online. (approx. "+str(round(current_clients/max_clients*100))+"%)")
			exit(2)
		else:
			print("OK! They are "+str(current_clients)+ " of max "+str(max_clients)+" Clients online. (approx. "+str(round(current_clients/max_clients*100))+"%)")
			exit(0)
	else:
		print("Error: "+result["status"]["message"])
		exit(3)