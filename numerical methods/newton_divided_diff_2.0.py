import matplotlib.pyplot as plt
def newton_divided_diff(x, y, argument):
    n = len(x)
    f = [[0 for i in range(n)] for j in range(n)]
    for dim in range(n):
       f[dim][0] = y[dim]
    values = []
    for i in range(1, n):
       for j in range(n - i):
           f[j][i] = ((f[j][i - 1] - f[j + 1][i - 1]) /
                      (x[j] - x[i + j]))
    sum= f[0][0]
    for i in range(1, n):
       mulipl = 1
       for j in range(i):
           mulipl = mulipl * (argument - x[j])
       sum = sum + (mulipl * f[0][i])
    values.append(sum)
    return values
x = [1970, 1990]
y = [3707475887, 5281653820]
print(newton_divided_diff(x, y, 1980))
x = [1960, 1970, 1990]
y = [3039585530, 3707475887, 5281653820]
print(newton_divided_diff(x, y, 1980))
x = [1960, 1970, 1990, 2000]
y = [3039585530, 3707475887, 5281653820, 6079603571]
print(newton_divided_diff(x, y, 2106))
