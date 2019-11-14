import math


def f_vector(y, t):
    F = [0, 0]
    a = 2
    k = 0.25
    F[0] = y[1] - (a * y[0] + k * y[1]) * y[0]
    F[1] = math.exp(y[0]) - (y[0] + a * y[1]) * y[0]
    return F


def euler_explicit(U0, T, E_add, tau_max, n):
    # file = open('explicit.txt', 'w')
    file1 = open('1.txt', 'w')
    file2 = open('2.txt', 'w')
    t_k = 0
    y_k = U0
    while t_k < T:
        F = f_vector(y_k, t_k)
        tau_k = E_add[0] / (math.fabs(F[0]) + E_add[0] / tau_max)
        for j in range(1, n):
            temp = E_add[j] / (math.fabs(F[j]) + E_add[j] / tau_max)
            tau_k = min(tau_k, temp)
        for j in range(n):
            y_k[j] = y_k[j] + tau_k * F[j]
        t_k = t_k + tau_k
        # file.write(str(t_k))
        # for j in range(n):
        #     file.write("\t" + str(y_k[j]))
        # file.write('\n')
        file1.write(str(t_k))
        file2.write(str(t_k))
        file1.write("\t" + str(y_k[0]))
        file2.write("\t" + str(y_k[1]))
        file1.write('\n')
        file2.write('\n')
    return
