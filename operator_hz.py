import random
a = []
for i in range(100):
    a.append(random.randint(0,100))
result = "netu" if 4 in a else "pon"
print("rezultat:\n",result)