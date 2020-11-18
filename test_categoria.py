
import googleapiclient.discovery
api_key="AIzaSyCWH5-fbx-6X4GHB3fc291PdVOBCyYOQGQ"

youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

request1=youtube.videos().list(
    part="snippet",
    id="VIwcc4y38hs"
)
response1 = request1.execute()
print(response1)
if(response1["pageInfo"]["totalResults"]>0):
    category=response1["items"][0]["snippet"]["categoryId"]
    request = youtube.videoCategories().list(
            part="snippet",
            
            id=category
        )
    response = request.execute()
    print(response1["items"][0]["snippet"]['title'])

    print(response1["items"][0]["snippet"]['channelId'])
    print(response1["items"][0]["snippet"]['description'])
    print(response["items"][0]["snippet"]['title'])
