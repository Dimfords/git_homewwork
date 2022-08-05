""" Задание 1
Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.
 """



# def max_delitel_recurs(a, b):
#     if b == 0:
#         return a
#     if a > b:
#         return max_delitel_recurs(b, a % b)
#     else:
#        return max_delitel_recurs(a, b % a)

# print(max_delitel_recurs(12, 30))



""" Задание 4
Написать игру «Пятнашки». """

from random import randint

unic_15 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','/\\']
rand_15 = []

def create_list16(arr_orig, arr_rand):
    for item in arr_orig:
        rand_index = randint(0, len(arr_rand))
        arr_rand.insert(rand_index, item)
    # для теста проверки завершения игры
    # arr_rand = ['01','02','03','04','05','06','07','08','09','10','11','/\\','13','14','15','12']
    return arr_rand

def draw_pole(arr):
    print(" _","_","_","_","_","_","_")
    for i in range (len(arr)):
        if i == 0 or i == 4 or i == 8 or i == 12:
            print(end="|")
        print (arr[i],end=' ')
        if i == 3 or i == 7 or i == 11 or i == 15:
            print(end="|")
            print()
    # print()
    print(" -","-","-","-","-","-","-")
    print()

def where_is_empty(arr):
    i = '/\\'
    ind = arr.index(i)
    return ind

def swap(num, empty_cell, arr):
    ind_num = arr.index(num)
    tmp = arr[empty_cell]
    arr[empty_cell] = arr[ind_num]
    arr[ind_num] = tmp
    return arr

def ansver():
    while True:
        text = input('Введите число от 1 до 15 без 0 нулей:')
        if text.isdigit() == False:
            print('Вводите только целые числа!')
        elif 15 < int(text) or int(text) < 0:
            print('Нет такого числа в игре 15-ки')
        elif int(text) < 10:
                text = "0"+ text
        return text     

def valid_movements(arr, ind):
    possible_mov = []
    # ind = arr.index(num)
    if ind == 0:
        possible_mov.append(arr[1])
        possible_mov.append(arr[4])
    elif ind == 1:
        possible_mov.append(arr[0])
        possible_mov.append(arr[2])
        possible_mov.append(arr[5])
    elif ind == 2:
        possible_mov.append(arr[1])
        possible_mov.append(arr[3])
        possible_mov.append(arr[6])
    elif ind == 3:
        possible_mov.append(arr[2])
        possible_mov.append(arr[7])
    elif ind == 4:
        possible_mov.append(arr[0])
        possible_mov.append(arr[5])
        possible_mov.append(arr[8])
    elif ind == 5:
        possible_mov.append(arr[1])
        possible_mov.append(arr[4])
        possible_mov.append(arr[6])
        possible_mov.append(arr[9])
    elif ind == 6:
        possible_mov.append(arr[2])
        possible_mov.append(arr[5])
        possible_mov.append(arr[7])
        possible_mov.append(arr[10])
    elif ind == 7:
        possible_mov.append(arr[3])
        possible_mov.append(arr[6])
        possible_mov.append(arr[11])
    elif ind == 8:
        possible_mov.append(arr[4])
        possible_mov.append(arr[9])
        possible_mov.append(arr[12])
    elif ind == 9:
        possible_mov.append(arr[5])
        possible_mov.append(arr[8])
        possible_mov.append(arr[10])
        possible_mov.append(arr[13])
    elif ind == 10:
        possible_mov.append(arr[6])
        possible_mov.append(arr[9])
        possible_mov.append(arr[11])
        possible_mov.append(arr[14])
    elif ind == 11:
        possible_mov.append(arr[7])
        possible_mov.append(arr[10])
        possible_mov.append(arr[15])
    elif ind == 12:
        possible_mov.append(arr[8])
        possible_mov.append(arr[13])
    elif ind == 13:
        possible_mov.append(arr[9])
        possible_mov.append(arr[12])
        possible_mov.append(arr[14])
    elif ind == 14:
        possible_mov.append(arr[10])
        possible_mov.append(arr[13])
        possible_mov.append(arr[15])
    else:
        possible_mov.append(arr[11])
        possible_mov.append(arr[14])

    return possible_mov

def endgame(game_arr, win_arr):
    if game_arr == win_arr:
       return True
    return False

def game():
    pole_arr = create_list16(unic_15, rand_15)
    draw_pole(pole_arr)
    c = 0
    while True:
        num = ansver()
        empty_cell = where_is_empty(pole_arr)
        if num in valid_movements(pole_arr, empty_cell):
            pole_arr = swap(num,empty_cell, pole_arr)
            draw_pole(pole_arr)
            c += 1
        else:
            print('Вы не можете передвинуть это число!')
        if endgame(pole_arr, unic_15):
            print("Ура! Вы победили!")
            print('Совершив ', c, ' шагов')
            break
            False

game()

# Быки и коровы и коня на шахматной доске не осилил :), но хотелось сделать. Может разберем на занятии?