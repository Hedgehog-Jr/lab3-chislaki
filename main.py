from Euler import euler_explicit


def main():
    euler_explicit(U0=[1, 0], T=1, E_add=[1e-5, 1e-5], tau_max=1, n=2)
    return


main()
