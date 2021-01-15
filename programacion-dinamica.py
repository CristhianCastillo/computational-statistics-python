import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_memoization(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError as identifier:
        resultado = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        memo[n] = resultado
        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    n = int(input("Escoje un numero: "))
    resultado = fibonacci_memoization(n)
    print(f'El resultado es: {resultado}')