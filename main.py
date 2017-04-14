import sys

from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_text import *
from whois import *

ROOT_DIR = "companies"
create_dir(ROOT_DIR)

#------------------------------------------------------------------------

# name is name of file as according to user
def gather_info(url):
	domain_name = get_domain_name(url)	
	ip_address = get_ip_address(url)
	
	nmap = get_nmap('-F', ip_address)
	robots_text = get_robots_text(url)
	whois = get_whois(domain_name)

	# Save results in text file
	create_report(url, domain_name, nmap, robots_text, whois)

#------------------------------------------------------------------------

def create_report(url, domain_name, nmap, robots_text, whois):
	project_dir = ROOT_DIR + "/" + domain_name
	create_dir(project_dir)
	write_file(project_dir + "/url.txt", url)
	write_file(project_dir + "/domain_name.txt", domain_name)
	write_file(project_dir + "/nmap.txt", nmap)
	write_file(project_dir + "/robots_text.txt", robots_text)
	write_file(project_dir + "/whois.txt", whois)

#------------------------------------------------------------------------

# Example program
if __name__ == "__main__":
	url = "http://www.thenewboston.com"
	print "Running main test program for: {}".format(url)
	gather_info(url)

#------------------------------------------------------------------------
