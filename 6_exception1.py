"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            user_say = input('Задай свой вопрос: ')
            if user_say in dictionary_ask:
                print(dictionary_ask[user_say])
                break
            else:
                print('Нужен другой вопрос!')
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    ask_user()
