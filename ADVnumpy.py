import numpy as np

data_from_text_file=np.genfromtxt('NumpyFiles.txt',delimiter=',')
print(data_from_text_file)

data_from_text=data_from_text_file.astype('int32')
print(data_from_text)

print(data_from_text >10)
print(data_from_text[data_from_text >10])