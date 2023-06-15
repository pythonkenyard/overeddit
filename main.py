import requests

#complete these fields

bearer = "" #this will be a long field starting 'eyJ....' its basically your cookie
comment = "deleted comment due to api change"


#SCRIPT DONT CHANGE BELOW THIS LINE
comment = comment.replace(" ","%20") # needed format in the post request.


def overwrite(url):
  headers = {
      'authority': 'oauth.reddit.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9,es;q=0.8,de-DE;q=0.7,de;q=0.6,it;q=0.5',
      'authorization': f'Bearer {bearer}'
      'content-type': 'application/x-www-form-urlencoded',
      'dnt': '1',
      'origin': 'https://www.reddit.com',
      'referer': 'https://www.reddit.com/',
      'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  }

  params = {
      'emotes_as_images': 'true',
      'rtj': 'only',
      'redditWebClient': 'desktop2x',
      'app': 'desktop2x-client-production',
      'raw_json': '1',
      'gilding_detail': '1',
  }

  data = f'api_type=json&return_rtjson=true&thing_id=t1_jn3o6ey&text&richtext_json=%7B%22document%22%3A%5B%7B%22e%22%3A%22par%22%2C%22c%22%3A%5B%7B%22e%22%3A%22text%22%2C%22t%22%3A%22{comment}%22%7D%5D%7D%5D%7D'

  response = requests.post('https://oauth.reddit.com/api/editusertext', params=params, headers=headers, data=data)
  print(response)
