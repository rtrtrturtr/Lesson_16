import json
import random
'''
person = {
    "name":"max",
    "age":10,
    "phones":["9111","76536765"]
}
result = json.dumps(person)
print(result)
print(type(result))
#=========================================================================================
spisok = {
    "что-то":2,
    "тоже что-то":3,
    "опять что-то":4
}
spisok = json.dumps(spisok)
print(spisok)
print(type(spisok))
'''

numbers = []
for i in range(10):
    numbers.append(random.randint(0,14))
print(numbers)
if 13 in numbers:
    print("есть тут 13")
else:
    print("нету тут 13")
#======================================================================================
a = int(input("yfgbib"))
spisok = (1,2,3,4,5,6,7,8,9,10,11,12,13,10000,15,16,17,18,19,20)

print(f"est tut {a}") if a in spisok else print(f"nety tut {a}")