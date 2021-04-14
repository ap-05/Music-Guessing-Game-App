from spotify_client import SpotifyAPI
from dotenv import load_dotenv, find_dotenv
import os
from random import randint, shuffle

def MusicFetch():
    artists = ['4tZwfgrHOc3mvqYlEYSvVi','4YRxDV8wJFPHPTeXepOstw','3xU8YsNNkmWSPewlB18NUz','5f4QpKfy7ptCHwTqspnSJI','6vWDO969PvNqNYHIOW5v0m','7jefIIksOi1EazgRTfW2Pk']
    return_list=[]
    selected_tracks = []
    """function fetching music for the game"""
    load_dotenv(find_dotenv())
    client = SpotifyAPI(os.getenv('client_id'),os.getenv('client_secret'))
    client.get_access_token()
    for y in range (0,5):
        tracks = client.get_list_of_track_info(artists[randint(0,(len(artists) - 1))])
        for x in range(0,4):
            print(len(tracks))
            track = randint(0,(len(tracks) - 1))
            select = False
            while not select:
                if tracks[track]['song_preview_url']:
                    selected_tracks.append(tracks[track])
                    select = True
                tracks.pop(track)
        return_list.append(
            {
                "questionText": selected_tracks[0]['song_preview_url'],
                "answerOptions": [
                        { "answerText": selected_tracks[0]["song_name"], "isCorrect": True }
                    ]
                    }
            )
        selected_tracks.pop(0)    
        for x in range (0,3):
            return_list[y]['answerOptions'].append({"answerText": selected_tracks[x]["song_name"], "isCorrect": False})
        
        shuffle(return_list[y]["answerOptions"])    
        
    print(return_list)    
    return return_list
        
    
