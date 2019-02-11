def matched(str):
	count=0
	for i in range(0, len(str)):
		if(str[i] == '('):
			count+=1
		if(str[i] == ')'):
			count-=1
			if(count==-1):
				break
	if(count==0):
		return True
	else:
		return False

def nestingdepth(str):
	if(not matched(str)):
		return -1 
	else:
		max = 0
		depth = 0
		for i in range(0,len(str)):
			if(depth>max):
				max = depth
			if(str[i] == '('):
				depth+=1
			if(str[i] == ')'):
				depth-=1
		return max