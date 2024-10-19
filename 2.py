def generate_table(N, M):
    # перше будемо проходити по кожному рядку
    for i in range(N):
        # Ініціалізуємо початкове значення для поточного рядка
        start_number = 10 * (i + 1)
        row = []
        
        # Додаємо M елементів до поточного рядка
        for j in range(M):
            row.append(start_number + j)
        
        # Виводимо сформований рядок
        print("\t".join(map(str, row)))

N = int(input("Введіть кількість рядків (N): "))
M = int(input("Введіть кількість стовпців (M): "))

if 2 <= N < 30 and 2 <= M < 30:
    generate_table(N, M)
else:
    print("Помилка: N та M мають бути в діапазоні від 2 до 29.")
