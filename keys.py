import math, random

def oddPart(m):
    while m%2==0:
        m//=2
    return m

def MillerRabin(a,n):
    if n==2:
        return True
    if n%2==0:
        return False
    m=oddPart(n-1)
    k=int(math.log((n-1)/m,2))
    b=pow(a,m,n)
    if b==1 or b==n-1:
        return True
    else:
        for i in range (1,k):
            b=pow(b,2,n)
            if b==n-1:
                return True
            elif b==1:
                return False
        return False
    
def MRPrimality(n,k):
    for i in range(1,k+1):
        a=random.randint(2,n-1)
        test=MillerRabin(a,n)
        if test==False:
            return False
    return True

def LargePrime():
    a=10**119
    b=10**120-1
    isprime=False
    while isprime==False:
        p=random.randint(a,b)
        isprime=MRPrimality(p,100)
    return p

#Sourced from https://www.extendedeuclideanalgorithm.com/code.php
def xgcd_nonrecursive(a, b):
	""" Calculates the gcd and Bezout coefficients, 
	using the Extended Euclidean Algorithm (non-recursive).
	(Source: extendedeuclideanalgorithm.com/code) 
	"""
	#Set default values for the quotient, remainder, 
	#s-variables and t-variables
	q = 0
	r = 1
	s1 = 1 
	s2 = 0
	s3 = 1 
	t1 = 0 
	t2 = 1
	t3 = 0
	
	'''
	In each iteration of the loop below, we
	calculate the new quotient, remainder, a, b,
	and the new s-variables and t-variables.
	r decreases, so we stop when r = 0
	'''
	while(r > 0):
		#The calculations
		q = math.floor(a/b)
		r = a - q * b
		s3 = s1 - q * s2
		t3 = t1 - q * t2
		
		'''
		The values for the next iteration, 
		(but only if there is a next iteration)
		'''
		if(r > 0):
			a = b
			b = r
			s1 = s2
			s2 = s3
			t1 = t2
			t2 = t3

	return abs(b), s2, t2

def eEXP(p,q):
    n=p*q
    phin=(p-1)*(q-1)
    exp=False
    while exp==False:
       e=random.randint(1,phin-1)
       a=xgcd_nonrecursive(e,phin)
       if (a[0]==1):
            exp=True
    return e

def dEXP(e,p,q):
    phin=(p-1)*(q-1)
    b=xgcd_nonrecursive(e,phin)
    if b[0]!=1:
         print("Error")
    return b[1]%phin

def Encrypt(t,e,n):
    return pow(t,e,n)

def Decrypt(c,d,n):
     return pow(c,d,n)

def main():
    #Generate two large primes using the Large Prime method
    #Regenerate p if it is equal to q so that the message cannot be easily decrypted.
    p=LargePrime()
    q=LargePrime()
    while p==q:
        q=LargePrime()
    n=p*q
    phin=(p-1)*(q-1)
    e=eEXP(p,q)
    d=dEXP(e,p,q)
    public_key=(e,n)
    private_key=(d,p,q)
    #Replace path with filename of where keys will be stored
    with open('/path/to/key/directory', 'w') as file:
        file.write("Public Key is:\n")
        file.write(f"e={public_key[0]}\n")
        file.write(f"n={public_key[1]}\n")
        file.write("Private key is:\n")
        file.write(f"d={private_key[0]}\n")
        file.write(f"p={private_key[1]}\n")
        file.write(f"q={private_key[2]}\n")

if __name__=='__main__':
     main()