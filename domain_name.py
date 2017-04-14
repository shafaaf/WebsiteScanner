# Get top level domain
# To run "whois" command, need only top level domain

# Bad idea to just strip

# Do: pip install tld before this
from tld import get_tld

# User passes in url. For example, https://thenewboston.com/
def get_domain_name(url):
	print "\nRunning get_domain_name for: {}".format(url)
	domain_name = get_tld(url)
	print "domain_name is: {}".format(domain_name)
	return domain_name


# Example program
if __name__ == "__main__":
	domainName = "https://thenewboston.com/"
	print "Running domain_name test program for: {}".format(domainName)
	print "tld is: {}".format(get_domain_name(domainName))
