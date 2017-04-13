import os

# "host url" gives IP Address of the url
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
print "ipAddress is: {}".format(get_ip_address(domainName))
