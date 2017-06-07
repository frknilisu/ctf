#!/usr/bin/python

"""
****************************************************************
- MD5 AND SHA1 ENCRYPTION
- MD5 DECRYPTION
AUTHOR : frknilisu
****************************************************************
"""

import hashlib
import sys
import os
import time
import urllib2
import urllib 
import re
import requests

"""

usages:
python script.py e1 < strings.txt
python script.py e2 < strings.txt
python script.py d1 < hashes.txt
python script.py d2 < hashes.txt

"""

def main():
	os.system("clear")

	operation = sys.argv[1]

	if operation == "e1":
		print "md5 encryption"
		md5encryption()
	elif operation == "e2":
		print "sha1 encryption"
		sha1encryption()
	elif operation == "d1":
		print "site: http://md5decrypt.net/"
		md5onlinedecryption1()
	elif operation == "d2":
		print "site: http://md5decryption.com/"
		md5onlinedecryption2()
	else:
		print "usage: python script.py [e1 | e2 | d1 | d2]"

####################################################################################

def md5encryption():
	string=raw_input("string you want to convert to MD5 > ")
	algorithim=hashlib.md5()
	algorithim.update(string)
	encrypted=algorithim.hexdigest()
	print'%s to MD5 hash %s' %(string,encrypted)

def sha1encryption():
	string=raw_input("string you want to convert to SHA1 > ")
	algorithim=hashlib.sha1()
	algorithim.update(string)
	encrypted=algorithim.hexdigest()
	print'%s to SHA1 hash %s' %(string,encrypted)

####################################################################################

def md5onlinedecryption1():
	myhash=raw_input("")
	hashtype = "md5"
	email = "koruyucu5@hotmail.com"
	code = "132b88151552bf35"

	while True:

		if len(myhash) != 32:
			break

		website = 'http://md5decrypt.net/Api/api.php'
		payload = {'hash':myhash, 'hash_type':hashtype, 'email':email, 'code': code} 
		r = requests.post(website, params=payload)
		key = r.text
		if key.startswith("CODE ERREUR"):
			print '[-] %s' % (key)
		else:
			key = key.split()
			print '[+] Hash: %s <-> Key: %s' % (myhash, key)

		myhash=raw_input("")

def md5onlinedecryption2():
	myhash=raw_input("")

	while True:

		if len(myhash) != 32:
			break

		website = 'http://md5decryption.com/'
		payload = {'hash':myhash,'submit':'Decrypt+It!'}
		weburl = urllib.urlencode(payload)
		req = urllib2.Request(website)
		try:
			fd = urllib2.urlopen(req, weburl)
			data = fd.read()
			match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
			if match: 
				print '[+] Hash: %s <-> Key: %s' % (myhash, match.group(2))
			else: 
				print '[-] Key Not found'
		except Exception as e:
			print e.message

		myhash=raw_input("")

main()