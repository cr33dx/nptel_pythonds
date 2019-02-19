def insertion(lis):
	for i in range(len(lis)):
		pos = i
		while(i>0 and lis[pos]<lis[i-1]):
			(lis[pos], lis[pos-1]) = (lis[pos], lis[pos-1])
			pos -= 1
	print (lis)
insertion([9,8,7,6,5,4,3,2,1,0])
