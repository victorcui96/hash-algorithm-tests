import random
import string
import hashlib
#Collision resistance -> It's hard to find a pair of messages x1 != x2 with Hash(x1) = Hash(x2) 
numTrials = 0
#pastStrings = set()
while True:
	randomString1 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(20)])
	randomString2 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(20)])
	#don't want to check any strings that have already been in set, b/c they won't produce a collision
	if randomString1 == randomString2: 
		continue;
	else:
		#encodes string in sequence of bytes b/c hashing function only takes sequence of bytes as a parameter
		#uses MD5 hashing algorithm
		hash_object_1 = hashlib.md5(randomString1.encode())
		#returns a HEX string representing the hash
		hash_string_1 = hash_object_1.hexdigest()
		hash_object_2 = hashlib.md5(randomString2.encode())
		hash_string_2 = hash_object_2.hexdigest()
		numTrials += 1
		#check first 24 bits of hash values
		if (hash_string_1[0:6] == hash_string_2[0:6]):
			break;
print "num trials to break collision-resistant property = "
print numTrials
