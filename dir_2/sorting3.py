""" Тема: Сортировка и поиск. Часть 3
Задание 1
Есть четыре списка целых. Необходимо их объединить
в пятом списке. Полученный результат в зависимости от
выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием линейного поиска. """


# l_1 = [1, 3, 5, 12, -5, -3, 2, 4, 20, 16, 19]
# l_2 = [21, 19, 3, 5 , 1, 0, 3, -6, -1, 21, 17]
# l_3 = [30, 60, 70, 80, -20, 10, 30, 50, 90, 11]
# l_4 = [12, 15, 17, 18, 65, -5, -1, 0, 16, 7, 9]

# def arr_append(arr1, arr2, arr3, arr4):
#     arr_sum = arr1 + arr2 + arr3 + arr4
#     print ("\nОбъединенный 5й список:\n", arr_sum)
#     return arr_sum

# def ascending_sorting(arr): #shell sorting
#     size = len(arr)
#     step = size // 2

#     while step > 0:
#         for i in range(step, size):
#             delta = i - step
#             while delta >= 0 and arr[delta] > arr[i]:
#                 arr[delta], arr[i] = arr[i], arr[delta]
#                 i = delta
#                 delta = i - step
#         step //= 2
#     print(arr)
#     return arr 

# def descending_sorting(arr): #shell sorting
#     size = len(arr)
#     step = size // 2

#     while step > 0:
#         for i in range(step, size):
#             delta = i - step
#             while delta >= 0 and arr[delta] < arr[i]:
#                 arr[delta], arr[i] = arr[i], arr[delta]
#                 i = delta
#                 delta = i - step
#         step //= 2
#     print(arr)
#     return arr 

# def linear_search(arr, key):
#     c = 0
#     for i in range(len(arr)):
#         if arr[i] == key:
#             print(f"Позиция искомого элемента {i}")
#             c +=1
#             return
#     if c == 0:
#         print("Элемент отсутвует в списке!")

# def menu():
#     print("\n \n Выберите пункт меню:\n\
#     1. Отсортировать по возрастанию\n\
#     2. Отсортировать по убыванию \n\
#     3. Найти элемент в массиве \n\
#     4. Выход из программы\n\
#     ")


# def main_prog(arr1, arr2, arr3, arr4):
#     summ_arr = arr_append(arr1, arr2, arr3, arr4)
#     menu()
#     while True:
#         user_choice = int(input('-> '))
#         if user_choice == 1:
#             summ_arr = ascending_sorting(summ_arr)
#             menu()
#         elif user_choice == 2:
#             summ_arr = descending_sorting(summ_arr)
#             menu()
#         elif user_choice == 3:
#             key = int(input('Введите элемент для поиска -> '))
#             linear_search(summ_arr, key)
#             menu()
#         elif user_choice == 4:
#             return
#         else: print("Неправильный ввод. Повторите!")

# main_prog(l_1, l_2, l_3, l_4)


""" Задание 2
Есть четыре списка целых. Необходимо объединить
в пятом списке только те элементы, которые уникальны
для каждого списка. Полученный результат в зависимости
от выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием бинарного поиска. """


# l_1 = [1, 3, 5, 12, -5, -3, 5, 4, 5, 16, 19]
# l_2 = [21, 19, 3, 5 , 1, 0, 19, -6, -1, 19, 17]
# l_3 = [30, 60, 70, 80, -20, 10, 30, 50, 60, 11]
# l_4 = [12, 15, 15, 18, 65, -5, -1, 0, 15, 7, 9]

# def arr_append(arr1, arr2, arr3, arr4):
#     arr_unic1 = []
#     for i in arr1:
#         if i not in arr_unic1:
#             arr_unic1.append(i)
#     arr_unic2 = []
#     for i in arr2:
#         if i not in arr_unic2:
#             arr_unic2.append(i)
#     arr_unic3 = []
#     for i in arr3:
#         if i not in arr_unic3:
#             arr_unic3.append(i)
#     arr_unic4 = []
#     for i in arr4:
#         if i not in arr_unic4:
#             arr_unic4.append(i)
    
#     summ_arr = arr_unic1 + arr_unic2 + arr_unic3 + arr_unic4
#     print ("\nОбъединенный 5й список:\n", summ_arr)
#     return summ_arr

# def ascending_sorting(arr): #shell sorting
#     size = len(arr)
#     step = size // 2

#     while step > 0:
#         for i in range(step, size):
#             delta = i - step
#             while delta >= 0 and arr[delta] > arr[i]:
#                 arr[delta], arr[i] = arr[i], arr[delta]
#                 i = delta
#                 delta = i - step
#         step //= 2
#     print(arr)
#     return arr 

# def descending_sorting(arr): #shell sorting
#     size = len(arr)
#     step = size // 2

#     while step > 0:
#         for i in range(step, size):
#             delta = i - step
#             while delta >= 0 and arr[delta] < arr[i]:
#                 arr[delta], arr[i] = arr[i], arr[delta]
#                 i = delta
#                 delta = i - step
#         step //= 2
#     print(arr)
#     return arr 

# def binar_search(arr, key):
#     # проверка сортировки по возрастанию списка
#     c = 0
#     for i in range(len(arr)-1):
#         if arr[i+1] >= arr[i]:
#             c += 1
#     if c == len(arr)-1:
#         low = 0
#         high = len(arr)-1
#         while low <= high:
#                 mid = low + (high - low)//2
#                 if arr[mid] == key:
#                     print(f"Позиция искомого элемента {mid}")
#                     return 
#                 elif arr[mid] < key:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#         print("Элемент отсутвует в списке!")
#         return

# # проверка сортировки по убыванию списка
#     c = 0
#     for i in range(len(arr)-1):
#         if arr[i+1] <= arr[i]:
#             c += 1
#     if c == len(arr)-1:
#         low = 0
#         high = len(arr)-1
#         while low <= high:
#                 mid = low + (high - low)//2
#                 if arr[mid] == key:
#                     print(f"Позиция искомого элемента {mid}")
#                     return 
#                 elif arr[mid] > key:
#                     low = mid + 1
#                 else:

#                     high = mid - 1
#         print("Элемент отсутвует в списке!")
#         return
# # выйти, если список не отсортирован
#     if c != len(arr)-1:
#         print("Список не отсортирован бинарный поиск не возможен, сначала отсортируйте!")
#         return
        
# def menu():
#     print("\n \n Выберите пункт меню:\n\
#     1. Отсортировать по возрастанию\n\
#     2. Отсортировать по убыванию \n\
#     3. Найти элемент в массиве \n\
#     4. Выход из программы\n\
#     ")


# def main_prog(arr1, arr2, arr3, arr4):
#     summ_arr = arr_append(arr1, arr2, arr3, arr4)
#     menu()
#     while True:
#         user_choice = int(input('-> '))
#         if user_choice == 1:
#             summ_arr = ascending_sorting(summ_arr)
#             menu()
#         elif user_choice == 2:
#             summ_arr = descending_sorting(summ_arr)
#             menu()
#         elif user_choice == 3:
#             key = int(input('Введите элемент для поиска -> '))
#             binar_search(summ_arr, key)
#             menu()
#         elif user_choice == 4:
#             return
#         else: print("Неправильный ввод. Повторите!")

# main_prog(l_1, l_2, l_3, l_4)