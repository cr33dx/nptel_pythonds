import math
def isPrime(lis):
	flag = 0
	#print("is prime is called")
	for i in range(2,(lis[0]//2)+1):
		if(lis[0]%i == 0):
			flag = 1
			break
	if(flag == 1):
		return False
	elif flag == 0 and len(lis) > 1:
		lis = lis[1:]
		#print(lis)
		return isSq(lis)
	if len(lis) == 1 and flag == 0:
		#print("I was called from isPrime")
		return True

def isSq(lis):
	x = math.sqrt(lis[0])
	#print("Value of x is" + str(x))
	#print("lent of lis "+ str(len(lis)))
	if(x % 1 != 0):
		return False
	elif(x % 1 ==0 and len(lis) > 1):
		lis = lis[1:]
		#print("isSq "+str(lis))
		return isPrime(lis)
	if len(lis) ==1 and x%1 == 0:
		#print("i was finaaly called and value of x was " + str(x))
		return True

def primesquare(lis):
	if(isPrime(lis) or isSq(lis)):
			return True
	else:
		return False
