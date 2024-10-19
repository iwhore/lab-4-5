def product_of_sequence(r, N):
    # Перевіряємо, що r не дорівнює 1, якщо дорівнює одиниці виводимо повідомлення
    if r == 1:
        return "Помилка: r не повинно дорівнювати 1"
    
    product = 1  # Ініціалізація змінної для добутку
    for i in range(N):
        product *= r  # Множимо на кожен наступний елемент
    
    return product

r = float(input("Введіть значення r: "))
N = int(input("Введіть кількість членів послідовності N: "))

result = product_of_sequence(r, N)
print(f"Добуток перших {N} членів послідовності: {result}")
