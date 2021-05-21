print(list(range(10)))

print(list(range(5, 10)))

print(list(range(0, 10, 2)))

print(list(range(4,6)))

print(list(range(7,0,-1)))

print(list(range(3,8)))

print(list(range(3,10,3)))

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}
for i in range(0, len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)
print(key_list)

limit = 10000
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
print("{}를 더할 때 {}를 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))