# overeddit   
Edit over all your historic reddit comments.    
This is as good as deleting your account in my opinion except it leaves a historic trace to show anyone in future that reddits decisions are why archived posts have lost so much useful info.
Note any external sites e.g. internetarchive etc which have cached your comments this cannot delete. what you posted in the past is likely permanently saved somewhere, but this will delete or overwrite what is on reddit at least.

# Status   
17/06: Working and tested by me to overwrite all comments. 
your account token seems tobe valid for 12 hours. so i managed to overwrite 15k of my 18k comments before i needed to update it and restart.

## Requirements:   
1. your comments data from Reddit: you can request it here.   
   https://www.reddit.com/settings/data-request
   note it usually takes 24-48hrs. it will be a zip and you need the comments.csv file   
3. Python - https://www.python.org/downloads/   
   (click add to path when installing and also install pip)   
 
### Setup Instructions:   
1.open command line   
2.type "pip install requests" and press enter to install this module then also  
3."pip install csv"   
If you have an error check python is installed correctly and install pip if you didnt install it as part of python install. Or note maybe it will say you already have them installed.
   
### Running instructions:   
1.Download the script main.py   
2.Add your bearer token to line 9 # if you need help to find this. open reddit press F12 and search gql then scroll down to the authorisation and copy(https://imgur.com/pdnGTKT)   
3.Add your id number in line 10 also. this is needed for certain comments. This is also in the reddit F12 screen in the gql, click the parameters tab and you will find id = "".   
Note: you can edit optional settings if you choose   
   
Once you edited the script, open cmd and run the script (in cmd type python main.py or python "c:/user/desktop/main.py" - wherever the file is located   
follow the onscreen instructions. example in this image   
https://imgur.com/j5aA5eX   

STOPPING: If you need to stop it at any stage bash ctrl + z a few times. you will have a prompt to resume where you left off when you restart.   

## Known Issues
I ran into an error around 12 hours into running this. It seems the bearer token expires and you need a new one. So you can run this for around 15k comments before error and you need an updated bearer token

## Future additions    
automatically stop after successivw fails? will ensure once token expires the system doesnt continue running
option to delete comments    
option to both overwrite then delete comments. (I have seen previous addons do this)     
Possibility to have a list of various comments which are chosen at random just to spice things up.       
Potential other options for ease of use: make a one click exe which can be run with login prompt and get token automatically. Currently beyond the scope of project but if there is demand I could look into this.   
   
## Background    
in May 2023 Reddit announced changes to its policies which will force out any 3rd party apps.   
There is what I can admit are valid reasons for this. However reddits policies are slowly becoming more and more corporate.    
Minimal efforts have been made to work with users on this except on fronts where it will impact their own income.    
Their API pricing is gouging and does not support 3rd party app developers. Which will force 3rd party apps out of commission.    
As a user of 3rd party app myself (RIF). I likely wont use reddit in future.    
I also see no benefit in my content remaining on their site and am overwriting every comment.    
Please feel free to see the script I have compiled (main.py)   
   
As an aside to the above I had been deleting some of my comments prior to this however reddit never supported deleting comments older than 1 year which is as far as you can view your history.    
as such i have personally built 10 years of comments with no way to remove comments over 8 years old.    
This script provides a functional,autoamted method to do this.   

Note: This was a quick 1-2hr script from my part. there is not much documentation within the script itself and formatting isnt great, but it gets the job done.  
