import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()


#gamma 
clf = svm.SVC(gamma=0.0001, C=100)

print(len(digits.data))

#training the dataset and leaving the last 2 to test on
x,y = digits.data[:-10], digits.target[:-10]


#fitting the classification
clf.fit(x,y)



#running the prediction
print('Prediction:', clf.predict(digits.data[-6].reshape(1,-1)))


#review gradient descent to udnerstand how we can arrive at the right answer
plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()




