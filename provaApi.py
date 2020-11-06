import os
import isodate
import json
import googleapiclient.discovery 
from datetime import datetime

date = datetime.now()
date=date.strftime("%d-%m-%Y_%H.%M.%S")

id_canale_lega="UCw2AF_J2QizzmWw99bs3e6Q"
api_key="AIzaSyCWH5-fbx-6X4GHB3fc291PdVOBCyYOQGQ"
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
   

    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        type="video",
        relatedToVideoId="IsaIaPtJZ4Q",
        maxResults=25
    )

    request2 = youtube.videos().list(
        part="snippet,contentDetails,topicDetails",
        id="IsaIaPtJZ4Q"
    )

    request3 = youtube.activities().list(
        part="snippet",
        home="true",
        maxResults=25
    )

    ''' response = request.execute()
    with open("results/search_results.json","w") as results:
        json.dump(response,results)
    '''
    response2 = request2.execute()
    
    dur=isodate.parse_duration(response2['items'][0]["contentDetails"]["duration"])
    
    #with open("results/videos_results.json","w") as results:
    #    json.dump(response2,results)
    
    '''response3 =request3.execute()
    with open("results/activities_results.json","w") as results:
        json.dump(response3,results)
    '''

 

if __name__ == "__main__":
    main()