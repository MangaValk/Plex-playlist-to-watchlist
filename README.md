# Plex-playlist-to-watchlist
Copy shows and movies from Playlists in your Plex Media Server libraries to the main Watchlist for 3rd party import (Sonarr, Radarr, etc)
Requires Python 3, pip, BeautifulSoup, and lxml

With the prerequisites installed, simply download the script to a directory, shift right click on the background of said directory, select "Open Powershell/Command Prompt Window Here"

Then run: py .\main.py

This script should then ask for your Plex Media Server IP address, as well as a temporary token (See: https://www.plexopedia.com/plex-media-server/general/plex-token/). The script should then list any available playlists for you to convert.
