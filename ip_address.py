import os

# "host url" gives IP Address of the url

# The Linux host command is used to find out 
# the IP address for a domain. It can also be 
# used to find the domain name for an IP address.

def get_ip_address(url):
	command = "host " + url
	# open a new process to run the command
	process = os.popen(command)
	results = str(process.read())
	print "\nresults is: {}\n".format(results)
	marker = results.find("has address") + 12 # marks to beginning of "has address" and moves 12 spots
	return results[marker:].splitlines()[0] # return first ip address


# Example program
domainName = "google.com"
print "Running get_ip_address test program for: {}".format(domainName)
print "ipAddress for {} is: {}".format(domainName, get_ip_address(domainName))
