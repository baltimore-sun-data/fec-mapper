import string
import requests
import time
import re
import json

#I'm running this in a virtualenv named fecm.
#At the moment, I use   source ~/.virtualenvs/fecm/bin/activate   to activate.

def main():

	print ' ... main stub started (gets candidate list)... '

	s = requests.session() 

	demoEndPoint = 'https://api.open.fec.gov/v1/candidates/?sort_nulls_large=true&office=P&candidate_status=C&sort=name&per_page=80&api_key=DEMO_KEY&page=1&cycle=2016'
	#^If you get complaints from the API endpoint, fill in your API key in place of the DEMO_KEY value above. 
	#Just remember to remove it before pushing back to github! 	
	#TODO: Ask someone on the FEC API team why Rubio isn't showing up on the request above.
	#We may need to tweak our selectors.

	#The candlistjson object is a dict, and candlistjson['results'] is a list.
	#Each candidate is a dict.
	#We're now going to loop through them, spitting out a few relevent details.
	#This will allow us to verify that all of our candidates are active until 2016.
	#(Edit: Yup, the output confirms that. See the next to-do item below for the next move.)
	for i in candlistjson['results']:
		print i['name']
		print i['candidate_id']
		print i['active_through']

		#TODO: Now start requesting details of individual candidates (and caching them, of course.)
		#demo string for an omalley request: 
		#https://api.open.fec.gov/v1/candidate/P60007671/history/2016/?page=1&sort=-two_year_period&api_key=DEMO_KEY&per_page=20&sort_nulls_large=true	

def getCandidate():

	print ' ... candidate stub started ... '


main()
