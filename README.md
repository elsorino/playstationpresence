Discord RPC to show what PS4/PS5 game you're playing

![Image Preview](https://i.imgur.com/O9qDYFf.png)

## Setup

### Windows method
1. Download the latest exe/ini files in [releases](https://github.com/elsorino/playstationpresence/releases)
2. Login into your [My PlayStation](https://my.playstation.com/) account.
3. In another tab, go to https://ca.account.sony.com/api/v1/ssocookie
4. Copy the npsso key into playstationpresence.ini
5. Add PSNID to playstationpresence.ini
   * You must have permission to view status, e.g your own account if private
6. Run the exe with playstationpresence.ini in the same folder

### Using Python
1. Download with `git clone https://github.com/elsorino/playstationpresence`
2. Copy playstationpresence.example.ini to playstationpresence.ini
3. Login into your [My PlayStation](https://my.playstation.com/) account.  
4. In another tab, go to https://ca.account.sony.com/api/v1/ssocookie  
5. Copy the npsso key into playstationpresence.ini
6. Add PSNID to playstationpresence.ini
   * You must have permission to view status, e.g your own account if private
7. Install requirements with `pip install -r requirements.txt`
8. Run the script with `python playstationpresence.py`

### How it works

The script works by using [PSNAWP](https://github.com/isFakeAccount/psnawp) to check a user's status every 15 seconds, using [pypresence](https://github.com/qwertyquerty/pypresence) to update RPC if the status is different

### Game Art

If a game is supported, it will have their icon shown while playing. A list of supported games is available at [the games repository](https://github.com/elsorino/playstationpresence-games)

### Issues/limitations

Non-games such as Netflix and suspended games will still show as playing the previous game. This is an issue with the PSN API and can't be fixed.

For any other issue, you can contact me on Discord at elso#3228 or open an issue

### Supported systems

Currently supports PS4/PS5. PS5 support was added recently and may still have bugs

Vita/PS3 don't seem to work with the current PSN API used. See below for alternatives for those systems

### TODO

Better method to grab the game/gameID, very crappy method right now

### See also

[Playstation Vita RPC](https://github.com/TheMightyV/vita-presence-the-server) - Discord RPC for the Playstation Vita written in C++(requires homebrew)

[PS3-Discord](https://github.com/boozerboozeman/PS3-Discord) - Discord RPC for the PS3(requires homebrew)

[PlayStationDiscord](https://github.com/Tustin/PlayStationDiscord) - Like this but written in Electron. Supports additional consoles
