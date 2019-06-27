import hashlib
import base64
import uuid


SALT     = '87654321'
CRACK    = 'MbTFw0OVLeXyb6oIe9Z+GQ=='

with open('rockyou.txt', 'r') as fp:
	for cnt, line in enumerate(fp):
		line = line.lstrip().rstrip()
		t_sha = hashlib.md5()
		t_sha.update(line+SALT)
		hashed_password = base64.b64encode(t_sha.digest())
		if hashed_password == CRACK:
			print ">>>Success!!! Password: {}\nPassword was at line {} in the wordlist".format(line, cnt)
			break
		if cnt % 2 == 0:
			print "Attempting Pass No. {}".format(cnt)
