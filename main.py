import random

def choose_difficulty():  ##Выбор уровня сложности игры
    print("Выберите уровень сложности:")
    print("1. Папочка, а можно поиграть? (10 попыток)")
    print("2. Не любитель азартных игр. (7 попыток)")
    print("3. Let's go gambling! (5 попыток)")

    while True:
        choice = input("Введите номер уровня сложности: ")

        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Не верно, попробуйте снова.")
            
def get_boundaries(): ##Получение нижней и верхней границы диапазона от пользователя
    while True:
        try:
            lower_bound = int(input("Введите нижнюю границу диапазона: "))
            upper_bound = int(input("Введите верхнюю границу диапазона: "))
            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                print("Нижняя граница должна быть меньше верхней!")
        except ValueError:
            print("Пожалуйста, введите целое число.")

def get_guess(lower_bound, upper_bound): ##Получение предположения от пользователя с проверкой диапазона
    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(f"Пожалуйста, введите число в диапазоне от {lower_bound} до {upper_bound}.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

def guess_the_number(): ##Основная функция игры 'Угадай число'
    print("Добро пожаловать в игру 'Угадай число'!")

    lower_bound, upper_bound = get_boundaries()  # Получаем границы диапазона

    number_to_guess = random.randint(lower_bound, upper_bound) # Генерируем число для угадывания

    attempts = choose_difficulty()     # Выбираем уровень сложности и количество попыток
    attempts_left = attempts

    print(f"Я загадал число от {lower_bound} до {upper_bound}. У вас {attempts} попыток, чтобы угадать его.")

    while attempts_left > 0:     # Основной игровой цикл
        guess = get_guess(lower_bound, upper_bound)

        if guess < number_to_guess:
            print("Попробуйте число больше!")
        elif guess > number_to_guess:
            print("Попробуйте число меньше!")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts - attempts_left + 1} попыток.")
            break

        attempts_left -= 1
        if attempts_left == 0:
            print(f"Увы, вы исчерпали все попытки. Загаданное число было {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
