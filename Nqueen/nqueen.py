def checkValid(mat,x,y):
	for i in range(1,len(mat)):
		if(mat[(x+i)%4][y] == True):
			return True
	for i in range(1,len(mat)):
		if(mat[x][(y+i)%4] == True):
			return True
	for i in range((len(mat))):
		for j in range(len(mat)):
			if(i + j == x + y):
				if(mat[i][j] == True):
					return True
			if(i - j == x - y):
				if(mat[i][j] == True):
					return True
	return False

def nqueen(table,n): 
	if n == 0:
		print(table) 
		return True

	for i in range (len(table)):
		for j in range(len(table)):
			if(checkValid(table,i,j)):
				continue
			table[i][j] = True
			if(nqueen(table,n-1)):
				return True
			table[i][j] = False
	return False


nqueen([[False]*5 for _ in range(5)],5)
