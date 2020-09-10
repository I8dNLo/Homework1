"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string_first, string_second):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not (isinstance(string_first, str) and isinstance(string_second, str)):
        return 0
    elif string_first == string_second:
        return 1
    elif len(string_first) > len(string_second):
        return 2
    elif string_second == 'learn':
        return 3
    else:
        return 'Непредвиденное условие'

print(main(1, 'Привет'))
print(main('Привет', 'Привет'))
print(main('Привет бобёр', 'Привет'))
print(main('Хай', 'learn'))
    
#if __name__ == "__main__":
#    main()
