import numpy as np

def prune(edges, net, inpt):
	print("edges: ",edges)
	print("inpt: ",inpt)
	print("net = ",net)
	diff = 0
	tmp = []
	for num in inpt:
		if net%num == 0:
			tmp.append([num,net/num])
			print("tmp = ",tmp)
	if len(tmp)>1:
		maxm = 0
		mark = 0
		for max_ip in range(len(tmp)):
			if tmp[max_ip][0] > maxm:
				maxm = tmp[max_ip][0]
				mark = max_ip
		edges.append(tmp[mark])
		print("final edges: ",edges)
		return edges
	elif len(tmp)==1:
		edges.append(tmp[0])
		print("final edges: ",edges)
		return edges
	else:
		mxm = np.amax(inpt)
		count = 1
		while mxm*count < net:
			count += 1
		edges.append([mxm,count-1])
		diff = net - mxm*(count-1)
		inpt = np.delete(inpt,inpt.tolist().index(mxm))
		edges = prune(edges, diff, inpt)
		return edges

edges = []
inpt = np.array([3,7])
pruned_nn = prune(edges, 10, inpt)
print(pruned_nn)

'''
combination tried:
net = 10
input = [1,3,2,4,5]		output = [[5,2]]
input = [3,7]			output = [[7,1],[3,1]]

corner case:
1) case 1:
net=10
input= 1,3
combination= 1*10 OR 1*1+3*3

2) case 2:
Repeated values of edge weights

3) case3:
Negative weight values
'''