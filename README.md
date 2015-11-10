# fec-mapper
Mapping FEC data because it's a fun thing to do. 

Basic API documentation on which this will rely:

https://api.open.fec.gov/developers 

Because I want to practice python a bit without having to spend forever on it, I will do the following:

-- Create a folder called "scrape" containing python scripts that output json for chatter, mapping, etc.,.

-- Create a folder called "history" allowing python scripts to compare current API output to older versions

-- Create a folder called "local-json" that simply holds the local json output by those python scripts

-- Create a folder called "bake" containing php/html views and a wrapper combining it all into output html
   (Scripts in this folder will also send any output that might go to an external CMS.)

-- Create a folder called "baked-html" containing output



Steps I used to make my workflow function:

-- Created repository using web interface

-- Used "git clone" to download to local workspace

-- Used   cd fec-mapper  to go into the local repository

-- Made some changes to the readme file using vim

-- Created some folders

-- Used format   
	git remote add origin https://github.com/user/repo.git   
	#...per   
	https://help.github.com/articles/adding-a-remote/
	#(^redundant but harmless)
	git remote -v
	echo "This file exists because http://bit.ly/1Y1NL31" > ./bake/placeholder.txt
	echo "This file exists because http://bit.ly/1Y1NL31" > ./baked-html/placeholder.txt
	echo "This file exists because http://bit.ly/1Y1NL31" > ./history/placeholder.txt
	echo "This file exists because http://bit.ly/1Y1NL31" > ./local-json/placeholder.txt
	echo "This file exists because http://bit.ly/1Y1NL31" > ./scrape/placeholder.txt
	git add *
	git commit
	#git may ask for some ID info here -- provide it if so.
	git push
	#(Entered password info here.)



