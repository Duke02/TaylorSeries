import sympy as sym
import numpy as num
import matplotlib.pyplot as pyplot

pyplot.style.use("ggplot")

x = sym.Symbol('x')
eToX = sym.functions.exp(x)
sinFunct = sym.functions.sin(x)
f = eToX


def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial(number-1)


def taylor(function, a, n):
    i = 0
    poly = 0
    while i <= n:
        poly = poly + (function.diff(x,i).subs(x, a))/(factorial(i))*(x - a)**i
        i += 1
    return poly

def plot():
    xLimits = [-5, 5]
    x1 = num.linspace(xLimits[0], xLimits[1], 800)
    y1 = []

    maxErr = float(input("What is the max error?"))
    a = 0
    j = 1
    overMaxErr = True

    while overMaxErr:
        funct = taylor(f, a, j)
        print("Taylor expansion at n = " + str(j), funct)
        for k in x1:
            y1.append(funct.subs(x, k))
            if abs(f.subs(x, k) - funct.subs(x, k)) < maxErr and abs(f.subs(x, -k) - funct.subs(x, -k)) < maxErr:
                overMaxErr = False
            else:
                overMaxErr = True
        if j % 4 == 1 or not overMaxErr:
            pyplot.plot(x1, y1, label='order' + str(j))
        y1 = []
        j += 1
    if f is eToX:
        pyplot.plot(x1, num.exp(x1), label="e to the x")
    elif f is sinFunct:
        pyplot.plot(x1, num.sin(x1), label="sin of x")
    pyplot.xlim(xLimits)
    pyplot.ylim([-5, 5])
    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.legend()
    pyplot.grid(True)
    pyplot.title("Taylor series approx")
    pyplot.show()

