import pandas as pd
from sklearn import tree
from sklearn.datasets import load_iris

def main():
    calc_lowest_entropy()


# Takes an 2 dimenson array or dataframe
# and calculates the entropy of the data
# def calc_entropy(data_array):
#     sum_cases = 
#     -((4/14) np.log2(4/14) + (10/14) np.log2(10/14))

def calc_lowest_entropy():
    data = pd.read_csv('./ml-bugs.csv')
    color = data['Color']
    length = data['Length (mm)']
    X = [color, length]
    Y = data['Species']
    print(X)
    print(Y)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    print(clf)

main()
