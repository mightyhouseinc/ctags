global01 = 1

def func01():
    local01 = 1

def func02():
    local02 = 2
    local03 = 3

def func03(x):
    return lambda x:x

def func04(x):
    def localfunc01():
        return x
    return localfunc01

class Cls01:
    member01 = 1
    def method01(self):
        local04 = 4
    member02 = 2
