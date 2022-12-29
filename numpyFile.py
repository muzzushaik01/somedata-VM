import numpy as np
'''
list_a=[1,2,3,4]
list_b=[5,6,7,8]
#print(list_a * list_b)

numpy_a=np.array([1,2,3,4])
numpy_b=np.array([5,6,7,8])
#print(numpy_a*numpy_b)
#common properties
numpyBasic_array=np.array([1,2,3.5,4,"a"])
#print(numpyBasic_array.dtype)    #u32 unicode-32
#print(numpyBasic_array.itemsize)
#print((numpyBasic_array.size))

#2D-array
#array_1D=np.array(([[[1,2,3],[3,4,5],[1,2,3],[3,4,5]]]))
#array_2D=np.array([[1,2,3],[4,5.0,6],[7,8,9]])
#print(array_2D)
#print(array_1D)
#print("Dimensions: {}".format(array_1D.ndim))
#print("Array Dtype: {}".format(array_1D.dtype))
#print("Dimensions: {}".format(array_2D.ndim))
#print("Array Dtype: {}".format(array_2D.dtype))
array_2D=np.array([1,2,3],dtype='float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)
array_x=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(array_x)
print(array_x.size)
print(array_x[1,2])
print(array_x[0,2])
print(array_x[:,2])
print(array_x[:,-1])
print(array_x[1])
#step-step :end: stepsize
print(array_x[0,0: 4: 2])
print(array_x[:, 0:4:2])
array_x[0,2]=10
array_x[:,2]=10

#3D
array_3D=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#print(array_3D[0,1,0])
#print(array_3D[:,:,0])
#We update the values in the matrix as below format
array_3D[0,:,1] = [200,300]
array_3D[:,:,0] = [[100,200],[300,400]]
print(array_3D.shape)
print(array_3D)
#shape = represents(no of axes, no of rows, no of colums)
#if the number of rows and columns differ then it may rise visibledeprecationError
#how ever we can also create custom arrays

#common arrays
#one's two's empty
print(np.zeros(3))
print(np.ones((3)))
two_d=np.zeros((2,3,3))
print(two_d)  

four_d=np.zeros((3,3,3,2))
#4D represents the 3 arrays, 3 axes, 3 rows, 2 columns
#array start with [ [[[ ]]] represents one array
#print(four_d)
four_d=np.zeros((3,3,3,2),dtype="int32")
print(np.zeros((3,3)))
print(np.full((4,4),(1,2,3,4)))

#fulllike
array_m = [1,2,3]
print(np.full_like(array_m))

array_zeros=np.zeros((3,3),dtype="int32")
array_zeros[1,1]=5
print(array_zeros)
updated_array=np.zeros((5,5),dtype = "int16")
updated_array[1:-1,1:-1]=array_zeros
print(updated_array)

array_x=np.array([1,2,3,4])
array_y=array_x
array_y[0]=7
print(array_y)

a=np.array([0,30,45,60,90])
sin=np.sin(a*np.pi/180)
A=np.arcsin(sin)
print(A)


#-------------------------------------------------------------------
array_stats=[[3,2,1, 8],[4,5,-6, 0]]
print(array_stats)
print(np.min(array_stats))
print(np.min(array_stats,axis=0))
print(np.min(array_stats,axis=1))

#print(np.max(array_stats))
#print(np.max(array_stats,axis=0))
#print(np.max(array_stats,axis=1))

print(np.sum(array_stats,axis=1))


one_d=np.arange(6)
print(one_d)

two_d=np.arrange(12)
four_d=np.arange(120).reshape(2,3,4,5)
print(four_d)
print(four_d.shape)


array_1=np.array([10,20,30,40])
array_2=np.array([20,30,40,50])
print(array_1*array_2)
print(array_1 @ array_2)
print(array_1.dot(array_2))

#stacking
a_v1=np.array([1,2,3])
a_v2=np.array([4,5,6])
a_v3=np.array([7,8,9])
print(np.array([a_v1,a_v2,a_v3]))
print(np.hstack([a_v1,a_v2,a_v3]))

#numpy array as a list

array_l=np.array([1,2,3,4,5,6,7,8,9,0,12,13,14])
print(array_l[[1,3,5,7,4]])
'''
def numpy_function(x,y,z):
    return x+y+z
b=np.fromfunction(numpy_function,(2,4,5),dtype='int32')
print(b)










