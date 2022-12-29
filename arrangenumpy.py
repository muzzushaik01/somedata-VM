import numpy as np
x = np.arange(5, dtype = "int16")
print(x)
y = np.arange(1,5,2)
print(y)
z = np.arange(1,9, 4)[::-1]
print(z)
w = np.flip(np.arange(1,9, 4))
print(w)
r = np.arange(2,2)
print(r)
print(r.itemsize)
#to square the elements in the array
print(x**2)
#to get trignometric values
t = np.sin(x)
print(t)
u = np.arange(-1,1.1,0.5)
print(u)
#absolute function is used to get positive values
v = np.abs(u)
print(v)
#arranging the array with numbers
i = np.arange(6).reshape((2,3))
print(i)

print(i.ndim)


#----------------------------------------------------------------------
array_stats=[[1,2,3],[4,5,6]]
print(np.min(array_stats))
print(np.min(array_stats,axis=0))
