def insertion(lis):
	for i in range(1,len(lis)):
		pos = lis[i]
		j = i - 1
		while(j>=0 and pos<lis[j]):
			lis[j+1] = lis[j]
			j-=1
		lis[j+1] = pos
	return lis
print(insertion([9,8,1,2,3,7]))
