# Игра Угадай число

## Описание
Этот проект - это код, что выбирает числа в случайном порядке, делая из этого мини игру. Игрок (пользователь) должен угадать число за определённое кол-во попыток.

## Установка и запуск
1. Убедитесь, что у вас установлен Python:
   откройте терминал (PowerShell - Windows, Terminal - Linux/macOS), введите команду python -- version или python3 -- version и нажмите Enter. Если Python установлен, вы увидите его версию, в противном случае его необходимо скачать с официального сайта.
2. Копируйте код в любой текстовый редактор и сохраните файл с разширением ".py", нарпимер: main.py.
3. В терминале перейдите в дерикторию с файлом (Например: cd/путь/к/вашей/папке), используйте фактический путь к папке.
4. Введите код запуска файла, например: python guess_the_number.py или python3 guess_the_number.py . Нажмите Enter.
5. После запуска, следуйте инструкциям в терминале.



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
