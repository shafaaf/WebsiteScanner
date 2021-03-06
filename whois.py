# whois gives info about who registered domain name, or through
# gives phone number, address, full name

# When making a website and buying domain name or registering domain name
# theres an option to buy domain name privacy around $10/yr but worth it 
# or else personal info out in public

# Need top level domain. No http or www

import os

def get_whois(url):
	print "\nRunning get_whois for: {}".format(url)
	command = "whois " + url
	process = os.popen(command)
	results = str(process.read())
	#print "results is: {}".format(results)
	return results

# Example program
if __name__ == "__main__":
	domainName = "developersfoundation.ca"
	print "Running whois test program for: {}".format(domainName)
	print "whois says: \n{}".format(get_whois(domainName))
