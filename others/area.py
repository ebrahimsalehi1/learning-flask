
from argon2 import Type


def area(r):
    # if r<=0:
    #     raise ValueError("the value must not be negative")

    # if type(r) not in (int,float):
    #     raise TypeError('Type must be number')

    try:
        if r<0:
            return -1
            
        return r**2
    except:
        return -1

print(area(-33))    