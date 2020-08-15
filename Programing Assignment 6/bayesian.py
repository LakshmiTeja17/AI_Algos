#NAME: J LAKSHI TEJA
#ID: 2017A7PS0068P

def createBayesianNetwork( inp_file):
	line = inp_file.readline()
	parent_list = {}
	cpt_list = {}
	while( line != "$$\n"):
		node, parents, cpt = line.split(" >> ")
		cpt = cpt.split()
		cpt = list(map( float, cpt))
		parents = parents.split(", ")
		parents[0] = parents[0][1:]
		parents[-1] = parents[-1][:-1]
		if( parents[0] != ''):
			parent_list[node] = parents
		else:
			parent_list[node] = []
		cpt_list[node] = cpt
		line = inp_file.readline()

	network = (parent_list, cpt_list)
	return network
	#print(parent_list)
	#print(cpt_list)
	
def computeMarkovBlanket( network, node):
	blanket = []
	parent_list, cpt_list = network
	blanket.extend( parent_list[node])
	children = []
	for n in parent_list:
		for parent in parent_list[n]:
			if( parent == node):
				children.append(n) 
				break

	for child in children:
		blanket.extend( parent_list[child])
		blanket.append(child)

	blanket = list(set(blanket))
	return blanket 

def nextCombo(other_list):
	#print( "before:", other_list)
	pos = -1
	temp = []
	for key in other_list.keys():
		temp.append(other_list[key])

	pos = 0
	for pos in range(len(temp)):
		if( temp[ len(temp) - 1 - pos] == 0):
			temp[ len(temp) - 1 - pos] = 1
			break

	for pos in range( len(temp) - pos, len(temp)):
		temp[pos] = 0

	pos = -1
	for key in other_list.keys():
		pos+=1
		other_list[key] = temp[pos]

	#print( other_list)

			 
def computeProbability( network, expression):
	prob = 0
	parent_list, cpt_list = network
	query_list, cond_list = expression
	other_list = {}
	for node in parent_list.keys():
		if (node not in query_list.keys() and node not in cond_list.keys()):
			other_list[node] = 0

	var_list = {}
	var_list.update(query_list)
	var_list.update(cond_list)

	for i in range( 2** len(other_list)):
		var_list.update(other_list)
		prob += computeJointProb( network, var_list)
		nextCombo( other_list)

	return prob
	
def computeJointProb(network, var_list):
	prob = 1
	parent_list, cpt_list = network
	for var in var_list:
		pos = 0
		parents = parent_list[var] 
		temp = len(parents)
		for i in range(len(parents)):
			if parents[i] == '':
				continue
			pos+= var_list[parents[i]] * ( 2** (temp - 1- i))
		
		#print( "jjj", cpt_list[var][pos])
		if( var_list[var] == 1):
			prob *= cpt_list[var][pos]
			#print("At ", var, prob)
		else:
			prob *= (1 - cpt_list[var][pos]	)
			#print("At ~", var, prob)		

	return prob

		 
		
