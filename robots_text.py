# When developing website, dont want some pages to be crawled like
# admin page or other private pages.

# robots.txt lists files dont want to crawl for google, yahoo

# When analyzing a site for security issues, see this file
# If developer says not to crawl these, can look here as can
# be sensitive

# Example file: https://www.reddit.com/robots.txt

import urllib
import requests


def get_robots_txt(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'

	r = requests.get(path + "robots.txt")
	#print "r.content is: {}".format(r.content) 
	return r.content
	
print get_robots_txt("http://www.reddit.com")
