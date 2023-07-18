#  move shows and movies from plex playlist to watchlist in bulk
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import urllib
import requests

def getPlaylistId(plexUrl, plexToken):
    playlistsLink = "%s/playlists?X-Plex-Token=%s" % (plexUrl, plexToken)
    f = urllib.request.urlopen(playlistsLink)
    parsed_html = BeautifulSoup(f.read(), 'xml')
    playlists = {}
    for playlist in parsed_html.find_all("Playlist"):
        playlists[int(playlist.get("ratingKey"))] = playlist.get("title")
    while 1:
        for playlistKey in playlists.keys():
            val = playlists[playlistKey]
            print("Key", playlistKey, 'value', val)

        try:
            selectedPlaylistKey = int(input("enter source playlist key:"))
        except ValueError:
            print('Please enter an integer.')
            continue

        if selectedPlaylistKey in playlists.keys():
            break

        print('invalid playlist key!')
    return selectedPlaylistKey

def getAllShowIdentifiersFromPlaylist(plexUrl, plexToken, playlistId):
    playlistLink = "%s/playlists/%s/items?X-Plex-Token=%s" % (plexUrl, playlistId, plexToken)
    f = urllib.request.urlopen(playlistLink)
    parsed_html = BeautifulSoup(f.read(), 'xml')
    playlistShowIdentifiers = [];
    for videos in parsed_html.find_all("Video"):
        try:
            playlistShowIdentifiers.append(videos.get("grandparentGuid").replace("plex://show/", ""))
        except:
            pass
        try:
            playlistShowIdentifiers.append(videos.get("guid").replace("plex://movie/", ""))
        except:
            pass

    # make distinct
    return list(set(playlistShowIdentifiers))


plexUrl = "http://10.1.0.139:32400"

plexUrl = input("Enter Plex URL - (Example: http://127.0.0.1:32400): Be sure to include http:// ")

plexToken = input("Enter Plex Token (See: https://www.plexopedia.com/plex-media-server/general/plex-token/):")

playlistShowIdentifiers = getAllShowIdentifiersFromPlaylist(plexUrl, plexToken, playlistId)

print(playlistShowIdentifiers)

#  https://curlconverter.com/
headers = {
    'x-plex-token': ('%s' % plexToken),
}

for result in playlistShowIdentifiers:
    params = {
        'ratingKey': result
    }

    response = requests.put('https://metadata.provider.plex.tv/actions/addToWatchlist', params=params, headers=headers)

    print(response)
