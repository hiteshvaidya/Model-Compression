'''
PRUNING STAGE:
Program for selection of edges of neural network
Version: 1.0
Logic: Selection of edges using fractional knapsack algorithm
Developer: Hitesh Vaidya
'''

import numpy as np
import csv

def read():
	fname = input("Enter name of the weights file: ")
	with open(fname) as csvfile:
		readcsv = csv.reader(csvfile, delimiter=',')
		layer = np.array(list(readcsv))
		inpt = []
		wt = []
		net = []
		for tmp1 in layer:
			inp_tmp = []
			wt_tmp = []
			tmp3 = 0
			for tmp2 in tmp1:
				if 'x' in tmp2:
					inp_tmp.append(float(tmp2[0]))
					wt_tmp.append(float(tmp2[2:]))
					tmp3 = tmp3 + float(tmp2[0]) * float(tmp2[2:])
				else:
					np.delete(tmp1,tmp1.tolist().index(tmp2),0)
					continue
			inpt.append(inp_tmp)
			wt.append(wt_tmp)
			net.append(tmp3)
		'''
		print("inputs: ",end="")
		print(inpt)
		print("weights: ",end="")
		print(wt)
		print("net: ",end="")
		print(net)
		'''
	return np.array(inpt),np.array(wt),np.array(net)

def prune(edges, net, inpt):
	diff = 0
	tmp = []
	for num in inpt:
		if net%num == 0:
			tmp.append([num,net/num])
	if len(tmp)>1:
		maxm = 0
		mark = 0
		for max_ip in range(len(tmp)):
			if tmp[max_ip][0] > maxm:
				maxm = tmp[max_ip][0]
				mark = max_ip
		edges.append(tmp[mark])
		return edges
	elif len(tmp)==1:
		edges.append(tmp[0])
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

inpt,wt,net = read()
for count in range(len(net)):
	edges = []
	pruned_nn = prune(edges, net[count], inpt[count])
	print("Layer ",count+1,":")
	print(" ---------------------------------------------------------------------------------------------------")
	print("| Input and weight combination before pruning:",end="")
	print("\t|\tInput and weight combination after pruning: |")
	print("|\tInputs     |      Weights",end="")
	print("\t\t|\t\tInputs      |     Weights\t    |")
	print("|------------------|----------------------------|---------------------------|-----------------------|")
	index3 = 0
	for index2 in range(len(inpt[count])):
		print("|\t",inpt[count][index2],"\t   | \t ",wt[count][index2],end="")
		if index3 < len(pruned_nn):
			print("\t\t\t|\t\t",pruned_nn[index3][0],"\t    |\t  ",pruned_nn[index3][1],"\t\t    |")
			index3 += 1
		else:
			print("\t\t\t|\t\t\t    |\t\t\t    |")
	print(" ---------------------------------------------------------------------------------------------------")

print()