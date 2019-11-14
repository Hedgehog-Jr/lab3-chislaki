from gauss import gauss


def jcount(f, x, M):
    J = [[0] * len(x) for i in range(len(x))]
    dx = [0] * len(x)
    for i in range(len(x)):
        dx[i] = x[i] * M
    for i in range(len(x)):
        for j in range(len(x)):
            fx = f[i](x)
            x[j] += dx[j]
            J[i][j] = (f[i](x) - fx) / dx[j]
            x[j] -= dx[j]
    return J


def newton(f, x, NIT, E1, E2, M):
    print('{:>5}'.format("k"), '{:>15}'.format("d1"), '{:>15}'.format("d2"))
    F = [0] * len(x)
    k = 1
    while k <= NIT:
        for i in range(len(x)):
            F[i] = -f[i](x)
        J = jcount(f, x, M)
        dx = gauss(J, F, len(x))
        x_k = [0] * len(x)
        for i in range(len(x)):
            x_k[i] = x[i] + dx[i]
        d1 = abs(f[0](x))
        for i in range(1, len(x)):
            d1 = max(d1, abs(f[i](x)))
        if x_k[0] < 1:
            d2 = abs(x_k[0] - x[0])
        else:
            d2 = abs((x_k[0] - x[0]) / x_k[0])
        for i in range(1, len(x)):
            if x_k[i] < 1:
                d2 = max(abs(x_k[i] - x[i]), d2)
            else:
                d2 = max(abs((x_k[i] - x[i]) / x_k[i]), d2)
        x = x_k
        print('{:>5}'.format(k), '{:>15}'.format(format(d1, '.9f')), '{:>15}'.format(format(d2, '.9f')))
        if d1 <= E1 and d2 <= E2:
            break
        if k == NIT:
            exit("IER = 2")
        k += 1
    print("\n")
    return x
