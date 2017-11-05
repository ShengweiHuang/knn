import numpy as np
from collections import Counter

def readUCI():
	with open("iris.data") as d:
		content = d.readlines()
	content = [x.strip(',') for x in content] 
	for i in range(0, len(content)):
		content[i] = content[i].split(',')
		for j in range(0, len(content[i])):
			try:
				content[i][j] = float(content[i][j])
			except:
				content[i][j] = str(content[i][j])
	return content

def distence(dataA, dataB):
	sumVal = 0.0
	for i in range(0, len(dataA)):
		try:
			sumVal += np.power((dataA[i] - dataB[i]), 2)
		except:
			sumVal += 0
	return np.sqrt(sumVal)

def label(data, index, k):
	# let data final index be label
	for i in range(0, len(data)):
		if i != index:
			data[i].append(distence(data[i], data[index]))
		else:
			data[i].append(0.0)
	data = np.array(data)
	data = data[np.argsort(data[:,-1])]
	kData = data[1:k+1]
	kdLabel = Counter(kData[:,4]).most_common(1)[0][0]
	return kdLabel

def main():
	data = readUCI()
	for k in range(1, len(data)):
		correct = 0
		for i in range(0, len(data)):
			if label(data, i, k) == data[i][4]:
				correct += 1
		print("k=", k, ", correct rate=", correct, "/", len(data))

if __name__ == "__main__":
	main()
