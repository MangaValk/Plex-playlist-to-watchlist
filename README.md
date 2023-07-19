# Plex-playlist-to-watchlist
Copy shows and movies from Playlists in your Plex Media Server libraries to the main Watchlist for 3rd party import (Sonarr, Radarr, etc)
Requires Python 3, pip, BeautifulSoup, and lxml

### Windows instructions
1. With the prerequisites installed, simply download the script to a directory, shift right click on the background of said directory, select "Open Powershell/Command Prompt Window Here"
2. Run the script:
>py .\main.py
3. Follow the prompts

### Mac/Linux instructions
1. With the prerequisites installed, download the script to a directory
  >wget https://github.com/ChiefBoyardee/Plex-playlist-to-watchlist/blob/master/main.py

2. Run the script
>python3 main.py
3. Follow the prompts


This script should then ask for your Plex Media Server IP address, as well as a temporary token (See: https://www.plexopedia.com/plex-media-server/general/plex-token/). The script should then list any available playlists for you to convert.
