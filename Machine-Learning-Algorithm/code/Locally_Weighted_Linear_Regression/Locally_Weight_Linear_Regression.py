import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter


# style setting
GOLD_RATIO = 1.618
MINIMAL_WIDTH = 3.54
SHORT_HEIGHT = MINIMAL_WIDTH / GOLD_RATIO
plt.rcParams['figure.figsize'] = MINIMAL_WIDTH, SHORT_HEIGHT
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['legend.loc'] = 'best'
plt.rcParams['legend.fontsize'] = 'medium'
plt.rcParams['font.size'] = 8


def lwlr(feature, label, k):
    m = np.shape(feature)[0]
    predict = np.zeros(m)
    weight = np.mat(np.eye(m))
    for i in range(m):
        for j in range(m):
            diff = feature[i, ] - feature[j, ]
            weight[j, j] = np.exp(diff * diff.T / (-2 * k ** 2))
        xTWx = feature.T * (weight * feature)
        theta = xTWx.I * (feature.T * (weight * label))
        predict[i] = feature[i, ] * theta
    return predict


def sortXY(feature, predict):
    L = sorted(zip(feature, predict), key = itemgetter(0))
    sort_feature, sort_predict = zip(*L)
    return sort_feature, sort_predict


def plotFigure(feature, predict, label, k):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	sort_feature, sort_predict = sortXY(np.array(feature[: , 0]), predict)
	plt.scatter(np.array(feature[: , 0]), np.array(label), s = 5)
	plt.plot(sort_feature, sort_predict, color='r', linewidth=1.5)
	plt.legend(labels = ['predict', 'data'])
	plt.title('k = ' + str(k))
	plt.xlabel('feature')
	plt.ylabel('label')
	plt.show()
	plt.savefig('./k=' + str(k) + '.png', bbox_inches = 'tight')


def main():
	fileName = './data.txt'
	df = pd.read_csv(fileName, header = None, sep = '\t')
	feature = df.iloc[:, :-1].copy()
	feature.insert(value = 1, loc = 1, column = "one")
	label = df.iloc[:, [-1]].copy()

	feature = np.mat(feature)
	label = np.mat(label)

	kVal = [1.0, 0.01, 0.002]
	for k in kVal:
		predict = lwlr(feature, label, k)
		plotFigure(feature, predict, label, k)


if __name__ == '__main__':
	main()