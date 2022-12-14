import matplotlib.pyplot as plt


def newton_divided_diff(x, y):
    n = len(x)
 
    f = [[0 for i in range(n)] for j in range(n)]
 
    for dim in range(n):
       f[dim][0] = y[dim]
 
    arguments = [i for i in range(1000, 3001, 50)]
    values = []
 
    for argument in arguments:
       for i in range(1, n):
           for j in range(n - i):
               f[j][i] = ((f[j][i - 1] - f[j + 1][i - 1]) /
                          (x[j] - x[i + j]))
 
       sum = f[0][0]
 
       for i in range(1, n):
           mulipl = 1
           for j in range(i):
               mulipl = mulipl * (argument - x[j])
           sum = sum + (mulipl * f[0][i])
       values.append(sum)
 
    return arguments, values
 
 
x = [1800, 1850, 1900, 2000]
y = [280, 283, 291, 370]
 
plt.plot(newton_divided_diff(x, y)[0], newton_divided_diff(x, y)[1])
plt.show()
