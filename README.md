# overeddit   
reddit comment overwriter. Overwrites all your reddit comments with a personal text   

# Status   
ongoing. Functional to a point. but this errored for me on comment 110 of 18k so it needs some tweaking in the next 24hr to run without issue.   
   
## Requirements:   
1. your comments data from Reddit: you can request it here. note it usually takes 24-48hrs. it will be a zip and you need the comments.csv file    
   https://www.reddit.com/settings/data-request
2. Python - https://www.python.org/downloads/   
   (click add to path when installing and also install pip)   
 
### Setup Instructions:   
open command line   
pip install requests   
pip install csv   
   
### Running instructions:   
Download the script main.py   
Add your bearer token to line 5? # if you need help to find this. open reddit press F12 and search gql then scroll down to the authorisation and copy(https://imgur.com/pdnGTKT)   
you can edit optional settings   
open cmd and run the script (in cmd type python main.py or python "c:/user/desktop/main.py" - wherever the file is located   
follow the onscreen instructions.   

## Future additions    
option to delete comments    
option to overwrite then delete comments.    

## Background    
in May 2023 Reddit announced changes to its policies which will force out any 3rd party apps.   
There is what I can admit are valid reasons for this. However reddits policies are slowly becoming more and more corporate.    
Minimal efforts have been made to work with users on this except on fronts where it will impact their own income.    
Their API pricing is gouging and does not support 3rd party app developers. Which will force 3rd party apps out of commission.    
As a user of 3rd party app myself (RIF). I likely wont use reddit in future.    
I also see no benefit in my content remaining on their site and am overwriting every comment.    
Please feel free to see the script I have compiled (main.py)   
   
As an aside to the above I had been removing my comments prior to this however reddit never supported comments older than 1 year. as such i have built 10 years of comments with no way to remove comments over 8 years.    
This is a functional method to do this.   
