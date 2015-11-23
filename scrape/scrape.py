import string
import requests
import time
import re
import json

#We're running this in a virtualenv named fecm.
#At the moment, I use   source ~/.virtualenvs/fecm/bin/activate   to activate.

def main():

	print ' ... main stub started (gets candidate list)... '

	s = requests.session() 

	demoEndPoint = 'https://api.open.fec.gov/v1/candidates/?sort_nulls_large=true&office=P&candidate_status=C&sort=name&per_page=80&api_key=DEMO_KEY&page=1&cycle=2016'
	#^If you get complaints from the API endpoint, fill in your API key in place of the DEMO_KEY value above. 
	#Just remember to remove it before pushing back to github! 	
	#TODO: Ask someone on the FEC API team why Rubio isn't showing up on the request above.
	#We may need to tweak our selectors.

	candlistresult = s.get(demoEndPoint)
	candlistcontent = candlistresult.content
	#print(candlistcontent)

	#Now we check to see whether we have a usable json object. (This will probably eventually be cached.)
	candlistjson = json.loads(candlistcontent)
	candlistdump = json.dumps(candlistjson,sort_keys=True, indent=4)

	print candlistdump
	print type(candlistjson['results'])
	#... so we know that candlistjson is a dict, and candlistjson['results'] is a list.
	#Now want to get a specific member of that list. Let's see if we can do that with a numbered index.
	print type(candlistjson['results'][0])
	#Ok. So each member of that list is a dict representing a candidate. Can we get a specific field?
	#(If so, this should spit out Abosede Adeshina's name.
	print candlistjson['results'][0]['name']
	#^Ok, that worked. Now let's get the candidate ID, which will then be handy for feeding into their candidate endpoint.
	#We also want to make sure that the candidate is active through 2016. 
	print candlistjson['results'][0]['candidate_id']
	print candlistjson['results'][0]['active_through']
	#^Ok, all of the last three lines of non-comment code worked (and should therefor eventually be commented/removed.
	#Time to see if we can make this work for everybody. 
	for i in candlistjson['results']:
		print i['name']
		print i['candidate_id']
		print i['active_through']

	#... well, that simple loop seemed to work.
	#TODO: Now start requesting details of individual candidates (and caching them, of course.)
	#demo string for an omalley request: 
	#https://api.open.fec.gov/v1/candidate/P60007671/history/2016/?page=1&sort=-two_year_period&api_key=DEMO_KEY&per_page=20&sort_nulls_large=true

	

def getCandidate():

	print ' ... candidate stub started ... '


main()
