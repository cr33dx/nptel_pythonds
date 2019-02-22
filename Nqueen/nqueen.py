def checkValid(mat,x,y):
	for i in range(len(mat)):
		if(mat[x][i] == True):
			return True
	for i in range(len(mat)):
		if(mat[i][y] == True):
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
	else:
		print (table)
	for i in range (n):
		for j in range(n):
			if(checkValid(table,i,j)):
				continue
			table[i][j] = True
			if(nqueen(table,n-1)):
				return True
			table[i][j] = False
	return False


nqueen([[False]*4 for _ in range(4)],4)
