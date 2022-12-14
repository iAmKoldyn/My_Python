import math


def main():
    rot = 1
    vol = 1

    def bisect(fun, a, b, eps):
        fa = fun(a)
        fb = fun(b)
        if fa*fb > 0.:
            print("Bad interval [%f, %f]" % (a,b))
            return 0.
        while (b-a)/2 > eps:
            c = (b+a)/2
            fc = fun(c)
            if fc == 0.: break
            if fa*fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        return (b+a)/2

    """1st task"""
    def w(x): return x ** 3 - 9
    def e(x): return 3 * (x**3) + (x**2) - x - 5
    def r(x): return (math.cos(x)**2) + 6 - x
    print(bisect(w, 2, 3, 10  -6))
    print(bisect(e, 1, 2, 10  -6))
    print(bisect(r, 6, 7, 10  -6))

    """2nd task"""
    def s(x): return 2*x**3 - 6*x -1
    print(bisect(s, -2, -1, 10**(-6)))
    print(bisect(s, -1, 0, 10**(-6)))
    print(bisect(s, 1, 2, 10**(-6)))

    """3rd task"""
    def a(x): return x**3 - 2
    def b(x): return x**3 - 3
    def c(x): return x**3 - 5
    print(bisect(a, 1, 2, 10**(-8)))
    print(bisect(b, 1, 2, 10**(-8)))
    print(bisect(c, 1, 2, 10**(-8)))

    """4th task"""

    def x(h): return math.pi * (h**2) * (rot - h/3) - vol
    print(bisect(x, 0, 1, 10**(-3)))

if __name__ == '__main__':
    main()