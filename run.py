import ctypes


class SHTC3:
    def __init__(self):
        self.dll = ctypes.CDLL("./SHTC3.so")
        init = self.dll.init
        init.restype = ctypes.c_int
        init.argtypes = [ctypes.c_void_p]
        init(None)

    def get_temperature(self):
        temperature = self.dll.get_temperature
        temperature.restype = ctypes.c_float
        temperature.argtypes = [ctypes.c_void_p]
        return temperature(None)

    def get_humidity(self):
        humidity = self.dll.get_humidity
        humidity.restype = ctypes.c_float
        humidity.argtypes = [ctypes.c_void_p]
        return humidity(None)


if __name__ == "__main__":
    SHTC3 = SHTC3()
    while True:
        print('Temperature = %6.2f°C , Humidity = %6.2f%%' % (SHTC3.get_temperature(), SHTC3.get_humidity()))
