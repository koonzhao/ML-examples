
from numpy import loadtxt, where
from pylab import scatter, show,legend, xlabel, ylabel

# load the dataset

data = loadtxt('data1.txt', delimiter=',')

x = data[:, 0:2]
y = data[:, 2]

pos = where(y == 1)
neg = where(y == 0)

scatter(x[pos, 0], x[pos, 1], marker='o', c='b')
scatter(x[neg, 0], x[neg, 1], marker='x', c='r')

xlabel('Feature1/Exam 1 score')
ylabel('Feature2/Exam 2 score')

legend(['Fail', 'Pass'])
show()

