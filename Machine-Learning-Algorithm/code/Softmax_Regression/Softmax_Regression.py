# coding:UTF-8

import numpy as np
import pandas as pd


def load_data(fileName):
    df = pd.read_csv(fileName, header = None, sep = '\t')
    feature = df.iloc[:, :-1].copy()
    pos = np.shape(np.array(feature))[1]
    feature.insert(value = 1, loc = pos, column = "one")
    label = df.iloc[:, [-1]].copy()
    feature = np.mat(feature)
    label = np.mat(label)
    return feature, label


def error_rate(err, label):
    m = np.shape(err)[0]
    sum_cost = 0.0
    for i in range(m):
        if err[i, label[i, 0]] / np.sum(err[i, :]) > 0:
            sum_cost -= np.log(err[i, label[i, 0]] / np.sum(err[i, :]))
        else:
            sum_cost -= 0
    return sum_cost / m


def softmax_regression(feature, label, maxCycle, alpha, k):
    m, n = feature.shape
    weight = np.mat(np.ones((n, k)))

    for i in range(maxCycle):
        err = np.exp(feature * weight)
        if i % 500 == 0:
            print("\titer = " + str(i) + " , train error rate = " + str(error_rate(err, label)))
        rowSum = -err.sum(axis = 1)
        rowSum = rowSum.repeat(k, axis = 1)
        err = err / rowSum
        for j in range(m):
            err[j, label[j, 0]] += 1
        weight = weight + alpha / m * feature.T * err
    return weight


def countNum(label):
    n = np.shape(label)[0]
    s = set()
    for i in range(n):
        s.add(label[i, 0])
    return len(s)


def save_model(fileName, weight):
    weight = pd.DataFrame(weight)
    weight.to_csv(fileName, header = None, index = None, sep = '\t')


def main():
    feature, label = load_data('./data.txt')
    weight = softmax_regression(feature, label, 10000, 0.4, countNum(label))
    save_model('./weight.txt', weight)


if __name__ == '__main__':
	main()