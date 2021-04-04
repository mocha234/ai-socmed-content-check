import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

data = {
    "data":
    [
        {
            'Column2': "example_value",
            'Text': "example_value",
            'Follower count': "0",
            'Friends count': "0",
            'Industries': "example_value",
            'Time': "example_value",
            'Day of Weeks': "example_value",
            'hashtags_count': "0",
            'length_hashtag': "0",
            'user_mentions_count': "0",
            'media': "0",
            'Column13': "example_value",
            'Column14': "example_value",
            'Column15': "example_value",
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://19c7c988-64b5-4dab-81f6-8936f8064488.eastus2.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))