from random import shuffle
f=open("kargerMinCut.txt")
edges=[]
vertices=[]
for line in f:
	s=line.split()
	vertices.append(int(s[0]))
	i=1
	while(i<(len(s))):
		if(([int(s[0]),int(s[i])] not in edges) and ([int(s[i]),int(s[0])] not in edges)):
			edges.append([int(s[0]),int(s[i])])
		i+=1

def Karger(edges, vertices):
	while(len(vertices)>2):
		remove=edges[0]
		edges=edges[1:]
		vertices.remove(remove[1])
		temp=list(edges)
		to_del=[]
		i=0
		while(i<len(temp)):
			if(edges[i][0]==remove[1]):
				to_del.append([edges[i][0],edges[i][1]])
				edges.append([remove[0],edges[i][1]])

			if(edges[i][1]==remove[1]):
				to_del.append([edges[i][0],edges[i][1]])
				edges.append([edges[i][0],remove[0]])

			if(edges[i][0]==edges[i][1]):
				to_del.append([edges[i][0],edges[i][1]])
			i+=1
		edges=[item for item in edges if item not in to_del]

	to_del=[]

	i=0
	while(i<len(edges)):
		if(edges[i][0]==edges[i][1]):
			to_del.append([edges[i][0],edges[i][1]])
		i+=1
	edges=[item for item in edges if item not in to_del]
	return len(edges),vertices,edges

mincut=len(edges)

for i in range(10):
	# shuffle(edges)
	x,y,z=Karger(edges, vertices)
	if mincut>x:
		mincut=x
		ver=y
		ed=z
print("mincut, ver, edges", mincut, ver, ed)