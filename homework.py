import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

# сгенерируем данные по оценкам:
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

# выводим получившийся словарь с оценками:
for student in students:
    print(f'{student}\n{students_marks[student]}')

print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить оценку ученика по предмету
5. Редактировать оценку ученика по предмету
6. Вывести информацию по всем оценкам для определенного ученика
7. Вывести средний балл по каждому предмету для определенного ученика
8. Выход из программы
''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку для удаления: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            try:
                students_marks[student][class_].remove(mark)
                print(f'Оценка {mark} для {student} по предмету {class_} удалена')
            except ValueError:
                print('ОШИБКА: указанная оценка не найдена')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 5:
        print('5. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        old_mark = int(input('Введите оценку для редактирования: '))
        new_mark = int(input('Введите новую оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            try:
                index = students_marks[student][class_].index(old_mark)
                students_marks[student][class_][index] = new_mark
                print(f'Оценка для {student} по предмету {class_} изменена с {old_mark} на {new_mark}')
            except ValueError:
                print('ОШИБКА: указанная оценка не найдена')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 6:
        print('6. Вывести информацию по всем оценкам для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Оценки для {student}:')
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 7:
        print('7. Вывести средний балл по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Средний балл для {student}:')
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 8:
        print('8. Выход из программы')
        break



