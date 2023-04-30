import random

awa = random.randrange(1, 101)
min = 0
max = 100
while True:
    wee = int(input(f"請輸入{min}~{max}的整數:"))
    if wee > awa:
        print("再小一點")
        if wee < max:
            max = wee
    if wee < awa:
        print("再大一點")
        if wee > min:
            min = wee
    if wee == awa:
        print("猜中了!!!!!!")
        break
