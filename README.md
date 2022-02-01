# No longer needed since Discord recently added official support for Playstation Network
Discord RPC to show what PS4/PS5 game you're playing

![Image Preview](https://i.imgur.com/O9qDYFf.png)

## Before starting
The default appids I setup only cover art for NA region games, if you're playing games outside the NA region(and use windows), I recommend checking out [this fork instead](https://github.com/cadewey/playstationpresence)

You can still use this anyway, but game art assets will be replaced with a PlayStation icon instead

Or if you know what you're doing, you can setup your own discord application, but that won't be covered here.
## Setup

### Windows without python installed
1. Download the latest exe/ini files in [releases](https://github.com/elsorino/playstationpresence/releases)
2. Login into your [My PlayStation](https://my.playstation.com/) account
3. In another tab, go to https://ca.account.sony.com/api/v1/ssocookie
4. Copy the npsso key into playstationpresence.ini
5. Add PSNID to playstationpresence.ini
   * You must have permission to view status, e.g your own account if private
6. If you're playing games outside the NA region, change gameart to false
   * Status is partially broken when art assets are missing, this replaces the art assets with a PlayStation icon instead
7. Run the exe with playstationpresence.ini in the same folder

### Using Python
1. Download with `git clone https://github.com/elsorino/playstationpresence`
2. Copy playstationpresence.example.ini to playstationpresence.ini
3. Login into your [My PlayStation](https://my.playstation.com/) account
4. In another tab, go to https://ca.account.sony.com/api/v1/ssocookie  
5. Copy the npsso key into playstationpresence.ini
6. Add PSNID to playstationpresence.ini
   * You must have permission to view status, e.g your own account if private
7. If you're playing games outside the NA region, change gameart to false
   * Status is partially broken when art assets are missing, this replaces the art assets with a PlayStation icon instead
8. Install requirements with `pip install -r requirements.txt`
9. Run the script with `python playstationpresence.py`

### How it works

The script works by using [PSNAWP](https://github.com/isFakeAccount/psnawp) to check a user's status every 15 seconds, using [pypresence](https://github.com/qwertyquerty/pypresence) to update RPC if the status is different

### Game Art

If a game is supported, it will have their icon shown while playing. A list of supported games is available at [the games repository](https://github.com/elsorino/playstationpresence-games)

Note that only NA region games are supported, if an NA region game is missing art assets, feel free to let me know

### Issues/limitations

Non-games such as Netflix and suspended games will still show as playing the previous game. This is an issue with the PSN API and can't be fixed.

For any other issue, you can contact me on Discord at elso#0442 or open an issue

### Supported systems

Supports PS4 & PS5

Vita/PS3 don't seem to work with the PSN API used. See below for alternatives for those systems

Program itself works on Windows, Linux, and macOS

### TODO

Look for a way to automatically determine if the art asset is available

### See also

[Playstation Vita RPC](https://github.com/TheMightyV/vita-presence-the-server) - Discord RPC for the Playstation Vita written in C++(requires homebrew)

[PS3-Discord](https://github.com/boozerboozeman/PS3-Discord) - Discord RPC for the PS3(requires homebrew)

[PlayStationDiscord](https://github.com/Tustin/PlayStationDiscord) - Like this but written in Electron.

[cadewey/playstationpresence](https://github.com/cadewey/playstationpresence) Fork of this with a completely different setup. Windows only, but much better if you're outside the NA region
