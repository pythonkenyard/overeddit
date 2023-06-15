import os
import time
import requests
import csv

#--------------UPDATE THESE FIELDS---------------------------------------------------

#COMPULSORY
bearer = ""                                     #this will be a long field starting 'eyJ....' its basically your cookie


#OPTIONAL
comment = "deleted comment due to api change"   # edit for your custom comment
delay = 1.5                                       # seconds between comments. Reddit has specified oauth should be able to to 60-100 requests per minute
csv_file = ""                                   #link to csv file. will be prompted if not included.

#-----------------SCRIPT DONT CHANGE BELOW THIS LINE--------------------------------------------------------------------------
running = False
comment = comment.replace(" ","%20") # needed format in the post request.

def prompt_selection():
  #os.system("cls") # clear the cmd line
  print("(1) overwrite comments:\
        \n(z) Exit")
  selection = input("choose:")
  if selection == "1":
    return False, "overwrite"

  elif selection.lower() == "z":
    return True, "skip"

  else:
    print("unknown input. please input e.g. 1 or z")
    return False, "skip"

#MAIN FUNCTION FOR OVERWRITING. IT IS JUST A POST REQUEST AS PER CHROME
def overwrite(item,num,duration):
  headers = {
      'authority': 'oauth.reddit.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9,es;q=0.8,de-DE;q=0.7,de;q=0.6,it;q=0.5',
      'authorization': f'Bearer {bearer}',
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

  data = f'api_type=json&return_rtjson=true&thing_id=t1_{item}&text&richtext_json=%7B%22document%22%3A%5B%7B%22e%22%3A%22par%22%2C%22c%22%3A%5B%7B%22e%22%3A%22text%22%2C%22t%22%3A%22{comment}%20{num}%20of%20{duration}%22%7D%5D%7D%5D%7D'

  response = requests.post('https://oauth.reddit.com/api/editusertext', params=params, headers=headers, data=data)
  if response.status_code == 200:
    print("SUCCESS")
    return "SUCCESS"
  else:
    print("ERROR")
    return "ERROR"
  
# load the csv file and return everything from column 1
def load_file(csvfile):
    list = []
    list2= []
    list3 = []
    with open(csvfile, "r", newline="", encoding='Latin1') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            list.append(row[0]) #ids
            list2.append(row[1]) # urls
            list3.append(row[8]) # comment text
    return list, list2, list3


#main script
if __name__ == "__main__":
    while not running:
        running, action = prompt_selection()
        if action == "skip":
            pass
        elif action == "overwrite":
            if not csv_file:
                try:
                    import tkinter
                    #add tkinter selection box and remove raise
                    raise
                except:
                    csv_file = input("input location of csv file (hold cmd, shift and right click then select copy as path): ")
                    csv_file = csv_file.replace('"',"")#remove apostrophe if included
            list_of_ids, list_of_urls, list_of_comments = load_file(csv_file) # load csv
            duration = len(list_of_comments)
            num=0
            start_num=0
            try:
                with open ("overeddit_log.txt","r") as f:
                    for count, line in enumerate(f):
                        pass
                    count+=1
                    print(f"existing data log file for {count} items")
                    start_num=input(f"start at what item (1-{duration}): ")
                    if not start_num:
                        start_num = 0

                f.close()
                write = "a"
                
            except:
                print("starting new log file")
                write = "w"
            
            with open ("overeddit_log.txt",write) as f:
                for item in list_of_ids:
                    if num < int(start_num):
                        pass
                        
                        num+=1
                    else:
                        print(list_of_urls[num])
                        print(list_of_comments[num])
                        num+=1
                        print(f"\noverwriting comment {num} of {duration}")
                        result = overwrite(item,num,duration)
                        output = f"{num} {result}: {list_of_urls[num]}\n"
                        try:
                            f.write(output)
                        except:
                            f.write(f"error loggin line {num}")
                        time.sleep(delay) # time delay between comment deletions to avoid ddosing or getting stopped.
                    
            f.close()
                    
        
        elif action == "delete":
            print("no support for deleting yet.")
