# fec-mapper
Mapping FEC data because it's a fun thing to do. 

Basic API documentation on which this will rely:

https://api.open.fec.gov/developers 


#####

Because I want to practice python a bit without having to spend forever on it, I will do the following:

-- Create a folder called "scrape" containing python scripts that output json for chatter, mapping, etc.,.

-- Create a folder called "history" allowing python scripts to compare current API output to older versions

-- Create a folder called "local-json" that simply holds the local json output by those python scripts

-- Create a folder called "bake" containing php/html views and a wrapper combining it all into output html
   (Scripts in this folder will also send any output that might go to an external CMS.)

-- Create a folder called "baked-html" containing output


=====
#####

TODOs:

x Set up a virtualenv called fecm   ... which can be activated with   source ~/.virtualenvs/fecm/bin/activate

~ Create a simple API call to pull some data for our state

-- Create a simple comparison that writes a human-readable timestamp to a file when the data has changed

-- Set up a cron job to run this -- in this way, we can judge a threshold so we don't get /constant/ alerts

-- Set up a simple chatter generator in python, describing the scope of data and recent notable changes

-- Output the JSON that will feed our map 

-- Pull each part of this readme file into its own file and create verbal pointers to those files

-- Make sure that all documentation uses the correct markup style. (It currrently does not.)

-- Start working on the php code in the "bake" folder 

-- Integrate with jade/scss/koala/etc.,. 
   (I would do this earlier, but we're still figuring out preciseely how we want to use those tools at work.)


=====
#####

Steps I used to make my workflow function on a relatively fresh VM:

-- Installed virtualenvwrapper using   sudo apt-get install virtualenvwrapper

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
	#And now the important three that you'll want to loop from now until the end of time:
	git add *
	git commit --message="More initial build work"
	git push



