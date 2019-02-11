def prime(n):
	flag = 0
	for i in range(2,n):
		if(n%i == 0):
			flag +=1
			break
	if(flag == 0):
		return True
	else:
		return False
def sumprimes(l):
	sum = 0
	for i in l:
		if(prime(i) and i>1):
			sum+=i
	return sum

print(sumprimes([-3,1,6]))
