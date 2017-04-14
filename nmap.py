import os

# e.g command: nmap -F ipAddress
# works even if no spaces are provided
def get_nmap(options, ip):
	print "\nRunning get_nmap for ip: {}".format(ip)
	command = "nmap " + options + " " + ip
	process = os.popen(command)
	results = str(process.read())
	#print "results is: {}".format(results)
	return results

if __name__ == "__main__":
	print "Running nmap test program"
	print get_nmap('-F', "54.186.250.79")
