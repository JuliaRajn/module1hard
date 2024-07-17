grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = {}

# Сортируем список имен по алфавиту
students_sorted = sorted(students)

for student in students_sorted:
    # Находим индекс студента в списке имен
    index = students_sorted.index(student)
    # Вычисляем средний балл по индексу
    average_grades[student] = sum(grades[index]) / len(grades[index])

print(average_grades)
