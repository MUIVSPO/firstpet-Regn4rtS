import random

def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1. Папочка, а можно поиграть? (10 попыток)")
    print("2. Не любитель азартных игр. (7 попыток)")
    print("3. Let's go gambling! (5 попыток)")
    choice = input("Введите номер уровня сложности: ")
    if choice == '1':
        return 10
    elif choice == '2':
        return 7
    elif choice == '3':
        return 5
    else:
        print("Неверный выбор, будет установлен уровень 'Папочка, а можно пиогрить?', Папочка разрешил.")
        return 10

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    lower_bound = int(input("Введите нижнюю границу диапазона: "))
    upper_bound = int(input("Введите верхнюю границу диапазона: "))
    
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = choose_difficulty()
    attempts_left = attempts

    print(f"Я загадал число от {lower_bound} до {upper_bound}. У вас {attempts} попыток, чтобы угадать его.")

    while attempts_left > 0:
        guess = int(input("Введите ваше предположение: "))
        if guess < lower_bound or guess > upper_bound:
            print(f"Пожалуйста, введите число в диапазоне от {lower_bound} до {upper_bound}.")
            continue

        if guess < number_to_guess:
            print("Больше!")
        elif guess > number_to_guess:
            print("Меньше!")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts - attempts_left + 1} попыток.")
            break

        attempts_left -= 1
        if attempts_left == 0:
            print(f"Вы исчерпали все попытки. Загаданное число было {number_to_guess}.")

if __name__=="__main__":
    guess_the_number()
