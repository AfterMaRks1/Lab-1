def get_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def main():
    while True:
        print("\n=== Простой калькулятор ===")
        a, b = get_numbers()
        print(f"{a} + {b} = {add(a, b)}")
        print(f"{a} - {b} = {subtract(a, b)}")
        print(f"{a} * {b} = {multiply(a, b)}")
        print(f"{a} / {b} = {divide(a, b)}")
        again = input("Продолжить? (д/н): ").lower()
        if again != "д":
            break
    print("До свидания!")


if __name__ == "__main__":
    main()
