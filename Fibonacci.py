def fibonacci(n):
    sequencia = [0, 1]
    
    while sequencia[-1] < n:
        prox_fib = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_fib)
    
    return sequencia

def verificar_fibonacci(n):
    sequencia = fibonacci(n)
    
    if n in sequencia:
        return f'O número {n} pertence à sequência de Fibonacci!'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci.'

numero = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))

resultado = verificar_fibonacci(numero)

print(resultado)
