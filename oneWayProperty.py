import random
import string
import hashlib
#Preimage resistance -> For a given h in the output space of hash function, it's hard to find any message x with H(x) = h
#the 'h' we are checking against
HASH_VALUE = '286755'
numTrials = 0
while True:
	#generates random strings of length 20
	randomStr = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(20)])
	#hash the random string, using MD5	
	hash_object = hashlib.md5(randomStr.encode())
	#get a HEX string representing the hash
	hash_string = hash_object.hexdigest()
	#check first 24 bits of hash value against our 'h'
	numTrials += 1
	if hash_string[0:6] == HASH_VALUE:
		break;
print "num trials to break one-way property = "
print numTrials
