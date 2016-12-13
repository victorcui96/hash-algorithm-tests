import hashlib
import binascii
#this python script is designed to print out the differing number of bits between two files ('msg1.txt' and 'msg2.txt'). The contents of these two files were put through the MD5 hash algorithm
file1 = open("msg1.txt", "r")
file2 = open("msg2.txt", "r")
file1Contents = file1.read()
file2Contents = file2.read()
#run the file contents through MD5 algorithm
hash_object1 = hashlib.md5(file1Contents)
hash_object2 = hashlib.md5(file2Contents)
hashString1 = (hash_object1.hexdigest())
hashString2 = (hash_object2.hexdigest())
#converts HEX string into integer
file1Binary = int(hashString1, 16)
file2Binary = int(hashString2, 16)
#formats integer into binary
file1Binary = format(file1Binary, '0>42b')
file2Binary = format(file2Binary, '0>42b')
numDifferentBits = 0
for x in xrange(0, len(file1Contents)):
	if int(file1Binary[x]) != int(file2Binary[x]):
		numDifferentBits += 1
print 'Num different bits = '
print numDifferentBits
