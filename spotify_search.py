import requests

url = "https://api.spotify.com/v1/search?q="

def getTopTrack(results):
    track_name = ""
    artists = []
    track = ""
    for i in results:
        for c,v in i.items():
            if c=="name":
                track_name = v
            elif c == "artists":
                for art in v:
                    for a,b in art.items():
                        if a=="name":
                            artists.append(b)
    track = track_name + " - "
    for i in range(len(artists)):
        if i == 0:
            track = track + artists[i]
        elif i != 0:
            track = track +", "+ artists[i]
    return track

def getResults(auth_head,queryString="Never gonna give you up", type="track", limit=1, include_external = None):
    url = "https://api.spotify.com/v1/search?q="
    queryString = queryString.replace(" ","+")
    url = url + queryString +"&type="+type +"&limit=" + str(limit)

    results = requests.get(url, headers = auth_head)
    results = results.json()
    results = results['tracks']['items']
    return getTopTrack(results)
