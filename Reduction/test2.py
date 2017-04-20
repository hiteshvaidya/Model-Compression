import numpy as np
import csv

fname = input("Enter name of the weights file: ")
with open('weights.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	layer = np.array(list(readcsv))
	print(layer)