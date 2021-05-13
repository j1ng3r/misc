import ctypes
ctypes.cast(id(29), ctypes.POINTER(ctypes.c_int))[6] = 100

x=1+28
print(x+1)
print((1+28)+1)
print(x==100)
print(100+1)
