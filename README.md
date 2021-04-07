Discord RPC support for PS4 written in python

![Image Preview](https://i.imgur.com/O9qDYFf.png)

## Setup

1. Download with `git clone https://github.com/elsorino/playstationpresence`
2. Copy config.example.py to config.py
3. Login into your [My PlayStation](https://my.playstation.com/) account.  
4. In another tab, go to https://ca.account.sony.com/api/v1/ssocookie  
5. Copy the npsso key into config.py
6. Add PSN username to config.py
   * It doesn't have to be your own PSNID
7. Install requirements with `pip install -r requirements.txt`
8. Run the script with `python playstationpresence.py`

### How it works

The script works by using [PSNAWP](https://github.com/isFakeAccount/psnawp) to check a user's status every 15 seconds, using [pypresence](https://github.com/qwertyquerty/pypresence) to update RPC if the status is different

### Game Art

If a game is supported, it will have their icon shown while playing. A list of supported games is available at [the games repository](https://github.com/elsorino/playstationpresence-games)

### Customization

You can remove showing your PSNID on hover by removing `small_text=PSNID` in playstationpresence.py(or replacing PSNID with whatever text you want)

If you want to print additional info about the user presence to your terminal, uncomment line 21. Useful for downloading art assets.

### Issues

If you receive a ratelimiting error, edit the timeout on line 39 to be hire(e.g 30). The ratelimit is 100 calls every 15 minutes, so the default shouldn't timeout.

For any other issue, you can contact me on Discord at elso#3228 or open an issue

### Support for other consoles

PS5/PS3 support is something I'll look into

Not going to support the Vita since a superior solution already exists(see below)

### See also

[Playstation Vita RPC](https://github.com/TheMightyV/vita-presence-the-server) - Discord RPC for the Playstation Vita written in C++(requires homebrew)

[PlayStationDiscord](https://github.com/Tustin/PlayStationDiscord) - Like this but written in Electron. Supports additional consoles