def main():
    print("Привет, мир!")


if __name__ == "__main__":
    main()

    def get_numbers():
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return a, b

    def main():
        print("Простой калькулятор")
        a, b = get_numbers()
        print(f"Вы ввели: {a} и {b}")

    if __name__ == "__main__":
        main()

        def add(a, b):
            return a + b

        def main():
            print("Простой калькулятор")
            a, b = get_numbers()
            result = add(a, b)
            print(f"Сумма: {result}")
