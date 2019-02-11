def rotatelist(list,length):
	for i in range(0,length):
		list = list[1:] + list[0:1]
	return list
