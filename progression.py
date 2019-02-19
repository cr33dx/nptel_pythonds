def progression(lis):
	if(len(lis) != 1):
		d = lis[1] - lis[0]
		flag = 0
		for i in range(1,len(lis)):
			if ((lis[i] - lis[i-1]) != d):
				flag = 1
		if flag == 1:
			return False
		else:
			return True
	else:
		return True
