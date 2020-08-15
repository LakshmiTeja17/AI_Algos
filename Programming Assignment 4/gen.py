#NAME: J LAKSHMI TEJA
#ID: 2017A7PS0068P

def init(num_var):
	var_list = {}
	domain_list = [] 
	const_graph = []
	for i in range(num_var):
		domain_list.append([])
		const_graph.append([])
	
	return (var_list, domain_list, const_graph)

def loadDefaultDomains(domain_list):
	'''for i in range(20):
		domain_list[i].extend( range(8))'''
	domain_list[0].extend([2,5,7])
	domain_list[1].extend([1,4,6,2])
	domain_list[2].extend([2,5,6,1])
	domain_list[3].extend([2,4,6,8])
	domain_list[4].extend([2,6,5])
	domain_list[5].extend([1,5,3])
	domain_list[6].extend([2,4,6,1,8])
	domain_list[7].extend([1,3,4])
	domain_list[8].extend([4,1,5,8,6])
	domain_list[9].extend([8])
	domain_list[10].extend([2,3])
	domain_list[11].extend([1,2,3,4,7])
	domain_list[12].extend([7,1,8])
	domain_list[13].extend([5,3,6,1])
	domain_list[14].extend([2,5])
	domain_list[15].extend([2,5,1,4])
	domain_list[16].extend([1,4,5,6])
	domain_list[17].extend([5,4])
	domain_list[18].extend([1,3,6,8])
	domain_list[19].extend([6])

def loadDefaultConstraintGraph( const_graph):
	const_graph[0].extend([1,2,4,7,8,11,12,17,18,19])
	const_graph[1].extend([0,2,4,7,8,11,17,18,19])
	const_graph[2].extend([0,1,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19])
	const_graph[3].extend([2,4,7,8,9,11,15,18,19])
	const_graph[4].extend([0,1,2,3,6,7,8,9,10,11,13,15,16,17,18,19])
	#const_graph[5].extend()
	const_graph[6].extend([2,4,7,8,10,12,13,18,19])
	const_graph[7].extend([0,1,2,3,4,6,8,9,10,11,12,14,15,17,18,19])
	const_graph[8].extend([0,1,2,3,4,6,7,9,10,11,12,14,15,16,17,18,19])
	const_graph[9].extend([2,3,4,7,8,10,11,16,17,18,19])
	const_graph[10].extend([2,4,6,7,8,9,13,16,17,18,19])
	const_graph[11].extend([0,1,2,3,4,8,7,9,14,17,18,19])
	const_graph[12].extend([0,2,6,7,8,18,19])
	const_graph[13].extend([2,4,6,10,19])
	const_graph[14].extend([7,8,11,15,16,17,18,19])
	const_graph[15].extend([2,3,4,7,8,14,16,17,18,19])
	const_graph[16].extend([2,4,8,9,10,14,15,16,17,18,19])
	const_graph[17].extend([0,1,2,4,7,8,9,10,11,14,15,16,18,19])
	const_graph[18].extend([0,1,2,3,4,6,7,8,9,10,11,12,14,15,16,17,19])
	const_graph[19].extend([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18])

def loadDomains(domain_list):
	for i in range(len(domain_list)):
		print("Input the domain lists:")
		string = input("Give comma seperated domain values for variable " + str(i) + "\n(WARNING: Do not use a space after comma. Sample input: 1,2,3):\n")
		l = string.split(",") 	
		l = map( int, l)
		domain_list[i].extend(l)
		print()

	print()

def loadConstraintGraph( const_graph):
	for i in range(len(const_graph)):
		print("Input the constraint graph:")
		string = input("Give comma seperated numbers of the variables involved in a constraint with variable N" + str(i) + "\n(WARNING: Do not use a space after comma. For example, for N1, N2, N3 the sample input is: 1,2,3):\n")
		l = string.split(",") 	
		l = map( int, l)
		l = [x - 1 for x in l]
		const_graph[i].extend(l)
		print()
	print()	
