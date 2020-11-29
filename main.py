import requests
import base64
import spotify_api_connector as con
import spotify_search as search



auth_head = con.genAuthentication()
results = search.getResults(auth_head)
print(results)
#resp = requests.get("https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V", headers = auth_head)
