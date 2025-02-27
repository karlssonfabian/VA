""" Python interface to the C++ Person class """
import ctypes

path = 'C:/Users/Fabian/OneDrive - Uppsala universitet/Universitet/År 4/Programmeringsteknik 2/Inlämningar/VA/VA_files/libperson.dll'
lib = ctypes.cdll.LoadLibrary(path)

class Person(object):
	def __init__(self, age):
		lib.Person_new.argtypes = [ctypes.c_int]
		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_getAge.argtypes = [ctypes.c_void_p]
		lib.Person_getAge.restype = ctypes.c_int
		lib.Person_setAge.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_getDecades.argtypes = [ctypes.c_void_p]
		lib.Person_getDecades.restype = ctypes.c_int
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Person_new(age)

	def getAge(self):
		return lib.Person_getAge(self.obj)

	def setAge(self, age):
		lib.Person_setAge(self.obj, age)

	def getDecades(self):
		return lib.Person_getDecades(self.obj)
        
	def __del__(self):
		return lib.Person_delete(self.obj)