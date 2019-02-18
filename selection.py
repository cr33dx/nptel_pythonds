def selection (lis):
	for i in range(len(lis)):
		min = lis[i]
		for j in range(i+1,len(lis)):
			if(lis[j] < min):
				(lis[j],lis[i]) = (lis[i],lis[j])
				min = lis[j]
	print(lis)

selection([1,5,6,2,9,3,4,5,614,124,124,124124,4,0,89999,14124124,4,5,6,98,65,34,12,8,31,39,54,45])

