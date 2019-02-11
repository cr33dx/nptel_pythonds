def intreverse(n):
	reverse = 0
	while(n!=0):
		num = n%10
		reverse = reverse*10 + num
		n = n//10
	return reverse

