# coding:UTF-8

import pandas as pd
import numpy as np



def load_data(fileName):
	df = pd.read_scv(fileName, header = None, sep = '\t')
	feature = df.iloc[:, :-1]
	label = df.iloc[:, [-1]]
	return np.mat(feature), np.mat(label)


def sigmoid(x):
	return 1.0 / (1 + np.exp(-x))


def FM(feature, label, k, maxCycle, alpha):
	m, n = np.shape(feature)
	w0 = 1
	weight = np.zeros((n, 1))
	V = np.random.normal(size=(n, k))

	for it in range(maxCycle):
		for x in range(m):
			colSum = feature[x] * V
			eleSquare = np.multiply(feature[x], feature[x]) * np.multiply(V, V)
			interaction = np.sum(np.multiply(colSum, colSum) - eleSquare) / 2.0
			yHat = w0 + feature[x] * weight + interaction
			loss = sigmoid(label[x] * yHat[0, 0]) - 1
			# update parameter
			w0 = w0 + alpha * loss * label[x]
			weight = weight + alpha * loss * label[x] * feature[x].T
			for i in range(n):
				for j in range(k):
					V[i, j] = V[i, j] - alpha * loss * label[x] * (feature[x, i] * (colSum[0, j] - V[i, j] * feature[x, i]))

	return w0, weight, V



def main():
	feature, label = load_data('./data.txt')
	w0, weight, V = FM(feature, label, 3, 10000, 0.01)


if __name__ == '__main__':
	main()