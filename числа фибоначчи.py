def sum_even_fibonacci(limit):
    total = 0
    a, b = 3, 4
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

limit = 7000000
result = sum_even_fibonacci(limit)

print(f"Сумма четных членов последовательности Фибоначчи, не превышающих 7 миллионов: {result}")