import requests
import base64

def getClientKeys():
    api = open("apiKey.txt", "r")
    client = api.readline()
    client_secret = api.readline()
    api.close()
    return client, client_secret

def genAuthentication():

    client, client_secret = getClientKeys()

    client_credentials = {
        client: client_secret
    }

    url = "https://accounts.spotify.com/api/token"
    encode = client[:-1]+":"+client_secret[:-1]
    encode = encode.encode('ascii')
    encoded = base64.b64encode(encode)
    encoded = encoded.decode('ascii')
    head = {
        "Authorization" : "Basic " + str(encoded)
    }
    req = {
        "grant_type": "client_credentials"
    }

    auth_token = requests.post(url, headers = head, data = req)
    auth_token = auth_token.json()
    auth_head = {
        "Authorization" : "Bearer " +auth_token["access_token"]
    }
    return auth_head
