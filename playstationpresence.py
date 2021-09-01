#!/usr/bin/env python3
from psnawp_api import psnawp
from pypresence import Presence
import configparser
import time
import ast

def discordrpc(appid):
    global rpc
    rpc.clear()
    rpc = Presence(appid, pipe=0)
    rpc.connect()

config = configparser.ConfigParser()
config.read('playstationpresence.ini')
npsso = config['main']['npsso']
PSNID = config['main']['PSNID']
gameart = config['main']['gameArt']

PS4OnPS5 = config['appids']['PS4OnPS5']
PS5 = config['appids']['PS5']
PS4 = config['appids']['PS4']

psnawp = psnawp.PSNAWP(npsso)
start_time = int(time.time())
oldpresence = ""
#Initial usage, used to clear status if user is offline
rpc = Presence(PS4,pipe=0)
rpc.connect()

while True:
    user_online_id = psnawp.user(online_id=PSNID)
    mainpresence = str(user_online_id.get_presence())
    #print(mainpresence) #Uncomment this to get info about games inc. artwork/gameid links
    start_time = int(time.time())
    if 'offline' in mainpresence:
        print("User is offline, clearing status")
        rpc.clear()
    else: 
        if (oldpresence == mainpresence):
            pass
        else:
            #Best way to work with backwards compatability is a seprate rpclient named Playstation 5 with PS4 game assets
            if 'PS5' in mainpresence:
                system = "ps5"
                if 'CUSA' in mainpresence:
                    discordrpc(PS4OnPS5) #PS4 games on PS5
                else:
                    discordrpc(PS5) #PS5 games
            else:
                system = "ps4"
                discordrpc(PS4)
            current = mainpresence.split("'")
            if (len(current) == 19): #Length of this is 19 if user is not in a game
                rpc.update(state="Idling", start=start_time, small_image=system, small_text=PSNID, large_image=system, large_text="Homescreen")
                print("Idling")
            else:
                if 'gameStatus' in mainpresence: #Not every game supports gameStatus
                    gametext = current[39]
                else:
                    gametext = current[27]
                if gameart == "yes":
                    gameid = current[23]
                else:
                    gameid = system
                gamename = current[27]
                #gamestatus = current[]
                rpc.update(state=gamename, start=start_time, small_image=system, small_text=PSNID, large_image=gameid.lower(), large_text=gametext)
                print("Playing %s" %gamename)
    time.sleep(15) #Adjust this to be higher if you get ratelimited
    oldpresence = mainpresence