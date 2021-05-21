from builtins import dict

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
for i in dictionary["ingredient"]:
    print("ingredient: ", i)
print("origin: ", dictionary["origin"])
print()

dictionary["name"] = "80D 건조 망고"
print("name: ", dictionary["name"])

name = "이름"
dict_key = {
    name: "7D 건조 망고",
    type: "당절임"
}

print(dict_key)

dictionary["price"] = 5000
dictionary["name"] = "80D 건조 파인애플"
del dictionary["ingredient"]
print(dictionary)

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

key = input("> 접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else :
    print("존재하지 않는 키에 접근하고 있습니다.")