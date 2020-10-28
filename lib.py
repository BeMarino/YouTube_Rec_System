
def getDuration(id):
    import isodate
    import json
    import googleapiclient.discovery    
    import time
    api_key="AIzaSyCWH5-fbx-6X4GHB3fc291PdVOBCyYOQGQ"
    
    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)
    
    request = youtube.videos().list(
        part="contentDetails",
        id=id
    )
    response=request.execute()
    time.sleep(3)
    dur=isodate.parse_duration(response['items'][0]["contentDetails"]["duration"])
    return int(dur.total_seconds())
 
