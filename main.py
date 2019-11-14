from Euler import euler_explicit
from Newton import newton
from functions import f1, f2


def main():
    euler_explicit(U0=[1, 0], T=1, E_add=[1e-3, 1e-3], tau_max=1, n=2)


main()
