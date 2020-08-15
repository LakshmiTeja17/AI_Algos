#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

def AC3( domain_list, const_graph):
	queue = []
	for i in range(len(const_graph)):
		for num in const_graph[i]:
			queue.append((i,num))

	while( len(queue) != 0):
		arc = queue.pop()
		#print("Arc popped is", arc)
		if( revise( domain_list, const_graph, arc) ):
			if( len(domain_list[ arc[0]]) == 0):
				return False
			for num in const_graph[arc[0]]:
				if( num!= arc[1]):
					queue.append(( num, arc[0]))
					#print("Arc appended is", ( num, arc[0]))

	
	return True

def revise( domain_list, const_graph, arc):
	revised = False
	for num in domain_list[arc[0]]:
		flag = False
		for num1 in domain_list[arc[1]]:
			if( num1 != num):
				flag = True
				break
	
		if( flag == False):
			#print("deleted value is", num)
			domain_list[arc[0]].remove(num)
			revised = True

	return revised
