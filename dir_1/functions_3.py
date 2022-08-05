""" Задание 1
Написать рекурсивную функцию нахождения степени 
числа. """


# def stepen_recur(num, p):
#     if p == 0:
#         return 1
#     return num * stepen_recur(num, p-1)

# print(stepen_recur(2,997))


""" Задание 2
Написать рекурсивную функцию, которая вычисляет 
сумму всех чисел в диапазоне от a до b. Пользователь вво-
дит a и b. Проиллюстрируйте работу функции примером. """

# def sum_range(min, max):
#     if min > max:
#         return 0
#     if min <= max:
#        return max + sum_range(min, max-1)
#     else:
#         return 0
        
# print(sum_range(1,5))

""" Задание 3
Написать рекурсивную функцию, которая выводит N 
звезд в ряд, число N задает пользователь. Проиллюстри-
руйте работу функции примером. """

# def draw_recur(n):
#     if n != 0:
#        print("*", end=" ")
#        draw_recur(n-1)
    

# draw_recur(997)

""" Задание 4
Написать игру «Крестики-нолики».
 """

fields = [
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.'],]

def print_field(arr):
    print(" ",0,1,2, end="")
    for i in range(3):
        print("\n",i, end="")
        for j in range(3):
            print(arr[i][j],end=" ")

def check_cell(arr, row, col):
    if row < 0 or row >= len(arr):
        return False
    if col < 0 or col >= len(arr[0]):
        return False
    return arr[row][col] == "."

def end_game(arr):
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != ".":
            return True
    for i in range(3):
        if arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != ".":
            return True
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != ".":
        return True
    if arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2] != ".":
        return True
    


def game(arr):
    num = 0
    while True:
        print_field(arr)
        print()
        row = int(input("Введите строку -->"))
        col = int(input("Введите колонку -->"))
        if check_cell(arr,row, col):
            arr[row][col] = "X" if num % 2 == 0 else "0"
            num += 1
        else:
            print("Неправильные координаты")
        if end_game(arr):
            print_field(arr)
            print()
            print("Победа!")
            break


game(fields)