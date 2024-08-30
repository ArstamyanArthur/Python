class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'

    def __mul__(self, other):
        if type(other) is not int:
            raise Exception('Invalid argument, must be int')
        self.name = other*self.name


def add_attribute(self):
    self.z = 9


x = type('Test', (Person, ), {'x': 5, 'add_attribute': add_attribute})
p1 = x('Arthur')
p2 = x('Anna')
p2*2
p1.y = 9
p1.add_attribute()
print(p1, p1.x, p1.y, p1.z)
print(p2, p2.x)


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        # making attrs UPPERCASE
        a = {}
        for key, val in attrs.items():
            if key.startswith('_'):
                a[key] = val
            else:
                a[key.upper()] = val
        print(a)
        
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    age = 1
    kids = 5

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Dog({self.name})'


dog_1 = Dog('Jack')
print(dog_1)
print(type(dog_1))
print(type(type(dog_1)))
