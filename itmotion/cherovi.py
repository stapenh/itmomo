
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


def print_n_numbers(n):
    if n == 1:
        print(1)
    else:
        print(n)
        return print_n_numbers(n-1)

def print_fromA2B(a, b):
    if b == a:
        print(b)
        return
    else:
        print(a)
        print_fromA2B(a+1, b)


def power_of_2(a):
    if a % 2 == 1:
        print('no')
        return
    elif a == 2:
        print('ye')
        return
    power_of_2(a // 2)



def count_of_numbers(n):
    if n // 10 == 0:
        return n
    else:
        return count_of_numbers(n // 10) + n % 10



def is_prime(n, i):

    if i**2 > n:
        print("ye")
        return 0
    else:
        if n % i == 0:
            print('no')
            return 0
        else:
            is_prime(n,i + 1)



def is_polindromm(s):







