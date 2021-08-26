import time
from ctypes import *
library = cdll.LoadLibrary("./netft.so")
sensorvalue = []
def sensor():
    global sensorvalue
    library.main.argtypes = [POINTER(c_int)]
    library.main.restype = c_void_p
    a = c_int(0)
    b = c_int(0)
    c = c_int(0)
    d = c_int(0)
    e = c_int(0)
    f = c_int(0)
    library.main(byref(a),byref(b),byref(c),byref(d),byref(e),byref(f))
    print(a,b,c,d,e,f)
    print(type(a))
    sensorvalue = [a.value, b.value, c.value, d.value, e.value, f.value ]
start_time = time.time()
sensor()
end_time = time.time()
print("%s s"%(end_time - start_time))
