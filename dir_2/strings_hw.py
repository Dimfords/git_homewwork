""" Практическое задание. String
1.Дана строка, в которой буква h встречается
как минимум два раза . Разверните
последовательность символов, заключенную
между первым и последним появлением буквы
h, в противоположном порядке.  """

# s = "Hello h world h"
# pos1 = s.find("h")
# pos2 = s.find("h",(pos1+1))
# res = s[(pos2-1):(pos1):-1]
# print(res)

""" 2.Дана строка. Удалите из этой строки все
символы n.  """

# s = "The BBC visited five separate impact sites in residential neighbourhoods in Kharkiv and saw evidence of a distinctive, symmetrical spalling effect associated with cluster munitions. We showed images from the sites to three weapons experts, who all said the impacts were consistent with the controversial weapons."
# c =s.count('n')
# print(s.replace('n', '', c))


""" 3.Дана строка. Замените в этой строке все
появления буквы h на букву H, кроме
первого и последнего вхождения.  """

# s = "The BBC visited five separate impact sites in residential neighbourhoods in Kharkiv and saw evidence of a distinctive, symmetrical spalling effect associated with cluster munitions. We showed images from the sites to three weapons experts, who all said the impacts were consistent with the controversial weapons."

# reverce_s = s[::-1]
# pos_first = s.find("h")
# pos_end = len(s) - reverce_s.find("h")
# count_replacement = s.count("h")

# tmp_res = s.replace('h', 'H', count_replacement)
# res = tmp_res[:pos_first] +'h'+tmp_res[pos_first+1:pos_end-1] + 'h' + tmp_res[pos_end:]

# print(res)


""" 4.Дана строка. Удалите из нее все символы,
чьи индексы делятся на 3.  """

s = "The BBC visited five separate impact sites in residential neighbourhoods in Kharkiv and saw evidence of a distinctive, symmetrical spalling effect associated with cluster munitions. We showed images from the sites to three weapons experts, who all said the impacts were consistent with the controversial weapons."

res = ""
str_len = len(s)
for i in range(str_len):
    if i%3 != 0: 
        res = res + s[i]
        
print(res)

""" 5.Дана строка. Замените в этой строке все
цифры 1 на слово one.  """

# s = "The 1 BBC visited 5 separate impact sites in 1 residential neighbourhoods in Kharkiv 1"

# str_len = len(s)
# res = ""

# for i in range(str_len):
#     if s[i] == str(1): 
#         res = res + "one"
#     else:
#         res = res + s[i]

# print(res)