from psnawp_api import psnawp
from pypresence import Presence
import time
import ast
from config import (
    npsso,
    client_id,
    PSNID
)
psnawp = psnawp.PSNAWP(npsso)
RPC = Presence(client_id,pipe=0)
RPC.connect()
print("RPC connection successful.")

start_time = int(time.time())
oldpresence = ""

while True:
    user_online_id = psnawp.user(online_id=PSNID)
    mainpresence = str(user_online_id.get_presence())
    #print(mainpresence) #Uncomment this to get info about games inc. artwork/gameid
    start_time = int(time.time())
    if 'offline' in mainpresence:
        print("User is offline, clearing status")
        RPC.clear()
    else: 
        if (oldpresence == mainpresence):
            continue
        else:
            test = mainpresence.split("'")
            if (len(test) == 19):
                RPC.update(state="Idling", start=start_time, small_image="ps4", small_text=PSNID, large_image="ps4")
                print("Idling")
            else:
                gamename = test[27]
                gameid = test[23]
                RPC.update(state=gamename, start=start_time, small_image="ps4", small_text=PSNID, large_image=gameid.lower())
                print("Playing %s" %gamename)
    time.sleep(30) #Checks every 30 seconds to prevent ratelimiting
    oldpresence = mainpresence
