""" Тема: Сортировка и поиск. Часть 2
Задание 1
Написать программу «справочник». Создать два списка
целых. Один список хранит идентификационные коды,
второй — телефонные номера. Реализовать меню для
пользователя:
■ Отсортировать по идентификационным кодам;
■ Отсортировать по номерам телефона;
■ Вывести список пользователей с кодами и телефонами;
■ Выход. """

# ind_code = [301, 920, 103, 104, 205, 106, 107, 108, 201, 458]
# tel_numb = ['0975445254', '0981112233', '0939995522', '0636661122', \
#              '0928881177', '0737775566', '0979992277', '0967772233', '0783335677'\
#             , '0567775511']

# def menu():
#     print("\n \n Выберите пункт меню:\n \
#    1. Отсортировать по идентификационным кодам\n\
#     2. Отсортировать по номерам телефона\n\
#     3. Вывести список пользователей с кодами и телефонами \n\
#     4. Выход из программы\n\
#     ")

# def spravo4nik(ind_code, tel_numb):
#     print("\nСправочник: \nинд.код    номер телефона")
#     for i in range(0, len(ind_code)):
#         print(ind_code[i], end=" -       ")
#         print(tel_numb[ind_code.index(ind_code[i])])
#     print()

# def tmp_list_before_sorting(arr):
#     tmp_l = []
#     for i in arr:
#         tmp_l.append(i)
#     return tmp_l

# def sort_ascending_by_ind_code(arr, ind_code, tel_numb):
#     print("1. Отсортировать по идентификационным кодам:")
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break
#     for i in arr:
#         indx = ind_code.index(i)
#         print(i, end=" -       ")
#         print(tel_numb[indx])
        
# def sort_ascending_by_tel_numb(arr, ind_code, tel_numb):
#     print("2. Отсортировать по номерам телефона:")
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break
#     for i in arr:
#         indx = tel_numb.index(i)
#         print(ind_code[indx], end=" -       ")
#         print(i)
        
# def main_prog():
#     menu()
#     while True:
#         user_choice = int(input('-> '))
#         if user_choice == 1:
#             sort_ascending_by_ind_code(tmp_list_before_sorting(ind_code), ind_code, tel_numb)
#             menu()
#         elif user_choice == 2:
#             sort_ascending_by_tel_numb(tmp_list_before_sorting(tel_numb), ind_code, tel_numb)
#             menu()
#         elif user_choice == 3:
#             spravo4nik(ind_code, tel_numb)
#             menu()
#         elif user_choice == 4:
#             return
#         else: print("Неправильный ввод. Повторите!")

# main_prog()



""" Задание 2
Написать программу «книги». Создать два списка
с данными. Один список хранит названия книг, второй —
годы выпуска. Реализовать меню для пользователя:
■ Отсортировать по названию книг;
■ Отсортировать по годам выпуска;
■ Вывести список книг с названиями и годами выпуска;
■ Выход; """

# books_title = ['Унесенные ветром', 'Пикник на обочине', 'Мартин Иден', 
#             'На западном фронте без перемен', 'Старик и море', 'Одиночество в сети', \
#             'Бойцовский клуб', 'Уцелевший', 'Облачный атлас', 'Робинзон Крузо']

# published = [1939, 1971, 1909, 1929, 1952, 2001, 1999, 1999, 2004, 1719]

# def menu():
#     print("\n \n Выберите пункт меню:\n \
#    1. Отсортировать по названию книг\n\
#     2. Отсортировать по годам выпуска\n\
#     3. Вывести список книг с названиями и годами выпуска \n\
#     4. Выход из программы\n\
#     ")

# def spravo4nik(books_title, published):
#     print("\Библиотека: \nНазвание                          Дата публикации")
#     for i in range(0, len(books_title)):
#         print((books_title[i]).ljust(30), end=" -       ")
#         print(published[books_title.index(books_title[i])])
#     print()

# def tmp_list_before_sorting(arr):
#     tmp_l = []
#     for i in arr:
#         tmp_l.append(i)
#     return tmp_l

# def sort_ascending_by_books_title(arr, books_title, published):
#     print("1. Отсортировать по названию книг:")
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break
#     for i in arr:
#         indx = books_title.index(i)
#         print(i.ljust(30), end=" -       ")
#         print(published[indx])
        
# def sort_ascending_by_published(arr, books_title, published):
#     print("2. Отсортировать по годам выпускаа:")
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#             else: break
#     for i in arr:
#         indx = published.index(i)
#         print((books_title[indx]).ljust(30), end=" -       ")
#         print(i)
        
# def main_prog():
#     menu()
#     while True:
#         user_choice = int(input('-> '))
#         if user_choice == 1:
#             sort_ascending_by_books_title(tmp_list_before_sorting(books_title), books_title, published)
#             menu()
#         elif user_choice == 2:
#             sort_ascending_by_published(tmp_list_before_sorting(published), books_title, published)
#             menu()
#         elif user_choice == 3:
#             spravo4nik(books_title, published)
#             menu()
#         elif user_choice == 4:
#             return
#         else: print("Неправильный ввод. Повторите!")

# main_prog()