import numpy as np
import matplotlib.pyplot as pp

#a = np.array([1,2,3,4])
#print(a)

#print(a.dtype)

#a = np.array([1,2,3,4],dtype=np.float64)
#print(a)

#print(a.ndim, a.shape, a.size)

#b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.float64)
#print(b)

#print(b.dtype, b.ndim, b.shape, b.size)

#print('zeros',np.zeros([3,3],'d'))
#print('empty',np.empty([4,4],'d'))
#print('linspace',np.linspace(0,10,5))
#print('arange',np.arange(0,10,1))
#print('random',np.random.standard_normal((2,4)))

a = np.random.standard_normal((2,3))
b = np.random.standard_normal((2,3))

print(np.vstack([a,b]))
print(np.hstack([a,b]))

print('transpose',a.transpose())
np.save('example.npy',a)
a1 = np.load('example.npy')
print('This is a1:',a1)