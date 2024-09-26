# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

def fibonacci(n):
    fibonacci = [0,1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)
    return fibonacci

def pertence(n):
    sequencia = fibonacci(n)
    if n in sequencia:
        print(f"{n} pertence a sequencia de Fibonacci.")
    else:
        print(f"{n} NÃO pertence a sequencia de Fibonacci.")

n = int(input("Digite um valor para N: "))
pertence(n)