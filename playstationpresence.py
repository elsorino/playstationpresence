from psnawp_api import psnawp
from pypresence import Presence
import time
import ast
from config import (
    npsso,
    PSNID
)
start_time = int(time.time())
oldpresence = ""
psnawp = psnawp.PSNAWP(npsso)
#Initial usage, used to clear status if user is offline

RPC = Presence("829124881324048404",pipe=0)
RPC.connect()

while True:
    user_online_id = psnawp.user(online_id=PSNID)
    mainpresence = str(user_online_id.get_presence())
    #print(mainpresence) #Uncomment this to get info about games inc. artwork/gameid links
    start_time = int(time.time())
    if 'offline' in mainpresence:
        print("User is offline, clearing status")
        RPC.clear()
    else: 
        if (oldpresence == mainpresence):
            pass
        else:
            #Best way to work with backwards compatability is a seprate RPClient named Playstation 5 with PS4 game assets
            if 'PS5' in mainpresence:
                system = "ps5"
                if 'CUSA' in mainpresence:
                    RPC.clear()
                    RPC = Presence("829746683835187220", pipe=0)
                    RPC.connect()
                else:
                    RPC.clear()
                    RPC = Presence("829547127809638451",pipe=0)
                    RPC.connect()
            else:
                system = "ps4"
                RPC.clear()
                RPC = Presence("829124881324048404",pipe=0)
                RPC.connect()
            current = mainpresence.split("'")
            if (len(current) == 19): #Length of this is 19 if user is not in a game
                RPC.update(state="Idling", start=start_time, small_image=system, small_text=PSNID, large_image=system, large_text="Homescreen")
                print("Idling")
            else:
                if 'gameStatus' in mainpresence: #Not every game supports gameStatus
                    gametext = current[39]
                else:
                    gametext = current[27]
                gameid = current[23]
                gamename = current[27]
                #gamestatus = current[]
                RPC.update(state=gamename, start=start_time, small_image=system, small_text=PSNID, large_image=gameid.lower(), large_text=gametext)
                print("Playing %s" %gamename)
    time.sleep(15) #Adjust this to be higher if you get ratelimited
    oldpresence = mainpresence