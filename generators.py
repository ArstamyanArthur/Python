# the idea behind generators is to save memory doing one thing at a time
'''
# comp might not be able to store this much memory 
x = [i**2 for i in range(10000000000)]
for el in x:
    print(el)
# so one way to avoid storing is this and generators are being used in similar way
for i in range(100000):
    print(i**2)
'''
#                                            generator class
'''
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        if self.last == self.n:
            raise StopIteration
        rv = self.last**2
        self.last += 1
        return rv


g = Gen(100)
while True:
    print(next(g))
'''
#                                               yield
def gen(n):
    for i in range(n):
        yield i**2

g = gen(10000)
# for el in g:
#     print(el)
print(type(g), g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#                             comparing  memory usage between using generator and list
import sys
x = [i**2 for i in range(100000)]
g = gen(100000)
print(sys.getsizeof(x))
print(sys.getsizeof(g))
