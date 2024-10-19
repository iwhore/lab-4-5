import math

def factorial_approximation(n):
    # Використовуємо формулу наближення факторіалу
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

def compute_pi(epsilon):
    n = 1  # Початкове значення n
    previous_pi = 0  # Початкове значення для попереднього обчисленого значення
    current_pi = factorial_approximation(n)  # Обчислюємо перше значення
    
    # Продовжуємо обчислення, поки різниця не стане меншою за epsilon
    while abs(current_pi - previous_pi) >= epsilon:
        n += 1
        previous_pi = current_pi
        current_pi = factorial_approximation(n)
    0
    return n

epsilon = float(input("Введіть точність ε: "))
terms_needed = compute_pi(epsilon)
print(f"Необхідна кількість членів ряду: {terms_needed}")
