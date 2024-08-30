# 1-st way the problem is if some error happens file wont be closed
file = open('file.txt', 'w')
file.write('hello_1')
file.close()
# 2-nd way in which file will be closed no matter errors happen or not
file = open('file.txt', 'w')
try:
    file.write('hello_2')
finally:
    file.close()
# 3-rd way equivalent to 2-nd way with WITH context manager
with open('file.txt', 'w') as file:
    print('hi')
    file.write('hello_3')
#                                       class Context Manager
class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)
    def __enter__(self):
        print('Enter')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{exc_type}, {exc_val}, {exc_tb}')
        print('Exit')
        self.file.close()
        if exc_type == Exception:
            return True

with File('file.txt', 'w') as f:
    print('middle_1')
    f.write('hello!')
    print('middle_2')
    raise Exception()
#                                   from contextlib import contextmanager
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print('Enter')
    fl = open(filename, method)
    try:
        yield fl
    finally:
        fl.close()
        print('Exit')

with file('file.txt', 'w') as f:
    print('Middle')
    f.write('hello!!')
    raise Exception()
