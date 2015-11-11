import string
import requests
import time
import re

def main():

	print ' ... main stub started ... '

	s = requests.session()

	demoEndPoint = 'https://api.open.fec.gov/v1/candidates/?sort_nulls_large=true&office=P&candidate_status=C&sort=name&per_page=80&api_key=DEMO_KEY&page=1&cycle=2016'
	#^If you get complaints from the API endpoint, fill in your API key in place of the DEMO_KEY value above. 
	#Just remember to remove it before pushing back to github! 	
	#TODO: Ask someone on the FEC API team why Rubio isn't showing up on the request above.
	#We may need to tweak our selectors.

	result = s.get(demoEndPoint)
	content = result.content
	print(content)

def getCandidate():

	print ' ... candidate stub started ... '


main()
