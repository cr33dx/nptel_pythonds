def matrixflip(lis,flip):
	lix = lis[:]
	if flip == 'h':
		for i in range(len(lix)):
				for j in range(len(lix[i])//2):
					(lix[i][j],lix[i][len(lix[i])-1-j]) = (lix[i][len(lix[i])-1-j],lix[i][j])
	if flip == 'v':
		for i in range(len(lix)//2):
			(lix[i],lix[len(lix)-1-i]) = (lix[len(lix)-1-i],lix[i])
	return lix