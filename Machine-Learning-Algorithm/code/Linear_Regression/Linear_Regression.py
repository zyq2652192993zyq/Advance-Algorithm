import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Least_Square(feature, label):
	return (feature.T * feature).I * feature.T * label


if __name__ == "__main__":
	df = pd.read_csv("./data.txt", header=None, sep='\t')
	feature = df.iloc[:, :-1].copy()
	feature.insert(value=1, loc=1, column="one")
	label = df.iloc[:, [-1]].copy()

	feature = np.mat(feature)
	label = np.mat(label)

	res = pd.DataFrame(Least_Square(feature, label))
	res.to_csv("result.txt", header=None, index=False)