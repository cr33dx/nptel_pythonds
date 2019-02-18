def isPrime(n):
	flag = 0
	for i in range(2,n//2):
		if(n%i == 0):
			flag = 1
			break
	if(flag == 0):
		return True
	else:
		return False

def primepartition(n):
	if(n%2==0):
		return True
	else:
		if(isPrime(n-2)):
			return True
		else:
			return False

