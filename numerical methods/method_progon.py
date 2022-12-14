import matplotlib.pyplot as plt


def method_progon(n, a, b, c, r):
    for i in range(1, n):
        s = c[i] / a[i - 1]
        a[i] = a[i] - s * b[i - 1]
        r[i] = r[i] - s * r[i - 1]

    x = [0] * n
    x[n - 1] = r[n - 1] / a[n - 1]
    for j in range(n - 1):
        i = n - 2 - j
        x[i] = (r[i] - b[i] * x[i + 1]) / a[i]
    return x


print('1st Task')
n = 4
a = [2, 10, -5, 4]
b = [1, -5, 2]
c = [0, 1, 1, 1]
r = [-5, -18, -40, -27]
print(method_progon(n, a, b, c, r))

print('2nd Task')
for n in [5, 10, 50]:
    print('for n =', n)
    a = [2] * n
    b = [-1] * n
    c = [-1] * n
    r = [1] * n
    arr = method_progon(n, a, b, c, r)
    print(arr)
    plt.plot(arr)
    plt.show()