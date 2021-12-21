import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def error_rate(predict, label):
    m = np.shape(predict)[0]
    sum_err = 0.0
    for i in range(m):
        if predict[i, 0] > 0 and (1 - predict[i, 0]) > 0:
            sum_err -= (label[i,0] * np.log(predict[i,0]) + (1-label[i,0]) * np.log(1-predict[i,0]))
        else:
            sum_err -= 0
    return sum_err / m


def save_model(fileName, weight):
	weight = pd.DataFrame(weight)
	weight.to_csv(fileName, header = None, index = None)


def LR(feature, label, maxCycle, alpha):
    n = np.shape(feature)[1]
    weight = np.mat(np.ones((n, 1)))

    for i in range(maxCycle):
        predict = sigmoid(feature * weight)
        err = label - predict
        if (i + 1) % 100 == 0:
            print("\titer = " + str(i + 1) + " , train error rate = " + str(error_rate(predict, label)))
        weight = weight + alpha * feature.T * err
    return weight


def main():
	fileName = './data.txt'
	df = pd.read_csv(fileName, header = None, sep = '\t')
	feature = df.iloc[:, :-1].copy()
	pos = np.shape(np.array(feature))[1]
	feature.insert(value = 1, loc = pos, column = "one")
	label = df.iloc[:, [-1]].copy()

	feature = np.mat(feature)
	label = np.mat(label)
	weight = LR(feature, label, 1000, 0.01)
	save_model('weight.txt', weight)


if __name__ == '__main__':
	main()