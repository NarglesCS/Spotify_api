# Spotify_api
Return the top result of a default search.

main.py  
  The current "main menu" all it does at the moment is run a default search and print the the track name and artist in the format of [(track name) - (artist)]  
  
spotify_api_connector.py  
  defined functions:  
    - getClientKeys()  
      -- returns the client key and private client key from a text file named "apiKey.txt" as long as the client key is on line 1 and private client key is on line 2  
    - genAuthentication()  
      -- returns the authentication results from the client key and private client key provided. (there is no error checking implemented).  
      
spotify_search.py  
  defined functions:  
    - getTopTrack(results[])  
      -- returns a string representation of the song from list of results. (only works for one song, otherwise it will return the name of the last song plus all artists appended in the list artists.  
    - getResults(auth_head,queryString="Never gonna give you up", type="track", limit=1, include_external = None)  
      -- returns the top track from the search  
  
