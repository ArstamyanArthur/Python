def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        total = time.time() - start
        print('Total: ', total)
        return rv
    return wrapper


def distance(point1, point2):
    time.sleep(2)
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5


print(distance([1, 2], [4, 6]))
distance = timer(distance)
print(distance([1, 2], [4, 6]))


@timer  # does same as distance = timer(distance) so this is what decorator does - adds some lines of code to existing function
def distance(point1, point2):
    time.sleep(2)
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5


print(distance([1, 2], [4, 6]))
