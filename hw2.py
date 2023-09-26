# Выбрана процедурная парадигма, чтобы была возможность переиспользовать данный код.

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print('')


def main():
    n = int(input("Введите число: "))
    multiplication_table(n)


if __name__ == "__main__":
    main()
