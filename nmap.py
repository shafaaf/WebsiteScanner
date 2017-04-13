import os

# e.g command: nmap -F ipAddress
# works even if no spaces are provided
def get_nmap(options, ip):
	command = "nmap " + options + " " + ip
	process = os.popen(command)
	results = str(process.read())
	return results


print "Running nmap test program"
print get_nmap('-F', "54.186.250.79")
