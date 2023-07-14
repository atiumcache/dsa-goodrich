import sys
data = []
lastSize = 0;
for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    if ((b > lastSize) & (a > 0)):
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format((a - 1),(lastSize)))
    lastSize = b
    data.append(None)
for i in range(100):
    data.pop()
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))