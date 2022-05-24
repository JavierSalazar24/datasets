import matplotlib.pyplot as plt


def f(x, y):
    return x/y


def runge_kutta(x, y, n, h):

    print('\n--------SOLUCIÓN--------')
    print('')
    print('x(n)\ty(n)\ty(n+1)')
    print('-------------------------')
    ejex = [x]
    ejey = [y]
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + k1 * h/2)
        k3 = f(x + h/2, y + k2 * h/2)
        k4 = f(x + h, y + k3 * h)
        yi = y+1/6*(k1+2*k2+2*k3+k4)*h
        print('%.4f\t%.4f\t%.4f' % (x, y, yi))
        print('-------------------------')
        y = yi
        x = x+h

        ejex.append(x)
        ejey.append(y)

    plt.plot(ejex, ejey)
    plt.scatter(ejex, ejey)
    plt.title('Runge-Kutta')
    plt.show()

# Inputs
# print('Enter initial conditions:')
# x = float(input('x0 = '))
# y = float(input('y0 = '))

# print('Enter number of steps:')
# n = int(input('Number of steps = '))


# RK4 method call
runge_kutta(1, 3, 4, 0.1)
