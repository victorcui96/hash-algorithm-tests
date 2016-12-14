Some small Python experiments to try and use brute-force to break two properties of a good hash function: The one-way property and the collision-free property. 

I'm using brute force to see how long it takes to break each of these properties, where 'how long' is measured by the number of trials it takes to break either the one-way property (i.e. 'pre-image resistant' property), or the collision-free property. 

Since most hash functions are very resistant to brute-force, it might take years to break them using brute-force. To make the task feasible, I reduced the length of the hash value to 24 bits. I also used MD5 as my hash algorithm. 

To run the experiments to brute-force the one-way property, % python oneWayProperty.py in the terminal. To run the experiments to brute-force collision resistance, % python collisionResistant.py in terminal.

You implement your own experiment yourself by following the instructions located at http://www.cis.syr.edu/~wedu/seed/Labs_12.04/Crypto/Crypto_Hash/Crypto_Hash.pdf

