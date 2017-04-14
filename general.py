import os

# New directory for each target/website
def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	else:
		print "{} already exists!".format(directory)

# Write data into file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()
