"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_marks =[
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '5a', 'scores': [3, 5, 5, 3, 4]},
    {'school_class': '6a', 'scores': [4, 4, 5, 5, 3]},
    {'school_class': '7a', 'scores': [5, 5, 5, 5, 5]},
    {'school_class': '8a', 'scores': [4, 4, 4, 4, 4]},
    {'school_class': '9a', 'scores': [3, 5, 4, 5, 2]},
    {'school_class': '10a', 'scores': [5, 5, 4, 4,5]},
    {'school_class': '11a', 'scores': [4, 5, 2, 2, 5]},
    ]


def main(school_marks):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    student_sum_scores = 0 #Будущий средний балл по школе
    student_count = 0  #Будущее общее количество оценок во всей школе
    for school_class in school_marks:  # Перебираем словари из списка
        class_sum_mark = sum(score in school_class['scores']) 
        class_size = len(score in school_class['scores']) 
        print(f"Средний балл класса {school_class['school_class']}: {class_sum_mark / class_size}")
        student_count += class_size
        student_sum_scores += class_sum_mark
    print(f'Средний балл по школе: {student_sum_scores/ student_count}')

main(school_marks)
    
#if __name__ == "__main__":
 #   main()
