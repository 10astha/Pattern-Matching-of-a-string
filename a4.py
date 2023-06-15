import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):
	return math.ceil(((10*m)/eps)*(math.log2((10*m)/eps)))

	# we calculated  N such that for every prime number less than N probability of false answer will be less than epsilon
    # we used inequality : (2*log(N)*log((26)**M)/N<eps
# Return sorted list of starting indices where p matches x

def ord1(s): #here we defined a function which gives numerical value for uppercase alphabets {A:1,B:2,C:3,D:4,E:5..........Z:26} 
	#and zero for "?" which we use for wildcard problem
	if s=="?":
		return 0
	else:
		return ord(s)-64

def modPatternMatch(q,p,x):
	res,m,n,i,P,t,d=[],len(p) , len(x),0,0,0,26
	h=1
	for i in range(1,m): # THIS GIVES US 26**(m-1) , we here use loop for the sake if space complexity
		h=(h*d)%q

	
	i=0
	while i<m: # finding fucntion f(y) values for pattern(P) and text(t)
		P = (d*P + ord1(p[i])) % q 
		t = (d*t + ord1(x[i])) % q

		i+=1
	for i in range(n-m+1): 
		if P == t:# if f(y) value matches then we store it in the list
			res.append(i)
		if i < n-m:# if P is not equal to t then we shift the i to i+1 and find f(y) value for f(x[i+1:i+1+m]) 
			# we do this by deleting the f(x[i])%q and multiplying the remaining by d and finally adding thw weight of new alphabet that is x[i+m+1]
# suppose we have a text s0s1s2s3s4s5s6s7 and pattern of length 5 that is m=5
#f(x[s0s1s2s3s4])=d^4(ord1(s0))+d^3(ord1(s1))+d^2(ord1(s2))+d(ord1(s1))+(ord1(s0))			
# f(s1s2s3s4s5)=d^4(ord1(s1))+d^3(ord1(s2))+d^2(ord1(s3))+d(ord1(s4))+(ord1(s5))	
#f(s1s2s3s4s5)=(f(s0s1s2s3s4)-d^4*ord1(s0))*d+ord1(s5)
			t = (d*(t-ord1(x[i])*h))%q
			t+=(ord1(x[i+m]))%q
			
	return res

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
	
	res,m,n,i,P,t,d=[],len(p) , len(x),0,0,0,26
	h=1
	for i in range(1,m):
		h=(h*d)%q
	i=0
	while i<m:
		if p[i]=="?":
			I=i
		P = (d*P + ord1(p[i])) % q
		t = (d*t + ord1(x[i])) % q
		i+=1
	for i in range(n-m+1):
	# here we did slight changes by assigning 0 to "?"
#for a given substring of length m we deleted weight of the alphabet wight at index I where I=p.index("?")  and if value matches we haave our ans
# else checking for the next substrings
		if P == (t-(pow(26,m-I-1)*ord1(x[i+I])))%q:
				res.append(i)
		if i < n-m:
			t = (d*(t-ord1(x[i])*h))%q
			t+=(ord1(x[i+m])) % q
	return res
