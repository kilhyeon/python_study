example_list = ["요소A", "요소B", "요소C"]
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i, item))
    i += 1

for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

print("단순출력")
print(example_list)
print()

print("# enumberate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
print()


print(list(range(0, 20, 2)))
print()

array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)

array = [i * i for i in range(0, 20, 2)]
print(array)

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)