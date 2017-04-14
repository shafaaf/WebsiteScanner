# When developing website, dont want some pages to be crawled like
# admin page or other private pages.

# robots.txt lists files dont want to crawl for google, yahoo

# When analyzing a site for security issues, see this file
# If developer says not to crawl these, can look here as can
# be sensitive

# Example file: https://www.reddit.com/robots.txt

import urllib
import requests


def get_robots_text(url):
	print "\nRunning get_robots_text for url: {}".format(url)
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'

	r = requests.get(path + "robots.txt")
	#print "r.content is: \n{}".format(r.content) 
	return r.content

if __name__ == "__main__":
	print get_robots_text("http://www.reddit.com")
