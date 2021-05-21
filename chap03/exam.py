numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
numberTo100 = [i for i in numbers if i >= 100]
print("100이상의 수", numberTo100)


list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
for sub_list in list_of_list:
    for i in sub_list:
        print(i)

list_seq = [i for sub_list in list_of_list for i in sub_list]
print("list_seq", list_seq)