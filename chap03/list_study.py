array = [273, 32, 103, "문자열", True, False]
print(array)

list_a = [273, 32, 103, "문자열", True, False]

print(list_a[0])

print(list_a[1:3])

list_a[0] = "변경"

print(list_a)

print(list_a[-1])
print(list_a[-2])
print(list_a[-3])




list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
for sub_list in list_of_list:
    for i in sub_list:
        print(i)