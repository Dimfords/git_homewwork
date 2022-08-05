""" Тема: Сортировка и поиск. Часть 1
Задание 1
Необходимо отсортировать первые две трети списка
в порядке возрастания, если среднее арифметическое
всех элементов больше нуля; иначе — лишь первую треть.
Остальную часть списка не сортировать, а расположить
в обратном порядке. """

# import random

# arr = [random.randint(-20, 20) for _ in range(10)]

# # arr = [19, 17, 21, -6, 8, 13, 6, -18, -8, -19] # aver = 3.1 for test
# # arr = [-1, -18, -16, -1, -14, 5, -1, -13, -6, -5] # aver = -7.0 for test

# def sorting_list(arr):
#     print(arr)
#     aver_arr = sum(arr)/len(arr)

#     if aver_arr > 0:
#         n = len(arr) * 2 // 3
#         print('2/3 SORTING')
#     else: 
#         n = len(arr) // 3 
#         print('1/3 SORTING')

#     for i in range(1,n):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break

#     middle_rest_list = (len(arr) - n) // 2 + n
#     c = 1
#     while n < middle_rest_list:
#         arr[len(arr)- c], arr[n] = arr[n], arr[len(arr)- c]
#         n += 1
#         c += 1
#     print(arr)

# sorting_list(arr)

""" Задание 2
Написать программу «успеваемость». Пользователь
вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
меню для пользователя:
■ Вывод оценок (вывод содержимого списка);
■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
■ Выходит ли стипендия (стипендия выходит, если
средний бал не ниже 10.7);
■ Вывод отсортированного списка оценок: по возрастанию или убыванию. """

# def marks():
#     с = 0
#     l = []
#     while с < 10:
#         mark = int(input("Введите оценку от 1 до 12 ->"))
#         if mark >= 1 and mark <= 12:
#             l.append(mark)
#             с += 1
#         else:
#             print("Неправильный ввод. Повторите")
#     return l

# def marks_list(arr):
#     print("\nСписок оценок студента:", end=" ")
#     for i in arr:
#         print(i, end=", ")

# def peresdacha(arr):
#     while True:
#         num = int(input("Введите номер элемента списка от нуля: "))
#         new_mark = int(input("Введите новую оценку: "))
#         if num >= 0 and num < len(arr) and new_mark >= 1 and new_mark <=12:
#             arr[num] = new_mark
#             print("\nОценки после пересдачи", end="")
#             marks_list(arr)
#             return arr
#         else: print("Ошибка ввода! Повторите ввод  номера элемента списка и оценки.")

# def stipendia(arr):
#     aver_bal = sum(arr) / len(arr)
#     if aver_bal >= 10.7:
#         print(f"Ваш средний бал: {aver_bal}, поздравляем у Вас будет стипендия!")
#     else:
#         print(f"Ваш средний бал: {aver_bal}, к сожалению стипендии не будет.")

# def sort_marks_ascending(arr):
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break

# def sort_marks_descending(arr):
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] > arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break

# def menu():
#     print("\n \n Выберите пункт меню:\n \
#     1.Вывод оценок\n\
#     2. Пересдача экзамена\n\
#     3. Начислят ли стипендию? \n\
#     4.Вывод оценок по возрастанию \n\
#     5. Вывод оценок по убыванию \n\
#     6. Выход из программы\n\
#     ")

# def main_prog():
#     arr = marks()
#     menu()
#     while True:
#         user_choice = int(input('-> '))
#         if user_choice == 1:
#             marks_list(arr)
#             menu()
#         elif user_choice == 2:
#             peresdacha(arr)
#             menu()
#         elif user_choice == 3:
#             stipendia(arr)
#             menu()
#         elif user_choice == 4:
#             sort_marks_ascending(arr)
#             marks_list(arr)
#             menu()
#         elif user_choice == 5:
#             sort_marks_descending(arr)
#             marks_list(arr)
#             menu()
#         elif user_choice == 6:
#             return
#         else: print("Неправильный ввод. Повторите!")

# main_prog()

""" Задание 3
Написать программу, реализующую сортировку списка
методом усовершенствованной сортировки пузырьковым
методом. Усовершенствование состоит в том, чтобы анализировать количество 
перестановок на каждом шагу, если
это количество равно нулю, то продолжать сортировку
нет смысла — список отсортирован. """

import random

arr = [random.randint(-20, 20) for _ in range(10)]
def bubble_sort(arr):
    for i in range(len(arr)):
        c = 0
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                c += 1
        if c == 0:
            break
    return arr

print(arr)
print(bubble_sort(arr))